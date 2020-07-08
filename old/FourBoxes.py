'''Use turtle to demonstrate
for loops and screen drawing

Use with python 2x
'''

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    # draw 5 boxes
    for i in range(5):
        # draw all 4 sides of a box
        for i in range(4):
            t.forward(sz)
            t.left(90)
        # positioning to keep the boxes separate
        t.forward(sz)
        t.penup()
        t.forward(sz)
        t.pendown()
wn = turtle.Screen()
wn.exitonclick()
wn.bgcolor("lightgreen")
