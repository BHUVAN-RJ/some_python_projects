from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle("circle")
        # self.ball.shapesize(1, 1)
        self.ball.penup()
        self.ball.color("white")
        self.new_y = 10
        self.new_x = 10
    def move(self):
        self.ball.setx(self.ball.xcor() + self.new_x)
        self.ball.sety(self.ball.ycor() + self.new_y)

    def bounce_y(self):
        self.new_y *= -1

    def bounce_x(self):
        self.new_x *= -1


