from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(500, 400)
race_is_on = False


tim = Turtle()
tim.penup()
tim.goto(-200, 150)
tim.shape("turtle")
tim.color("purple")
tom = Turtle()
tom.penup()
tom.goto(-200, 100)
tom.shape("turtle")
tom.color("indigo")
jom = Turtle()
jom.penup()
jom.goto(-200, 50)
jom.shape("turtle")
jom.color("blue")
hom = Turtle()
hom.penup()
hom.goto(-200, 0)
hom.shape("turtle")
hom.color("green")
pom = Turtle()
pom.penup()
pom.goto(-200, -50)
pom.shape("turtle")
pom.color("yellow")
gom = Turtle()
gom.penup()
gom.goto(-200, -100)
gom.shape("turtle")
gom.color("orange")
mom = Turtle()
mom.penup()
mom.goto(-200, -150)
mom.shape("turtle")
mom.color("red")

guess = screen.textinput("Make a bet!!!", "Which color will you think will win??(VIBGYOR)")
if guess:
    race_is_on = True

turtles = [ tim,tom,jom,hom,pom,gom,mom]

while race_is_on:
    for t in turtles:
        t.forward(random.randint(0,10))
        if t.xcor() > 230:
            won = t.pencolor()
            print(f"{won} has won")
            race_is_on = False


if guess == won:
    print("You won $10 , congrats")
else:
    print("Yor turtle lost ")
screen.exitonclick()

