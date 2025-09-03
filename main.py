from turtle import Screen
from bat import Player, Computer
from ball import Ball
from score_board import PlayerScoreBoard, ComputerScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player = Player()
computer = Computer()
ball = Ball()
player_score_board = PlayerScoreBoard()
computer_score_board = ComputerScoreBoard()

def bounce():
    if ball.distance(computer) < 60 and 335 < ball.xcor() < 340:
        ball.x_direction = "left"
    if ball.distance(player) < 60 and -335 > ball.xcor() > -340:
        ball.x_direction = "right"

def score_point():
    if ball.xcor() > 400:
        player.score += 1
        player_score_board.point(player.score)
        ball.reset()
    if ball.xcor() < -400:
        computer.score += 1
        computer_score_board.point(computer.score)
        ball.reset()

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")

screen.onkey(computer.move_up, "Up")
screen.onkey(computer.move_down, "Down")

screen.tracer(0)

game_is_on = True
while game_is_on:
    screen.update()
    bounce()
    score_point()
    ball.move()
    ball.bounce()

    time.sleep(0.01)

screen.exitonclick()
