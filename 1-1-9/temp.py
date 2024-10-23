import turtle as trtl
global xpos, ypos
import random as rd
# initialize turtle to begin painting
def init():
    global xpos, ypos
    xpos = 480
    ypos = 300
    clouds.speed(0)
def cloud_draw():
    global xpos, ypos
    for cloud in range(3):
        if cloud % 2 == 0:
            ypos -= 20
            xpos -= 50

        else:
            ypos += 20
            xpos -= 50
        clouds.penup()
        clouds.goto(xpos, ypos)
        clouds.pendown()
        clouds.fillcolor('grey')
        clouds.begin_fill()
        clouds.circle(50)
        clouds.end_fill()

        clouds.penup()
        clouds.pendown()
def lightning():
    global xpos, ypos
    ypos = -230
    xpos = -20
    clouds.width(5)
    clouds.penup()
    clouds.goto(xpos, ypos)
    clouds.pendown()
    clouds.color('yellow')
    clouds.setheading(90)
    clouds.left(15)
    clouds.forward(230)
    clouds.right(100)
    clouds.forward(40)
    clouds.left(85)
    clouds.forward(230)

def rain():
    global xpos, ypos
    ypos = rd.randint(-500, 500)
    xpos = rd.randint(-500, 500)
    clouds.penup()
    clouds.goto(xpos, ypos)
    clouds.pendown()
    clouds.color('blue')
    clouds.setheading(110)
    clouds.forward(4)



clouds = trtl.Turtle()
clouds.penup()
init()



#making three clouds
for cloud in range(3):
    xpos -= 150
    ypos = 300
    cloud_draw()



#method for painting the grass
def grass_draw():
    global xpos, ypos
    xpos = -500
    ypos = -400
    clouds.penup()
    clouds.goto(xpos, ypos)
    clouds.pendown()
    clouds.left(90)



#paints the grass
grass_draw()
clouds.color('#038c25')
for total in range(1000):
    clouds.forward(rd.randint(50, 100))
    xpos += 1
    clouds.pendown()
    clouds.goto(xpos, ypos)
    clouds.penup()

#draw lightning
lightning()

#draw raindrops
for number in range(1000):
    rain()

#draw lightning
lightning()


wn = trtl.Screen()
#painting the sky
wn.bgcolor('#B2BEB5')
wn.mainloop()