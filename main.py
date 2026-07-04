from turtle import Screen
from snake import Snake
from food import Food
from scroreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# user_input=screen.textinput(title="Challenge yourself", prompt="Enter the score you expect to reach: ")
# expected_score=int(user_input)

snake = Snake()
food = Food()
score_board = Scoreboard()


screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09) # control the update time

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score_board.increase()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        snake.reset_snake()
        score_board.reset_scoreboard()

    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            snake.reset_snake()
            score_board.reset_scoreboard()




screen.exitonclick()