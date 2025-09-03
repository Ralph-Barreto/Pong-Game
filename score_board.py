from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 0)
        self.penup()
        self.color("white")
        self.speed("fastest")

    def point(self, new_score):
        """Draws a new score on the screen"""
        self.clear()
        self.write(new_score, align="center", font=("Courier", 48, "normal"))

class PlayerScoreBoard(ScoreBoard):
    def __init__(self):
        super().__init__()
        self.goto(-200, 200) # sets position

class ComputerScoreBoard(ScoreBoard):
    def __init__(self):
        super().__init__()
        self.goto(200, 200) # sets position