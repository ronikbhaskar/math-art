"""
helper to draw gradient backgrounds
IMPORTANT: if you use this, it's fine on the turtle window,
but it is HORRIBLE for conversion to actual images.
Turtle graphics were not made to create gradients, 
at least not like this.
"""

import turtle
from turtle import Screen, Turtle
from time import sleep

def draw_gradient_bkg(color1, color2, width, height, 
                      vertical = True, resolution = 1):
    """
    draws a gradient rectangle with proportions width, height
    centered at (0,0)
    boolean vertical is direction of gradient
    """

    assert type(color1) is tuple and type(color2) is tuple, \
        f"colors must be 3-tuples"

    turtle.tracer(0,0)
    num_incs = height if vertical else width
    increments = [(end - start) / (num_incs // resolution) \
                  for end, start in zip(color2,color1)]
    
    tortoise = Turtle()
    tortoise.color(color1)
    tortoise.pensize(resolution)
    tortoise.speed(0)
    tortoise.hideturtle()
    tortoise.penup()
    x_start, y_start = -width//2, height//2
    tortoise.goto(x_start, y_start)
    if not vertical:
        tortoise.right(90)
    tortoise.pendown()

    for pixel_num, pos in enumerate(range(num_incs // 2, num_incs // -2, -resolution)):

        tortoise.forward(width if vertical else height)
        tortoise.color(tuple([start + increment * pixel_num \
                             for start, increment in zip(color1, increments)]))
        tortoise.penup()
        if vertical:
            tortoise.setx(x_start)
            tortoise.sety(pos)
        else:
            tortoise.setx(-pos)
            tortoise.sety(y_start)
        tortoise.pendown()

    turtle.update()
    turtle.tracer(1,10)
    sleep(3)

if __name__ == "__main__":
    draw_gradient_bkg((1,0,0),(0,1,1),200,200, resolution = 10)