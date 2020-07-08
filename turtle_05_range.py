import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.color("blue")
t.shape("turtle")
t.penup()

for size in range(10): 
    t.forward(50)
    t.stamp()
    t.forward(-50)
    t.right(36) 

wn.exitonclick()
