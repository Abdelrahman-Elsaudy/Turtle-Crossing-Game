from turtle import Turtle
import random

CARS_COLORS = ["red", "blue", "green", "yellow", "purple", "black", "orange"]


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.hideturtle()

    def creation(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(CARS_COLORS))
        car.goto(300, random.randint(-250,280))
        self.cars_list.append(car)

    def motion(self):
        for x in self.cars_list:
            x.backward(5)
