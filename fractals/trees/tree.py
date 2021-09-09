from tkinter import *
import turtle
import time
import math


# the tree class and everything in it

class Tree:

    def trunk_size(self):
        """I base this off of the convergence value for geometric series that sums to 500
        last part accounts for offset"""
        return 500 * (1 - self.proportion) * (3 - self.offset) / 3


    def initial_angle(self):
        return (self.branches - 1) * self.angle / 2

    def branch_to_len(self, branch):
        """this assumes that the trunk is branch 0"""
        return self.trunk_size() * (self.proportion ** branch)

    def setup_pen(self):
        turtle.tracer(0, 0)
        self.pen.setheading(90)
        self.pen.penup()
        self.pen.sety(-300)
        self.pen.pendown()
        self.pen.speed(100000)
        turtle.title("Tree Generator")
        # turtle.bgcolor(self.bkg)
        self.pen.hideturtle()

    def __init__(self, branches, proportion, angle, thickness, color, bkg, color2, offset, layers, transition_branch):
        """branches,proportion,angle,thickness,color,bkg,color2,offset,cutoff,transition_length"""

        # in case the user closes the screen
        if not turtle.TurtleScreen._RUNNING: # necessary for the code to run, but doesn't follow conventions
            turtle.Turtle._screen = None  # force recreation of singleton Screen object
            turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition

        self.branches = branches # branches that split
        self.proportion = proportion  # between length of current and previous layer
        self.angle = angle  # between branches, in degrees
        self.i_angle = self.initial_angle()

        self.offset = offset
        self.cutoff = self.branch_to_len(layers) # converts branches to pixel length

        self.thickness = thickness  # reduces each level based on proportion
        self.colors = [color, color2]
        self.bkg = bkg  # if i really want to implement a background
        self.tlength = self.branch_to_len(transition_branch) # converts branches to pixel length

        self.pen = turtle.Turtle()
        self.pen.hideturtle()


        self.canvas = None
        # self.canvas = self.pen.getscreen()

    '''
    # old version - didn't work very well with the GUI
    def __init__(self, branches, proportion, angle, thickness, color, bkg, color2, offset, cutoff, transition_length):
        """branches,proportion,angle,thickness,color,bkg,color2,offset,cutoff,transition_length"""
        self.branches = branches
        self.proportion = proportion  # between length of current and previous layer
        self.angle = angle  # between branches, in degrees
        self.i_angle = self.initial_angle()

        self.thickness = thickness  # reduces each level based on proportion
        self.colors = [color, color2]
        self.bkg = bkg  # if i really want to implement a background
        self.tlength = transition_length

        self.offset = offset
        self.cutoff = cutoff

        self.pen = turtle.Turtle()


        self.canvas = None
        # self.canvas = self.pen.getscreen()
    '''

    def set_thickness(self, size):
        self.pen.width(size * self.thickness)

    def set_color(self, size):
        """determines the branch color based on size"""
        if size > self.tlength:
            self.pen.color(self.colors[0])
        else:
            self.pen.color(self.colors[1])

    def draw_bkg(self):
        """this method exists because setting the bkg through turtle doesn't let you save it in the image"""
        bkg_pen = turtle.Turtle()
        bkg_pen.hideturtle()
        bkg_pen.speed(100000)
        bkg_pen.color(self.bkg)
        bkg_pen.backward(400)
        bkg_pen.begin_fill()
        bkg_pen.left(90)
        bkg_pen.forward(400)
        for _ in range(4):
            bkg_pen.right(90)
            bkg_pen.forward(800)
        bkg_pen.end_fill()

    def save(self,filename):  # does what it says
        self.canvas.getcanvas().postscript(file=filename)
        '''
        if "y" == input("Save Image? y/n: ").lower()[0]:
            self.canvas.getcanvas().postscript(file=input("enter name of file: "))
        #turtle.clearscreen()
        #turtle.bye()
        '''

    def create(self):
        self.setup_pen()
        self.draw_bkg()

        size = self.trunk_size()

        offset_branch = math.trunc(self.branches / 2)

        self._create(size, offset_branch)
        turtle.update()
        self.canvas = turtle.getscreen()
        #self.save()

    def _create(self, size, offset_branch):
        if size < self.cutoff:
            return
        self.set_thickness(size)
        self.set_color(size)

        self.pen.forward(size)
        self.pen.left(self.i_angle)
        for i in range(self.branches):
            self._create(size * self.proportion, offset_branch)  # recursive call

            if i + 1 == offset_branch:
                self.pen.forward(int(self.offset * size))
            elif i + 1 == self.branches:
                self.pen.left(self.angle * (self.branches - offset_branch))
                self.pen.backward(int(self.offset * size))
                self.pen.right(self.angle * (self.branches - offset_branch))
            # this whole block deals with offset to make sure it works with any length

            self.pen.right(self.angle)
        self.pen.left(self.angle + self.i_angle)

        self.set_color(size)
        self.set_thickness(size)
        self.pen.backward(size)


'''
t = Tree(3, 0.8, 20, 1 / 10, "#A0522D", "#00CCFF", "#3A5F0B", 3 / 10, 15, 40)
t = Tree(2, 0.7, 45, 1 / 10, "#000000", "#FFFFFF", "#000000", 0, 10, 0)
t = Tree(4,0.7,25,1 / 10, "#A0522D", "#FFFFFF", "#A0522D", 1, 20, 0)
t = Tree(3, 0.8, 12, 1/10, "#000000", "#FFFFFF", "#FF0000", 0, 0, 2)
t.create()
'''



# this is me testing the tree with different angles before making it recursive to determine if it works
def test():
    tree = turtle.Turtle()
    tree.setheading(90)
    tree.penup()
    tree.sety(-100)
    tree.pendown()
    tree.speed(1)
    size = 50
    branches = 6
    angle = 32  # between branches
    initial_angle = (branches - 1) * angle / 2
    offset = size / 2
    # calculating an initial angle based on branch num and separation was crucial in the beginning

    # everything after this comprises the create method for Tree
    tree.forward(size)
    tree.left(initial_angle)
    for i in range(branches):
        tree.forward(size)
        tree.backward(size)

        if i + 1 == math.trunc(branches / 2):
            tree.forward(int(offset))
        elif i + 1 == branches:
            tree.left(angle * (branches - math.trunc(branches / 2)))
            tree.backward(int(offset))
            tree.right(angle * (branches - math.trunc(branches / 2)))
        # this whole block deals with offset to make sure it works with any length

        tree.right(angle)
    tree.left(angle + initial_angle)
    tree.backward(size)
    time.sleep(5)

# test()
