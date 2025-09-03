from turtle import Screen
from bat import Player, Computer
from ball import Ball
from score_board import PlayerScoreBoard, ComputerScoreBoard
import time

### Creating Screen ###
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

### Setting up Objects in the game ###
player = Player()
computer = Computer()
ball = Ball()
player_score_board = PlayerScoreBoard()
computer_score_board = ComputerScoreBoard()

### Ball interaction code ###

def bounce():
    """If the ball goes too low or two high it will hit virtual wall and bounce"""
    if ball.distance(computer) < 60 and 335 < ball.xcor() < 340:
        ball.x_direction = "left"
    if ball.distance(player) < 60 and -335 > ball.xcor() > -340:
        ball.x_direction = "right"

def score_point():
    """If the ball goes beyond either paddle it will cause the appropriate player to gain a point and this
    will be displayed on the screen"""
    if ball.xcor() > 400:
        player.score += 1
        player_score_board.point(player.score)
        ball.reset()
    if ball.xcor() < -400:
        computer.score += 1
        computer_score_board.point(computer.score)
        ball.reset()

### keyboard controls ###
screen.listen()
# for player:
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
# for computer:
screen.onkey(computer.move_up, "Up")
screen.onkey(computer.move_down, "Down")

screen.tracer(0)

### Game loop ###
game_is_on = True
while game_is_on:
    screen.update()
    bounce()
    score_point()
    ball.move()
    ball.bounce()

    time.sleep(0.01)

screen.exitonclick()
