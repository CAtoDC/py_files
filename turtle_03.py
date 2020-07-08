import turtle

# instantiate turtle
t = turtle.Turtle()

# use the turtle shape
t.shape("classic")

# start position
t_position = t.pos()
print (t_position)

# make the turtle blue
t.color("blue")

# get a screen
screen = t.getscreen()

# draw a 5-pointed star
for i in range(5):
    t.forward(200)
    t.left(144)

# end position
print (t_position)


screen.exitonclick()
