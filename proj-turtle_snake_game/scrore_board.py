import snake
from turtle import Turtle, Screen


class Score(snake.Snake):
    def __init__(self):
        self.sc_turtle = Turtle()
        self.sc_turtle.pencolor("white")
        self.sc_turtle.hideturtle()
        self.score = 0
        self.sc_turtle.penup()
        self.sc_turtle.goto(0, 290)
        self.sc_turtle.pendown()
        self.sc_turtle.write(f"Score:{self.score}", False, "center", ("Arial", 20, "bold "))

    def update_score(self):
        self.score += 1
        self.sc_turtle.clear()
        self.sc_turtle.write(f"Score:{self.score}", False, "center", ("Arial", 20, "bold "))

    def game_over(self):
        self.sc_turtle.penup()
        self.sc_turtle.goto(0, 0)
        self.sc_turtle.pendown()
        self.sc_turtle.write("GAME OVER!!!", False, "center",  ("Arial", 30, "bold "))


