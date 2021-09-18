"""
Old recursive sierpinski triangle script I made.
I decided it would fit with everything I was doing.
Made some changes to turn it into a single function.
"""

import turtle
import os
from helpers.ps_to_image import make_gif
from helpers.background import draw_gradient_bkg
from math import sqrt

def sierpinski(side_length, pen):
    """
    Single function to draw Sierpinski Triangle
    """

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

def sierpinski_simultaneous(side_length, pen):
    """
    modified function to draw the three corners "simultaneously"
    """

    # this line is to vertically center the triangle
    # based on the starting position of the pen
    pen.sety(pen.pos()[1] - side_length * sqrt(3) / 12)

    pen2 = pen.clone()
    pen3 = pen.clone()
    pens = [pen, pen2, pen3]
    for i, pen in enumerate(pens):
        pen.speed(0)
        pen.hideturtle()
        pen.penup()
        pen.right(i * 120)
        pen.left(30)
        pen.backward(side_length/sqrt(3))
        pen.left(30)
        pen.pendown()
        pen.forward(side_length)
        pen.right(120)
        pen.forward(side_length / 2)

    def _sierpinski_simultaneous(size, pens):
        """recursive function to draw the corners"""
        if size < side_length / 100:
            return
        [pen.forward(size) for pen in pens]

        for _ in range(3):
            _sierpinski_simultaneous(size/2, pens)
            for pen in pens:
                pen.right(60)
                pen.forward(size)
                pen.right(60)

        [pen.backward(size) for pen in pens]

    _sierpinski_simultaneous(side_length / 4, pens)

if __name__ == "__main__":
    side_length = 450
    image_folder = os.path.dirname(os.path.realpath(__file__)) + "/images"
    tortoise=turtle.Turtle()
    tortoise.color("white")
    turtle.Screen().setup(side_length * 1.5,side_length * 1.5)
    tortoise.speed(0)
    tortoise.hideturtle()
    draw_gradient_bkg((255/255,249/255,194/255),
                      (255/255,167/255,145/255),
                      700,700)
    turtle.tracer(1,3)
    make_gif(lambda: sierpinski_simultaneous(side_length, tortoise), 
             "sierpinski", f"{image_folder}/sierpinski.gif", 
             square = True, compressed = False)
