import turtle
import random

colors = ['red', 'green', 'blue', 'yellow', 'brown', 'purple', 'pink', 'orange']

def turcircle(x, y):
    color = colors[random.randint(0, len(colors) - 1)]
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(random.randint(10, 100))
    t.end_fill()
    
t = turtle.Pen()
t.speed(5)
turtle.onscreenclick(turcircle)
