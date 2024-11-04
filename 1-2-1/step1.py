
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
font_setup = ("Arial", 20, "normal")
#-----initialize turtle-----
spot = trtl.Turtle()
score_writer = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
counter =  trtl.Turtle()
#-----game functions--------
score_writer.penup()
score_writer.goto(-200, 200)
score_writer.hideturtle()
counter.penup()
counter.goto(-200, 130)
counter.hideturtle()
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
def change_position():
    xpos = rand.randint(1, 400)
    ypos = rand.randint(1, 300)
    spot.goto(xpos, ypos)
def update_score():
    global score
    score += 1
    score_writer.write(score, font=font_setup)
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def spot_click(x, y):
    spot.penup()
    countdown()
    change_position()
    update_score()


#-----events----------------
spot.onclick(spot_click)
wn = trtl.Screen()
wn.mainloop()
