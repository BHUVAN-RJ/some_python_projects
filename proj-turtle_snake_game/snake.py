from turtle import  Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in self.positions:
            self.add_segment(pos)

    def add_segment(self, position):
        tut = Turtle("square")
        tut.penup()
        tut.color("white")
        tut.goto(position)
        self.segments.append(tut)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
            segs = len(self.segments)
            segs = segs - 1
            while segs > 0:
                self.segments[segs].goto(self.segments[segs - 1].xcor(), self.segments[segs - 1].ycor())
                segs -= 1
            self.segments[0].forward(20)

    def left(self):
        if self.segments[0].heading() == 90:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].right(90)

    def right(self):
        if self.segments[0].heading() == 90:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].left(90)

    def up(self):
        if self.segments[0].heading() == 0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].right(90)

    def down(self):
        if self.segments[0].heading() == 0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].left(90)

