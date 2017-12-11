# Andrew Moore
# 10/16
# M5T1_B - Initials

# Write a simple program to write my initials

import turtle
def main ():
    win = turtle.Screen()
    t = turtle.Turtle()
    # display options
    t.pensize(5)  # increase pensize (takes integer)
    t.pencolor("blue") # set pencolor (takes string)
    t.shape("turtle")

    #commands to draw letter "A"
    t.penup()
    t.forward(100)
    t.left(120)
    t.pendown()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.backward(40)
    t.left(120)
    t.forward(60)
    t.penup()

    #commands to draw letter "M"
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.pendown()
    t.left(180)
    t.forward(90)
    t.right(150)
    t.forward(100)
    t.left(125)
    t.forward(100)
    t.right(150)
    t.forward(90)




main()
