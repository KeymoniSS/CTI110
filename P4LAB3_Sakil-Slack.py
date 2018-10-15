# This program should display my first and last initials
# September 19, 2018
# CTI-110 P4T1 - Turtle Lab
# Keymoni Sakil-Slack
#

import turtle
wn = turtle.Screen()
wn.title("Snowflake")

snowflake = turtle.Turtle()
snowflake.color("lightblue")
snowflake.pensize(3)

snowflake.right(90)

for flake in range(6):
    
    snowflake.forward(100)
    snowflake.forward(-40)
    snowflake.left(40)
    snowflake.forward(35)
    snowflake.forward(-35)
    snowflake.right(80)
    snowflake.forward(35)
    snowflake.forward(-35)
    snowflake.left(40)
    snowflake.forward(-60)
    snowflake.left(60)



wn.mainloop()







