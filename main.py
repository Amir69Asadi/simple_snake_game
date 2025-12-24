# import
import turtle
import time

deley=0.1


# set up the screen
win=turtle.Screen()
win.title('amir snake')
win.bgcolor('green')
win.setup(width=600,height=600)
win.tracer(0)
#snake head
head=turtle.Turtle()
head.speed()
head.shape('circle')
head.color('gray')
head.penup()
head.goto(0,0)
head.direction='up'

#functions
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
# main game loop
while True:
    win.update()
    time.sleep(deley)
    move()
win.mainloop()