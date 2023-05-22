# Moves turtle in random directions and for random distances.
# Using different values in "angles" and "lengths" can create different 
#   shapes/patterns like hexagons, trapezoids, and especially triangles.

import turtle, random
from time import time


# Define window size variables and change some settings
width = 900
height = 800
turtle.screensize(width, height)
turtle.speed(0) # fastest speed

# Lists containing random angles and distances to move
angles = [-60, 60]
lengths = [25, 50, 100]

# Loop forever
while (True): 
    # Use random.choice to pick a random length and angle to move
    turtle.forward(random.choice(lengths))
    turtle.right(random.choice(angles))

    # Go home if moved past an edge
    # turtle.xcor() and .ycor() return the x and y coordinates of the turtle.
    # I use the width and height assigned above for checking if the turtle 
    #   has passed an edge. Divide by 2 because (0,0) is in the center, 
    #   and width/height are the full width and height of the window. 
    if (turtle.xcor() > width/2 
            or turtle.xcor() < -width/2 
            or turtle.ycor() > height/2 
            or turtle.ycor() < -height/2):
        turtle.up()
        turtle.home()
        turtle.down()