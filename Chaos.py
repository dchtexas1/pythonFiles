###############################################################################
# Name: Dax Henson
# Date: 2017/03/30
# Description: Utilizes the chaos game to create a Sierpienski Triangle
###############################################################################
from Tkinter import *
from random import randint


# the 2D point class
class Point(object):

    # constructor; sets default x and y values and instantiates them
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    # accessors and mutators for the x and y values
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, arg):
        # converts the given value to a floating point value
        self._x = float(arg)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, arg):
        # converts the given value to a floating point value
        self._y = float(arg)

    # uses the midpoint theorem to find each midpoint value between two points
    def midpt(self, arg):
        return Point(((self.x + arg.x) / 2), ((self.y + arg.y) / 2))


# the chaos game class
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):

    # initializes a canvas with which to render images
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def play(self, n):
        self.vertices()
        # duplicates two random vertices
        p1 = vtcs[randint(0, 2)]
        p2 = vtcs[randint(0, 2)]
        # finds the midpoint of the two points
        m = p1.midpt(p2)
        self.plot(m.x, m.y, POINT_COLOR)
        # plots the passed number of points
        for i in xrange(n):
            # selects a singular random vertex
            v = vtcs[randint(0, 2)]
            # finds and plots the midpoint between v and the previous midpoint
            m1 = m.midpt(v)
            self.plot(m1.x, m1.y, POINT_COLOR)
            # moves on to finding the next midpoint
            m = m1

    # plots the three initial vertices
    def vertices(self):
        # the top vertex
        v1 = Point(WIDTH / 2, 0)
        self.plot(v1.x, v1.y, VERTEX_COLOR, "vertex")
        # the bottom left vertex
        v2 = Point(0, HEIGHT)
        self.plot(v2.x, v2.y, VERTEX_COLOR, "vertex")
        # the bottom right vertex
        v3 = Point(WIDTH, HEIGHT)
        self.plot(v3.x, v2.y, VERTEX_COLOR, "vertex")
        # creates an array to keep track of the list
        global vtcs
        vtcs = [v1, v2, v3]

    def plot(self, x, y, color, pointType="point"):
        if (pointType == "vertex"):
            self.create_oval(x, y, x + VERTEX_RADIUS * 2,
                             y + VERTEX_RADIUS * 2, outline=color, fill=color)
        elif (pointType == "point"):
            self.create_oval(x, y, x + POINT_RADIUS * 2,
                             y + POINT_RADIUS * 2, outline=color, fill=color)


##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
# the default vertex radius is 2 pixels and color is red
VERTEX_RADIUS = 2
VERTEX_COLOR = "red"
# the default point radius is 0 pixels and color is black
POINT_RADIUS = 0
POINT_COLOR = "black"
# the number of midpoints to plot
NUM_POINTS = 50000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
# create the chaos game as a Tkinter canvas inside the window
s = ChaosGame(window)
# play the chaos game with at least 50000 points
s.play(NUM_POINTS)
# wait for the window to close
window.mainloop()
