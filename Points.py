###############################################################################
# Name: Dax Henson
# Date: 2017/03/15
# Description: Implements 2D point class in Python.
###############################################################################
from math import sqrt


# the 2D point class
class Point(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, arg):
        self._x = float(arg)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, arg):
        self._y = float(arg)

    def dist(self, arg):
        return sqrt((self.x - arg.x)**2 + (self.y - arg.y)**2)

    def midpt(self, arg):
        return "({},{})".format((self.x + arg.x) / 2, (self.y + arg.y) / 2)

    def __str__(self):
        return("({},{})").format(self.x, self.y)


##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print "p1:", p1
print "p2:", p2
print "p3:", p3
# calculate and display some distances
print "distance from p1 to p2:", p1.dist(p2)
print "distance from p2 to p3:", p2.dist(p3)
print "distance from p1 to p3:", p1.dist(p3)
# calculate and display some midpoints
print "midpt of p1 and p2:", p1.midpt(p2)
print "midpt of p2 and p3:", p2.midpt(p3)
print "midpt of p1 and p3:", p1.midpt(p3)
