from turtle import Turtle, title, done as turtled
from time import sleep as turtles

title("turtles all the way down 2")

def turtle(turtled):
    turtle, turtleturtle = Turtle(), Turtle()
    turtle.shape("turtle")
    turtle.turtlesize(10,10,10)
    turtle.color((0,1,0.5) if turtled else (0.5,0.5,1))
    turtleturtle.shape("turtle")
    turtleturtle.turtlesize(3/4,3/4,3/4)
    turtleturtle.color((0.5,0.5,1) if turtled else (0.5,1,0.5))
    for _ in range(30):
        turtle.turtlesize(*[1.09 * turtle for turtle in turtle.turtlesize()])
        turtleturtle.turtlesize(*[1.09 * turtle for turtle in turtleturtle.turtlesize()])
        turtles(1/20)
    return not turtled

turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(turtle(not not True))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
turtled()