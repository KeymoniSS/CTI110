# This program should display the percentage of males and females in a class.
# September 10, 2018
# CTI-110 P2HW2 - Male Female Percentage
# Keymoni Sakil-Slack
#

import turtle
wn = turtle.Screen()
wn.title("Square and Triangle")

#Create square
square = turtle.Turtle()

for draw in range(4):
    square.forward(50)
    square.left(90)

#Create Triangle
triangle = turtle.Turtle()
triangle.color("blue")

for draw in range(3):
    triangle.forward(50)
    triangle.left(120)

wn.mainloop()
