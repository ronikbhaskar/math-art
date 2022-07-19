"""
TODO: Documentation
"""

# Imports
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits import mplot3d

mpl.use("webagg") # horrible, but prevents segfaults for now

# Constants
COLOR = (10 / 255, 243 / 255, 1)
DIM = 5
FPS = 24
LENGTH = 3.5
HEIGHT = 5
STRUCT_PTS = [
    [[-5, 5], [0, 0], [HEIGHT, HEIGHT]],
    [[-5, -5], [-1, 0], [0, HEIGHT]],
    [[-5, -5], [1, 0], [0, HEIGHT]],
    [[5, 5], [-1, 0], [0, HEIGHT]],
    [[5, 5], [1, 0], [0, HEIGHT]],
]
INIT_SWING_PTS = [
    [[-1, -1], [0, 0], [HEIGHT, HEIGHT - LENGTH]],
    [[1, 1], [0, 0], [HEIGHT, HEIGHT - LENGTH]],
]
INIT_SEAT_PTS = [
    [
        [-1, 1, 1, -1, -1],
        [0.5, 0.5, -0.5, -0.5, 0.5],
        [HEIGHT - LENGTH, HEIGHT - LENGTH, HEIGHT - LENGTH, HEIGHT - LENGTH, HEIGHT - LENGTH]
    ]
]
GRAVITY = 9.81 # it really doesn't matter

class Simulation:

    def __init__(self):
        """
        theta : angle between downward direction and swing arms
        omega : angular velocity
        """

        self.theta = -np.pi / 6
        self.omega = 0
        self.swing_pts = INIT_SWING_PTS
        self.seat_pts = INIT_SEAT_PTS


    def update(self, dt):
        """
        dt : time interval for updating simulation
        has little translation to real world
        """

        alpha = - GRAVITY / LENGTH * np.sin(self.theta)
        self.omega += alpha * dt
        self.theta += self.omega * dt

    def get_new_pts(self):
        """
        calculates new points based on updated angles
        """
        sin_t = np.sin(self.theta)
        cos_t = np.cos(self.theta)
        for pts in self.swing_pts:
            pts[1][1] = LENGTH * sin_t
            pts[2][1] = HEIGHT - LENGTH * cos_t

        # could this be more concise? yes
        # do I have the time? no
        self.seat_pts[0][1][0] = self.swing_pts[0][1][1] + 0.5 * cos_t
        self.seat_pts[0][2][0] = self.swing_pts[0][2][1] + 0.5 * sin_t
        self.seat_pts[0][1][4] = self.seat_pts[0][1][0]
        self.seat_pts[0][2][4] = self.seat_pts[0][2][0]
        self.seat_pts[0][1][3] = self.swing_pts[0][1][1] - 0.5 * cos_t
        self.seat_pts[0][2][3] = self.swing_pts[0][2][1] - 0.5 * sin_t

        self.seat_pts[0][1][1] = self.swing_pts[1][1][1] + 0.5 * cos_t
        self.seat_pts[0][2][1] = self.swing_pts[1][2][1] + 0.5 * sin_t
        self.seat_pts[0][1][2] = self.swing_pts[1][1][1] - 0.5 * cos_t
        self.seat_pts[0][2][2] = self.swing_pts[1][2][1] - 0.5 * sin_t

    def animate(self, name):
        """
        name : str, title of animation
        """
        fig = plt.figure(name, figsize=(4.8, 4.8))
        ax = fig.add_axes([0, 0, 1, 1], projection='3d')
        ax.axis("off")
        ax.set_facecolor("black")
        ax.view_init(elev=20)

        structure = sum([ax.plot(xs, ys, zs, '-', linewidth=1, c=COLOR) for (xs, ys, zs) in STRUCT_PTS], [])
        swing = sum([ax.plot(xs, ys, zs, '-', linewidth=1, c=COLOR) for (xs, ys, zs) in INIT_SWING_PTS], [])
        seat = sum([ax.plot(xs, ys, zs, '-', linewidth=1, c=COLOR) for (xs, ys, zs) in INIT_SEAT_PTS], [])
        
        limits = (-DIM, DIM)
        ax.set_xlim(limits)
        ax.set_ylim(limits)
        ax.set_zlim(limits)

        def animation_fxn(_):

            self.update(0.12)

            self.get_new_pts()

            for pts, piece in zip(self.swing_pts, swing):
                piece.set_data(pts[0], pts[1])
                piece.set_3d_properties(pts[2])

            for pts, piece in zip(self.seat_pts, seat):
                piece.set_data(pts[0], pts[1])
                piece.set_3d_properties(pts[2])

            fig.canvas.draw()
            return structure + swing + seat

        interval = 1000 / FPS

        anim = animation.FuncAnimation(fig, animation_fxn, 
                                frames=1000, interval=interval)

        plt.show()

# Main block
def main():
    sim = Simulation()
    sim.animate("Swing")

if __name__ == "__main__":
    main()