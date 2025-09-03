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
        self.score = 0
        # self.refresh()

    def move_up(self):
        """Makes the bat move upward"""
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """Makes the bat move downward"""
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

########################################################################################################################
class Player(Bat):
    """Set up for the Player's bat"""
    def __init__(self):
        super().__init__()
        self.goto(-350, 0)

class Computer(Bat):
    """Set up for the Computer's bat"""
    def __init__(self):
        super().__init__()
        self.goto(350, 0)