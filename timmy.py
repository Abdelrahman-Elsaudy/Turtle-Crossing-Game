from turtle import Turtle


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(0, -280)
        self.turtle_step = 10

    def moving_up(self):
        self.goto(0, self.ycor()+self.turtle_step)

    def moving_down(self):
        self.goto(0, self.ycor()-self.turtle_step)
