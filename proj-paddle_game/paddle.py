from turtle import Turtle


class Paddle:
    def __init__(self, num ):
        self.pad = Turtle("square")
        self.pad.color("white")
        self.pad.shapesize(stretch_wid=1, stretch_len=5)
        self.pad.penup()
        self.pad.setheading(90)
        if num == 1:
            self.pad.setposition(-380, 0)
        else:
            self.pad.setposition(380, 0)

    def moveup(self):
        self.pad.forward(30)



    def movedown(self):
        self.pad.backward(30)



