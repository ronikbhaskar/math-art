"""
Old recursive sierpinski triangle script I made.
I decided it would fit with everything I was doing.
Made some changes to turn it into a single function.
"""

from tkinter import *
import turtle
from helpers.ps_to_image import make_gif

SIDE_LENGTH = 300

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

        if size < 3:
            return
        pen.forward(size)

        for _ in range(3):
            _sierpinski(size/2)
            pen.right(60)
            pen.forward(size)
            pen.right(60)

        pen.backward(size)

    _sierpinski(side_length / 2)

if __name__ == "__main__":
    make_gif(lambda: sierpinski(SIDE_LENGTH, turtle.Turtle()), "test.gif")
    # sierpinski(SIDE_LENGTH, turtle.Turtle())
