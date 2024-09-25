##############################################################################
#   a114_TR_guess.py
#   Example solution: see comments below
##############################################################################
#   a114_while_guess.py

import turtle as trtl

# changed default colors to navy and salmon
color1 = "Navy"
color2 = "Salmon"

wn = trtl.Screen()
height = 180 # changed from 50 to 180

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 1
angle = 75 # changed from 65 to 75
seg = int(360/angle)

while painter.ycor() < height:
  if (space % 10 == 0): # changed to mod 10
    painter.fillcolor(color1)
    painter.color(color1)
  elif (space % 5 == 0): # changed to space % 5 == 0
    painter.fillcolor(color2)
    painter.color(color2)

  painter.right(angle)
  painter.forward(3*space + 10) # changed 2 to 3
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()
  space += 1

wn.mainloop()