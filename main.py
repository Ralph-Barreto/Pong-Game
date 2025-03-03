from turtle import Screen
from bat import Player, Computer
import time


player = Player()
computer = Computer()

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.exitonclick()