from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

pad1 = Paddle(1)
pad2 = Paddle(2)
ball = Ball()

game_is_on = True


screen.listen()
screen.onkey(pad1.moveup, "w")
screen.onkey(pad1.movedown, "s")
screen.onkey(pad2.moveup, "Up")
screen.onkey(pad2.movedown, "Down")

while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()
    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.bounce_y()

    if ball.ball.distance(pad1.pad) < 10 and ball.ball.xcor() > 340:
        ball.bounce_x()

    if ball.ball.distance(pad2.pad) < 10 and ball.ball.xcor() < -340:
        ball.bounce_x()




screen.exitonclick()