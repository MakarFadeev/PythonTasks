import turtle
import random

t = turtle.Pen()
t.speed(5)
speed = 5

def up():
    global speed
    x, y = t.pos()
    t.goto(x, y + speed)

def down():
    global speed
    x, y = t.pos()
    t.goto(x, y - speed)

def right():
    global speed
    x, y = t.pos()
    t.goto(x + speed, y)

def left():
    global speed
    x, y = t.pos()
    t.goto(x - speed, y)
        
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(left, 'Left')

turtle.listen()
