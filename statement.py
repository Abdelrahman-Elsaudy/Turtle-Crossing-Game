from turtle import Turtle


class Statements(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1

    def levels(self):
        self.goto(-280,260)
        self.clear()
        self.write(f"Level: {self.score}", False, align= "left", font=('Arial', 16, 'normal'))

    def end(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align= "center", font=('Arial', 12, 'bold'))
