# Math Art

An exploration of math, code, and visual art.

## Strange Attractors

The GIFs of the strange attractors can be found in:<br />
 - [https://github.com/ronikbhaskar/math-art/tree/main/strange_attractors/attractor_gifs](https://github.com/ronikbhaskar/math-art/tree/main/strange_attractors/attractor_gifs)

I stumbled across the idea of modeling strange attractors completely on accident, but it piqued my interest, so I ran with it. There are plenty of online resources that discuss strange attractors and their history, which I won't get into here, but it's definitely worth exploring. 

My process isn't the cleanest or most efficient, but that was never the goal. I'm just here to make some art.

### Summary

Here's how I generate these animations. First, I pick a strange attractor and save its differential equations as a function in `attractors.py`. Next, I use SciPy's `odeint` function to generate the curves for a bunch of initial conditions (initial x, y, and z coordinates for the trajectories). Then, I loop through the list of points that make the curve and graph them one frame at a time. Finally, I add some pretty colors and tails to make everything look a bit nicer, and I save the whole thing as a GIF.

### Simulation Class

I created the `Simulation` class, defined in `modeling.py`, to simplify the process of animating chaotic attractors. The constructor takes the following arguments:<br />

 - name : str
   - Title of the figure when plotted
 - ode : function
   - A function used to describe set of ordinary differential equations.
   - The first argument must be tuple of x, y, and z.
   - The second argument must be time.
 - args : tuple
   - The remaining arguments for ode
 - t_final : int
   - final time
 - num_t_values : int
   - number of times to evenly split the range of time values
 - num_trajectories : int, optional
   - The number of points you want flying around the screen
 - tail_length : int, optional
   - The length of each trajectory's "comet tail," in terms of the number of points
 - t_initial : int, optional
   - initial time
 - velocity : int, optional
   - number of points to skip per frame in animation
 - color : str, optional
   - defaults to blue
   - determines the color of the graph
   - current options: blue, green, pink, orange
 - seed : int, optional
   - the random seed used for generating initial points

All optional arguments are keyword arguments.

There are a lot, I know, but most of the time, you only need the first five arguments. The rest can be adjusted to fine-tune the animation.

You can change some animation parameters as needed:
 - `set_start_frame` changes when the animation begins
   - takes int
 - `set_limits` set the viewing limits for the graph in each axis with 2-tuples 
   - takes (float, float),(float, float),(float, float)
 - `set_perspective` set perspective using altitude and azimuth degrees 
   - takes (float, float)
 - `set_rotation` changes the rotation function for each camera angle component
   - takes kwargs: alt_rotation = "static", azim_rotation = "static" (kwargs can be "static", "dynamic", or "partial")

Once everything has been adjusted, the `generate_animation()` method generates the animation. This should be immediately followed by either `show_animation()` or `save_gif(file_name)`.

## References / Inspiration

### Fractals:

 - My middle school math teacher for showing me the Sierpinski Triangle and the Koch Curve<br />

### Strange Attractors: 

 - Bernd Ulmann, "The Aizawa attractor", December 2018, https://analog-paradigm.com/downloads/alpaca_17.pdf<br />
 - Christian Hill, "The Lorenz attractor", December 2015, https://scipython.com/blog/the-lorenz-attractor/<br />
 - CodeParade, "Chaos Equations - Simple Mathematical Art", March 2019, https://www.youtube.com/watch?v=fDSIRXmnVvk<br />
 - Jake VanderPlas, "Animating the Lorenz System in 3D", February 2013, https://jakevdp.github.io/blog/2013/02/16/animating-the-lorentz-system-in-3d/<br />
 - Julien C. Sprott, "Strange Attractors", Winter 2008, https://sprott.physics.wisc.edu/pubs/paper317.pdf<br />
 - Orfeas Liossatos, "Are there other Chaotic Attractors", March 2019, https://www.youtube.com/watch?v=idpOunnpKTo<br />
