from snake import Snake
from turtle import Turtle
import random


class Food(Snake):
    def __init__(self):
        self.food_t = Turtle("circle")
        self.food_t.color("red")
        self.food_t.penup()
        self.food_t.shapesize(0.5, 0.5)
        self.food_t.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.new_food()

    def new_food(self):
        self.food_t.goto(random.randint(-280, 280), random.randint(-280, 280))