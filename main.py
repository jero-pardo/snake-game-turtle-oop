import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

# Configurations
GAME_BOUNDARY = 290
SNAKE_START_LOC = (0, 0)

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Initialize objects
snake = Snake()
food = Food()
score_board = ScoreBoard()

def restart_btn_click(x, y):
    if (40 > x > -40) and (-60 < y < -30):
        score_board.reset_score()
        start_game()

def start_game():
    snake.kill_snake()
    snake.create_snake(SNAKE_START_LOC)
    food.refresh()

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food.pos()) < 15:
            food.refresh()
            snake.extend()
            score_board.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > GAME_BOUNDARY \
        or snake.head.xcor() < -GAME_BOUNDARY \
        or snake.head.ycor() > GAME_BOUNDARY \
        or snake.head.ycor() < -GAME_BOUNDARY:
            is_game_on = False
            score_board.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                score_board.game_over()


# Event Listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onscreenclick(restart_btn_click, 1)


start_game()
screen.mainloop()