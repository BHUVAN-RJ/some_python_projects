from turtle import Turtle,Screen
import time
import snake
import food
import scrore_board
screen = Screen()
screen.setup(600, 640)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)


game_is_on = True
main_snake = snake.Snake()
food_turt = food.Food()
score = scrore_board.Score()
screen.listen()
screen.onkey(main_snake.up, "Up")
screen.onkey(main_snake.down, "Down")
screen.onkey(main_snake.left, "Left")
screen.onkey(main_snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    main_snake.move()
    if main_snake.segments[0].distance(food_turt.food_t) < 15:
        food_turt.new_food()
        score.update_score()
        main_snake.extend()

    if main_snake.segments[0].xcor() > 290 or main_snake.segments[0].xcor() < -290 or main_snake.segments[0].ycor() > 300 or main_snake.segments[0].ycor() < -310:
        game_is_on = False
        score.game_over()
    for segment in main_snake.segments[1:]:
        if main_snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()




screen.exitonclick()