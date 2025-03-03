from turtle import Turtle

class Bat(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.goto(0,0)
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.speed("fastest")
        # self.refresh()

class Player(Bat):

    def __init__(self):
        super().__init__()
        self.goto(-500, 0)

class Computer(Bat):
    def __init__(self):
        super().__init__()
        self.goto(500, 0)