from turtle import Turtle, Screen
import random

colors = ["red", "blue", "green", "yellow", "purple", "maroon", "aqua", "pink", "black", "gold", "silver"]

turtle = Turtle()


screen = Screen()
screen.colormode(255)
turtle.speed(1000)

def color():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    tup = (c1, c2, c3)
    return tup

def spot(col):
    turtle.begin_fill()
    turtle.fillcolor(col)
    turtle.circle(5)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


num = 0
x = turtle.xcor()

while True:
    if num % 10 == 0:

        y = turtle.ycor()
        turtle.penup()
        turtle.setposition(x, y - 50)
        turtle.pendown()
    num += 1
    spot(color())






screen.exitonclick()