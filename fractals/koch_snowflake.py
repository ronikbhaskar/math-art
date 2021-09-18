"""
Since this seemed similar enough to the Sierpinski Triangle script I wrote,
I decided to make one for the Koch Curve, or the Koch Snowflake,
which is just three Koch Curves put together.
"""

import turtle
import os
from helpers.ps_to_image import make_gif
from helpers.background import draw_gradient_bkg
from math import sqrt

BASE_FOLDER = os.path.dirname(os.path.realpath(__file__))
ANGLES = [60, -120, 60, 0]

def koch_snowflake(side_length, seg_length, pen):
    """
    draws a koch snowflake centered at wherever the pen is located
    """

    pen.hideturtle()
    pen.penup()
    pen.left(30)
    pen.backward(2*side_length/3)
    pen.left(30)
    pen.pendown()

    for _ in range(3):
        koch_curve(side_length / 3, seg_length, pen)
        pen.right(120)

    pen.penup()
    pen.right(30)
    pen.forward(side_length/sqrt(3))
    pen.right(30)
    pen.pendown()

def koch_snowflake_simultaneous(side_length, seg_length, pen):
    """
    draws a koch snowflake centered at wherever the pen is located
    """

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

    def _koch_curve_simultaneous(size, seg_length, pens):
        """recursive function to draw the curves that make each side"""

        for angle in ANGLES:
            if size <= seg_length:
                [pen.forward(size) for pen in pens]
            else:
                _koch_curve_simultaneous(size / 3, seg_length, pens)
            [pen.left(angle) for pen in pens]

    _koch_curve_simultaneous(side_length / 3, seg_length, pens)

    for pen in pens:
        pen.speed(1)
        pen.hideturtle()
        pen.penup()
        pen.right(120)
        pen.forward(30)
        pen.pendown()

def koch_nested_snowflakes(side_length, seg_length, pen):
    """
    draws rotated, nested koch snowflakes
    """

    x, y = pen.pos()
    while side_length >= seg_length:
        koch_snowflake(side_length, seg_length, pen)
        pen.penup()
        pen.goto(x,y)
        pen.setheading(0)
        pen.pendown()
        side_length /= 3

def koch_curve(size, seg_length, pen):
    """recursive function to draw the curves that make each side"""

    for angle in ANGLES:
        if size <= seg_length:
            pen.forward(size)
        else:
            koch_curve(size / 3, seg_length, pen)
        pen.left(angle)

if __name__ == "__main__":
    side_length = 350
    image_folder = os.path.dirname(os.path.realpath(__file__)) + "/images"
    seg_length = 4.5
    tortoise = turtle.Turtle()
    tortoise.color("white")
    tortoise.hideturtle()
    turtle.Screen().setup(side_length * 2,side_length * 2)
    draw_gradient_bkg((4/255, 9/255, 96/255),
                      (255/255, 229/255, 195/255),
                      side_length * 2, side_length * 3)
    turtle.tracer(1,5)
    make_gif(lambda: koch_snowflake_simultaneous(side_length, 
                                                 seg_length, 
                                                 tortoise),
            "koch", f"{image_folder}/koch_snowflake.gif",
            square = True, compressed = False)

