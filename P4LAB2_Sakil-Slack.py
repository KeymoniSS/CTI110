# This program should display my first and last initials
# September 19, 2018
# CTI-110 P4T1 - Turtle Lab
# Keymoni Sakil-Slack
#

import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("First and Last initials")

#Create square
first_initial = turtle.Turtle()
first_initial.color("limegreen")
first_initial.pensize(3)

#Draw the letter K
first_initial.penup()
first_initial.backward(100)
first_initial.pendown()

first_initial.left(90)
first_initial.forward(105)
first_initial.penup()
first_initial.backward(50)
first_initial.pendown()
first_initial.right(45)
first_initial.forward(65)
first_initial.backward(55)
first_initial.right(90)
first_initial.forward(90)


#Create Triangle
last_initial = turtle.Turtle()
last_initial.color("yellow")
last_initial.pensize(3)

last_initial.penup()
last_initial.backward(50)
last_initial.left(90)
last_initial.forward(100)
last_initial.right(90)
last_initial.forward(100)
last_initial.pendown()

last_initial.right(180)
last_initial.forward(50)
last_initial.left(45)
last_initial.forward(35)
last_initial.left(90)
last_initial.forward(35)
last_initial.left(45)
last_initial.forward(45)
last_initial.right(45)
last_initial.forward(35)
last_initial.right(90)
last_initial.forward(35)
last_initial.right(45)
last_initial.forward(65)



wn.mainloop()
