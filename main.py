# import
import turtle
import time

deley=0.1


# set up the screen
win=turtle.Screen()
win.title('amir snake')
win.bgcolor('black')
win.setup(width=600,height=600)
win.tracer(0)
#snake head
head=turtle.Turtle()
head.speed()
head.shape('circle')
head.color('red')
head.penup()
head.goto(0,0)
head.direction='left'

#functions
def go_up():
    head.direction='up'
def go_down():
    head.direction='down'
def go_right():
    head.direction='right'
def go_left():
    head.direction='left'        



def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)      
                      
# main game loop
while True:
    win.update()
    time.sleep(deley)
    move()
win.mainloop()