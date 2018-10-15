# This program should draw a shape using a nested loop.
# September 26, 2018
# CTI-110 P4LAB - Nested Loops
# Keymoni Sakil-Slack
#


import turtle
wn = turtle.Screen()
wn.title("Star")

#Create star
star = turtle.Turtle()
star.color("limegreen")

#Optional fill (with color)
star.begin_fill()

#Create for loop
for draw in range(5):
    star.left(72)
    star.forward(200)
    star.left(-144)
    for draw in range(3):
        star.left(-144)
                     
star.end_fill()
wn.mainloop()

# Pseudocode:
# Import the turtle 
# Create loops 
# Input desired angles and lengths
# Output desired shape design
