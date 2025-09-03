from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.goto(0, 0)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.x_direction = "right"
        self.y_direction = "down"

    def move(self):
        if self.x_direction == "right":
            new_x = self.xcor() + 2
            self.goto(new_x, self.ycor())
        elif self.x_direction == "left":
            new_x = self.xcor() - 2
            self.goto(new_x, self.ycor())

        if self.y_direction == "down":
            new_y = self.ycor() - 2
            self.goto(self.xcor(), new_y)
        elif self.y_direction == "up":
            new_y = self.ycor() + 2
            self.goto(self.xcor(), new_y)

    def bounce(self):
        if self.ycor() > 250:
            self.y_direction = "down"
        if self.ycor() < -250:
            self.y_direction = "up"

    def reset(self):
        self.goto(0, 0)
        time.sleep(0.2)
