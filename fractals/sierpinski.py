"""
Old recursive sierpinski triangle script I made.
I decided it would fit with everything I was doing.
Made some changes to turn it into a single function.
TODO: Added a koch curve function.
"""

from tkinter import *
import turtle
import os
import shutil
from typing import Callable
from pathlib import Path
from helpers.ps_to_image import make_gif

SIDE_LENGTH = 600
FPS = 12
BASE_FOLDER = os.path.dirname(os.path.realpath(__file__))
TEMP_FOLDER = "pleaseignorethistempfolder"

def sierpinski(side_length, pen):
    """
    Single function with no arguments to draw Sierpinski Triangle
    """

    turtle.Screen().setup(side_length * 1.5,side_length * 1.5)
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.backward(side_length/4)
    pen.left(60)
    pen.backward(side_length/2)
    pen.pendown()
    for _ in range(3):
        pen.forward(side_length)
        pen.right(120)

    def _sierpinski(size):
        """simple recursive function to draw upside down triangles"""

        if size < side_length / 100:
            return
        pen.forward(size)

        for _ in range(3):
            _sierpinski(size/2)
            pen.right(60)
            pen.forward(size)
            pen.right(60)

        pen.backward(size)

    _sierpinski(side_length / 2)

# def defunct_function(draw : Callable, name : str, out_file : str) -> Image:
#     """
#     combines images in postscript folder as frames of gif
#     assumes images are sorted
#     """

#     Path(TEMP_FOLDER).mkdir(parents = True, exist_ok = False)
#     drawing_is_running = True

#     def save(interval : int, folder : str, index : int):
#         """saves turtle screen every interval as postscript file to folder"""
#         if drawing_is_running:
#             print("{0}/{1}{2:04d}{3}".format(folder, name, index, PS_EXT))
#             turtle.getcanvas().postscript(file="{0}/{1}{2:04d}{3}".format(folder, name, index, PS_EXT))
#             index += 1
#             turtle.ontimer(lambda: save(interval, folder, index), interval)

#     interval = int(1000 / FPS)
#     turtle.ontimer(lambda: save(interval, TEMP_FOLDER, 0), interval)
#     draw()
#     drawing_is_running = False

#     images = generate_image_list(TEMP_FOLDER)
#     images[0].save(out_file, 
#                    save_all = True, 
#                    append_images = images[1:], 
#                    loop = 0)

#     shutil.rmtree(TEMP_FOLDER)

if __name__ == "__main__":
    make_gif(lambda: sierpinski(SIDE_LENGTH, turtle.Turtle()), "sierpinski", f"{BASE_FOLDER}/test8.gif")
    # sierpinski(SIDE_LENGTH, turtle.Turtle())
