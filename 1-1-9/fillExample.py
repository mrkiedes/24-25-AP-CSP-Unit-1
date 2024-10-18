import turtle as trtl

# Instantiate the turtle
filler = trtl.Turtle()

# Begin filling drawn objects
filler.begin_fill()

# Change first color
filler.fillcolor("blue")

filler.circle(50)

# End filling drawn objects
filler.end_fill()


filler.goto(100, 100)

# Start second fill
filler.begin_fill()

# Change the color of the fill
filler.fillcolor("red")
filler.circle(100)

# End the fill
filler.end_fill()


wn = trtl.Screen()
wn.mainloop()