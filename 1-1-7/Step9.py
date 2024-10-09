################################################################################
#   a117_TR_traversing_turtles_1.py
#   Example solution:
#      Turtles are manipulated using a variety of lists and
#      are drawn in an outward growing octagon.
################################################################################
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# initialize myturtles list, turtles with different shapes and colors
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  t.penup()
  my_turtles.append(t)

# draw all turtles in a circular shape
start_x = 0
start_y = 0
direction = 90
for t in my_turtles:
  t.goto(start_x, start_y)
  t.setheading(direction)
  t.pendown()
  t.right(45)
  t.forward(50)
  direction = t.heading()
  start_x = t.xcor()
  start_y = t.ycor()

wn = trtl.Screen()
wn.mainloop()