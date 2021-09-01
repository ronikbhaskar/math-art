#!usr/bin/env python3

import os
from pathlib import Path
from modeling import Simulation
from attractors import *

def make_static_lorenz(out_file):
    """
    generates gif of lorenz attractor without rotation
    """

    lorenz_sim = Simulation("Lorenz Attractor", 
                            lorenz, (10, 8 / 3, 28), 
                            30, 
                            5000,
                            num_trajectories = 200)
    lorenz_sim.set_start_frame(2500)
    lorenz_sim.set_limits((-17, 17), (-17, 17), (13, 38))
    lorenz_sim.set_perspective("xz")
    lorenz_sim.generate_animation()
    lorenz_sim.save_gif(out_file)

def make_rotating_lorenz(out_file):
    """
    generates gif of lorenz attractor with rotation
    """

    lorenz_sim = Simulation("Lorenz Attractor", 
                            lorenz, (10, 8 / 3, 28), 
                            30, 
                            5000,
                            num_trajectories = 200,
                            period = 360)
    lorenz_sim.set_start_frame(2500)
    lorenz_sim.set_limits((-23, 23), (-23, 23), (11, 40))
    lorenz_sim.set_perspective("xz")
    lorenz_sim.set_rotation(azim_rotation = "dynamic")
    lorenz_sim.generate_animation()
    lorenz_sim.save_gif(out_file)

def make_static_halvorsen(out_file):
    """
    generates gif of halvorsen attractor without rotation
    """

    halvorsen_sim = Simulation("Halvorsen Attractor", 
                               halvorsen, (1.4,), 
                               10, # t_final
                               1500, # num_t_values
                               color = "pink", 
                               num_trajectories = 200)
    halvorsen_sim.set_perspective((-30,-135))
    halvorsen_sim.set_limits((-9, 9), (-9, 9), (-6, 9))
    halvorsen_sim.generate_animation()
    halvorsen_sim.save_gif(out_file)

def make_rotating_halvorsen(out_file):
    """
    generates gif of halvorsen attractor with rotation
    """

    halvorsen_sim = Simulation("Halvorsen Attractor", 
                               halvorsen, (1.4,), 
                               10, # t_final
                               1500, # num_t_values
                               color = "pink", 
                               num_trajectories = 200, 
                               period = 240)
    halvorsen_sim.set_perspective((-30,-135))
    halvorsen_sim.set_rotation(alt_rotation = "partial",
                               azim_rotation = "dynamic")
    halvorsen_sim.set_limits((-11, 11), (-11, 11), (-6, 9))
    halvorsen_sim.generate_animation()
    halvorsen_sim.save_gif(out_file)

def make_static_aizawa(out_file):
    """
    generates gif of aizawa attractor without rotation
    """

    aizawa_sim = Simulation("Aizawa Attractor",
                            aizawa, (0.95, 0.7, 0.65, 3.5, 0.25, 0.1),
                            20,
                            2000,
                            color = "green",
                            num_trajectories = 200,
                            tail_length = 70)
    aizawa_sim.set_perspective("xz")
    aizawa_sim.set_limits((-1.06, 1),(-1, 1),(0, 1.5))
    aizawa_sim.generate_animation()
    aizawa_sim.save_gif(out_file)

if __name__ == "__main__":
    sim_dict = {"static_lorenz.gif": make_static_lorenz, 
                "rotating_lorenz.gif": make_rotating_lorenz, 
                "static_halvorsen.gif": make_static_halvorsen, 
                "rotating_halvorsen.gif": make_rotating_halvorsen, 
                "static_aizawa.gif": make_static_aizawa}
    base_folder = os.path.dirname(os.path.realpath(__file__))
    folder = f"{base_folder}/attractor_gifs"
    Path(folder).mkdir(exist_ok = True)
    for filename, make_sim in sim_dict.items():
        make_sim(f"{folder}/{filename}")

    