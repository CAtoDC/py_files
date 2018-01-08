'''Using a turtle shape, draws a spiral
that gets larger over time.
'''

import turtle

wn = turtle.Screen()
#wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

# range of 5 to 60 by increments of 2
print(range(5,60,2))

tess.up()                       

for size in range(5,100,2):     
    tess.stamp()
    tess.forward(size)
    tess.right(24)

wn.exitonclick()
