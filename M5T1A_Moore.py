# CTI-110
# M5T1A - Turtle Lab
# Andrew Moore
# 10/11
# M5T1_A - Shapes
# Write a simple program to draw a square and triangle

import turtle
def main():
    
    win = turtle.Screen()
    t = turtle.Turtle()
    # add some display options
    t.pensize(8)    # increase pensize (takes integer)
    t.pencolor("green")  # set pencolor (takes string)
    t.shape("turtle")

    #commands to draw square
    t.forward(75)      #tell turtle to move forward by 75 units
    t.left(90)      #tell turtle to turn by 90 degrees
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)

    t.penup()
    t.forward(50)

    #commands to draw triangle
    t.pendown()
    t.forward(75)
    t.left(120)
    t.forward(75)
    t.left(120)
    t.forward(75)
    


main()
    
