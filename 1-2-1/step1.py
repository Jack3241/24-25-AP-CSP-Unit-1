
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------
def change_position():
    xpos = rand.randint(1, 400)
    ypos = rand.randint(1, 300)
    spot.goto(xpos, ypos)
def update_score():
    global score
    score += 1
    print(score)
def spot_click(x, y):
    spot.penup()
    change_position()
    update_score()

#-----events----------------
spot.onclick(spot_click)
wn = trtl.Screen()
wn.mainloop()
