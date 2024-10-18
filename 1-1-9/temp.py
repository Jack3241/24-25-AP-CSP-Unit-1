import turtle as trtl

# move pen to start making clouds
clouds = trtl.Turtle()
clouds.penup()
xpos = 150
ypos = 300


# making and coloring clouds
for cloud in range(10):
    clouds.goto(xpos, ypos)
    clouds.fillcolor('grey')
    clouds.begin_fill()
    clouds.circle(50)
    clouds.end_fill()
    # move pen to make next cloud
    clouds.penup()

    clouds.pendown()
wn = trtl.Screen()
wn.mainloop()
