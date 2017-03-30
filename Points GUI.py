###############################################################################
# Name: Dax Henson
# Date: 2017/03/20
# Description: Implements 2D point class in Python and plots points.
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

    def dist(self, arg):
        # uses the pythagorean theorem to find the distance between two points
        return sqrt((self.x - arg.x)**2 + (self.y - arg.y)**2)

    def midpt(self, arg):
        # uses the midpoint theorem to find the midpoint between two points
        return "({},{})".format((self.x + arg.x) / 2, (self.y + arg.y) / 2)

    def __str__(self):
        # prints the point in the proper format
        return("({},{})").format(self.x, self.y)


# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):

    # initializes a canvas with which to render images
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    # outlines the steps to plot a passed amount of points in random locations
    def plotPoints(self, n):
        for i in range(n):
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            self.plot(x, y)

    # function for rendering a point at a passed location in a random color
    def plot(self, x, y):
        color = COLORS[randint(0, len(COLORS) - 1)]
        self.create_oval(x, y, x + POINT_RADIUS * 2,
                         y + POINT_RADIUS * 2,
                         outline=color)


##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 400x400
WIDTH = 400
HEIGHT = 400
# the default point radius is 0 pixels (i.e., no center to the oval)
POINT_RADIUS = 0
# colors to choose from when plotting points
COLORS = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
# the number of points to plot
NUM_POINTS = 2500

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
