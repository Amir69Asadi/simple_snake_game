# import
import turtle
import time
import random as rnd

deley=0.15


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
head.color('green')
head.penup()
head.goto(0,0)
head.direction='stop'
# snake food
food=turtle.Turtle()
food.speed()
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,110)

 
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
               
#Keyboard bindings
win.listen()
win.onkeypress(go_down,'s')               
win.onkeypress(go_up,'w')               
win.onkeypress(go_left,'a')               
win.onkeypress(go_right,'d')               
                      
# main game loop
while True:
    win.update()
    if head.distance(food)<20:
        # move food to a random spot
        x=rnd.randint(-290,290)
        y=rnd.randint(-290,290)
        food.goto(x,y)
    move()  
    time.sleep(deley)

win.mainloop()