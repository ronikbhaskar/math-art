"""
This file consists of the Simulation class and all of its functionality,
including generating and saving animations.
"""

import numpy as np
from scipy.integrate import odeint

from matplotlib import pyplot as plt
from matplotlib import animation

from math import floor
from functools import partial

from attractors import lorenz, halvorsen

class Simulation:
    """primary class for creating, rendering, and saving animations"""

    FPS = 24
    
    VIEWS = {
        "xy": (-90, 90),
        "xz": (0, 90),
        "yz": (0, 0)
    }
    
    COLORS = { # RGB on a 0 to 1 scale
        "blue": (10/255, 243/255, 1, 0.65),
        "green": (120/255, 1, 120/255, 0.65),
        "pink": (1, 133/255, 200/255, 0.65),
        "orange": (1, 135/255, 15/255, 0.65),
    }

    def __init__(self, name, ode, args, t_final, num_t_values,
                 num_trajectories = 100, tail_length = 50, t_initial = 0, 
                 velocity = 3, period = 360, color = "blue", seed = 1):
        """
        Parameters
        ----------
        name : str
            Title of the figure when plotted
        ode : function
            A function used to describe set of ordinary differential equations.
            The first argument must be tuple of x, y, and z.
            The second argument must be time.
        args : tuple
            The remaining arguments for ode
        num_trajectories : int, optional
            The number of points you want flying around the screen
        tail_length : int, optional
            The length of each trajectory's "comet tail,"
            in terms of the number of points
        t_initial : int
            initial time
        t_final : int
            final time
        num_t_values : int
            number of times to evenly split the range of time values
        velocity : int
            number of points to skip per frame in animation
        color : str, optional
            defaults to blue
            determines the color of the graph
            current options: blue, green, pink
        seed : int, optional

        """
        assert color in Simulation.COLORS.keys(), f"color {color} not available"

        np.random.seed(1)
        self.num_trajectories = num_trajectories
        self.tail_length = tail_length
        self.t_values = np.linspace(t_initial, t_final, num_t_values)
        self.velocity = velocity
        self.period = period # in frames for rotation function

        self.rotate_alt = lambda x: 0
        self.rotate_azim = lambda x: 0

        # all points less than 0.01 away from (0, 0, 0)
        initial_values = -0.005 + 0.01 * np.random.random((num_trajectories,3))
        self.trajectories = np.asarray([odeint(ode, 
                                               point, 
                                               self.t_values, 
                                               args=args)
                                        for point in initial_values])
        
        # standard matplotlib
        self.fig = plt.figure(name ,figsize = (4.8,4.8))
        self.ax = self.fig.add_axes([0, 0, 1, 1], projection='3d')
        self.fig.subplots_adjust(left=0, bottom=0, right=1, top=1, 
                                 wspace=None, hspace=None)
        self.ax.axis("off")
        self.ax.set_facecolor("black")

        self.color = Simulation.COLORS[color]
        self.start_frame = 0
        # the [] at the end of the sum function is the initial value,
        # so each element of the list comprehension is appended to a list.
        # Since each element is a list, this turns [[plot],[plot],[plot],...]
        # into [plot,plot,plot,...].
        self.tails = sum([self.ax.plot([],[],[],'-',linewidth=0.1,c=self.color) 
                          for _ in range(num_trajectories)],[])
        self.heads = sum([self.ax.plot([],[],[],'.',markersize = 0.1,c="white") 
                          for _ in range(num_trajectories)],[])

    def set_start_frame(self, start_frame):
        """changes when the animation begins"""

        self.start_frame = start_frame
    
    def set_limits(self, x_limits, y_limits, z_limits):
        """set the viewing limits for the graph in each axis with 2-tuples"""

        self.ax.set_xlim(x_limits)
        self.ax.set_ylim(y_limits)
        self.ax.set_zlim(z_limits)

    def set_perspective(self, perspective):
        """set perspective using altitude and azimuth degrees"""

        if perspective in Simulation.VIEWS.keys():
            alt, azim = Simulation.VIEWS[perspective]
        else:
            alt, azim = perspective
        self.ax.view_init(alt, azim)
        self.rotate_alt = lambda x: alt
        self.rotate_azim = lambda x: azim

    def get_rotation_function(self, rotation_type, initial):
        """returns rotation function for given type and initial value"""

        if rotation_type == "linear":
            return lambda x: initial + x * 360 / self.period
        elif rotation_type == "dynamic":
            return lambda x: initial + 360 / self.period * x - \
                             90 / np.pi * np.sin(4 * np.pi * x / self.period)
            # return lambda x: initial - 180 + \
            #                  180 * np.cos(2 * np.pi * x / self.period)
        elif rotation_type == "partial":
            return lambda x: initial * np.cos(2 * np.pi * x / self.period)
        else:
            return lambda x: initial

    def set_rotation(self, alt_rotation = "static", azim_rotation = "static"):
        """changes the rotation function for each camera angle component"""

        self.rotate_alt = self.get_rotation_function(alt_rotation, 
                                                     self.ax.elev)
        self.rotate_azim = self.get_rotation_function(azim_rotation, 
                                                      self.ax.azim)

    def get_animation_function(self):
        """instance method for animation, will converted to static method"""

        def animate(i):
            """i is a counter for the current frame"""
            
            self.ax.view_init(self.rotate_alt(i), self.rotate_azim(i))
            
            i += self.start_frame
            i = floor(self.velocity * i) % self.trajectories.shape[1]

            for tail, head, traj in zip(self.tails, 
                                        self.heads, 
                                        self.trajectories):
                x, y, z = traj[max(0, i - self.tail_length):i].T
                tail.set_data(x, y)
                tail.set_3d_properties(z)

                head.set_data(x[-1:], y[-1:])
                head.set_3d_properties(z[-1:])

            self.fig.canvas.draw()
            return self.tails + self.heads
        
        return animate

    def generate_animation(self):
        """uses base_animation function to generate animation"""

        animate = self.get_animation_function()
        frames = len(self.t_values) // self.velocity
        interval = 1000 // Simulation.FPS
        self.anim = animation.FuncAnimation(self.fig, animate, 
                                            frames=frames, interval=interval,
                                            blit=False)
    
    def show_animation(self):
        """must run generate_animation before this"""

        plt.show()

    def save_gif(self, file_name):
        """must run generate_animation before this"""

        self.anim.save(file_name, writer = "ffmpeg", dpi = 200, fps = Simulation.FPS)

if __name__ == "__main__":
    # lorenz_sim = Simulation("Lorenz Attractor", lorenz, (10, 8 / 3, 28), 30, 3000)
    # lorenz_sim.set_start_frame(1500)
    # lorenz_sim.set_limits((-23, 23), (-23, 23), (11, 40))
    # lorenz_sim.set_perspective("xz")
    # lorenz_sim.show_animation()
    halvorsen_sim = Simulation("Halvorsen Attractor", halvorsen, (1.4,), 10, 1200, color = "pink", num_trajectories = 100, period = 240)
    # halvorsen_sim.set_start_frame(2000)
    halvorsen_sim.set_perspective((-30,-135))
    halvorsen_sim.set_rotation(alt_rotation = "partial", azim_rotation = "dynamic")
    # halvorsen_sim.set_limits((-9, 9), (-9, 9), (-6, 9))
    halvorsen_sim.set_limits((-10, 10), (-10, 10), (-6, 9))
    halvorsen_sim.generate_animation()
    halvorsen_sim.show_animation()
