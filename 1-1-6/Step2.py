#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
x.pensize(40)
x.circle(20)

# w is number of legs
number_of_legs = 6

# y leg length
y = 70

# z is the angle
z = 380 / number_of_legs
x.pensize(5)

#Draw the legs
n = 0
while (n < number_of_legs):
  x.goto(0,0)
  x.setheading(z*n)
  x.forward(y)
  n = n + 1
x.hideturtle()
wn = trtl.Screen()
wn.mainloop()