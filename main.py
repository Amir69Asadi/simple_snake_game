# import
import turtle
import time
import random as rnd

deley = 0.15

# set up the screen
win = turtle.Screen()
win.title('amir snake')
win.bgcolor('black')
win.setup(width=600, height=600)
win.tracer(0)
# snake head
head = turtle.Turtle()
head.speed()
head.shape('circle')
head.color('green')
head.penup()
head.goto(0, 0)
head.direction = 'stop'
# snake food
food = turtle.Turtle()
food.speed()
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 110)

segments = []


# functions
def go_up():
    head.direction = 'up'


def go_down():
    head.direction = 'down'


def go_right():
    head.direction = 'right'


def go_left():
    head.direction = 'left'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

    # Keyboard bindings


win.listen()
win.onkeypress(go_down, 's')
win.onkeypress(go_up, 'w')
win.onkeypress(go_left, 'a')
win.onkeypress(go_right, 'd')

# main game loop
while True:
    win.update()
    # check for a collision with the food
    if head.distance(food) < 20:
        # move food to a random spot
        x = rnd.randint(-290, 290)
        y = rnd.randint(-290, 290)
        food.goto(x, y)
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)
        food.goto(x, y)
    # move the end segment first in reverse order
    for indes in range(len(segments) - 1, 0, -1):
        x = segments[indes - 1].xcor()
        y = segments[indes - 1].ycor()
        segments[indes].goto(x, y)
    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    time.sleep(deley)

win.mainloop()
