# This program should draw both a square and a triangle with the for loop
# September 19, 2018
# CTI-110 P4T1 - Turtle Lab
# Keymoni Sakil-Slack
#

import turtle
wn = turtle.Screen()
wn.title("Square and Triangle")

#Create square
square = turtle.Turtle()

#Create for loop
for draw in range(4):
    square.forward(200)
    square.left(90)

#Create Triangle
triangle = turtle.Turtle()
triangle.color("blue")

#Move Triangle
triangle.penup()
triangle.backward(300)
triangle.pendown()

#Create for loop
for draw in range(3):
    triangle.forward(200)
    triangle.left(120)

wn.mainloop()
