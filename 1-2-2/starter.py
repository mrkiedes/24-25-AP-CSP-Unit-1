##############################################################################
#   a121_TR_catch_a_turtle_complete.py
#   Example solution:
#      A game where a turtle appears at random locations on the screen and
#      a player raises their score by clicking the turtles in time.
#      Complete with all the challenges.
##############################################################################
# -----import statements-----
import turtle as trtl
import random as rand

# -----game configuration-----
# To view in trinket change the values of font_size, spot_size, and
# screen_size by half
colors = ["black", "sky blue", "salmon", "orchid", "pale green"]
font_setup = ("Arial", 20, "normal")
spot_size = 2
spot_color = 'pink'
spot_shape = "turtle"
timer = 30
counter_interval = 1000
timer_up = False
score = 0

# -----initialize the turtles-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(160, 160)  # x,y set to fit on smaller screen
score_writer.pendown()
# score_writer.showturtle()

counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-160, 160)  # x,y set to fit on smaller screen
counter.pendown()


# counter.showturtle()

# -----game functions-----

# countdown function
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

    # update and display the score


def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)


# what happens when the spot is clicked
def spot_clicked(x, y):
    global timer_up
    if (not timer_up):
        update_score()
        change_position()
    else:
        spot.hideturtle()


# resize the turtle
def resize():
    sizes = [.5, 1, 1.5, 2]
    spot.shapesize(rand.choice(sizes))


# stamp turtle
def leave_a_mark():
    spot.fillcolor(rand.choice(colors[1:]))
    spot.stamp()
    spot.fillcolor(colors[0])  # comment out for more a more difficult game


# change the position of spot
def change_position():
    leave_a_mark()  # challenge to add color
    resize()  # challenge to change size of turtle
    new_xpos = rand.randint(-150, 150)  # x,y set to fit on smaller screen
    new_ypos = rand.randint(-150, 150)  # x,y set to fit on smaller screen
    spot.penup()  # 2nd step in moving
    spot.hideturtle()  # 3rd step in moving
    spot.goto(new_xpos, new_ypos)  # 1st step in moving
    spot.showturtle()
    spot.pendown()


# starting the game
def start_game():
    spot.onclick(spot_clicked)
    counter.getscreen().ontimer(countdown, counter_interval)


# ----------events----------
start_game()
wn = trtl.Screen()
wn.bgcolor("white smoke")
wn.mainloop()
