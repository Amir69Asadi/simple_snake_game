# import
import turtle
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
head.color('red')
head.penup()
head.goto(0,0)
head.direction='stop'


# main game loop
while True:
    win.update()
win.mainloop()