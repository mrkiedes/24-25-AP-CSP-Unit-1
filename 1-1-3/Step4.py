#   a113_numeric_comparison.py
#   Predict what the following code will do.
import turtle as trtl

painter = trtl.Turtle()

for line in range(3):
  painter.forward(100)
  painter.right(120)
  painter.forward(200)

wn = trtl.Screen()
wn.mainloop()