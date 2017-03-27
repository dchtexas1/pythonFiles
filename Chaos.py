######################################################################################################################
# Name: 
# Date: 
# Description: 
######################################################################################################################

# the 2D point class
class Point(object):
	# write your code for the point class here (and subsequently remove this comment)

# the chaos game class
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
	# write your code for the chaos game class here (and subsequently remove this comment)

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
