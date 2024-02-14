# Use "w" to move the turtle up, and "s" to move the turtle down.

from turtle import Screen
from timmy import Timmy
from cars import Cars
import time
from statement import Statements

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

current_level = Statements()
game_over = Statements()
timmy = Timmy()
cars = Cars()

game_on = True
coeff = 0
speed = 0.2
while game_on:
    screen.update()
    time.sleep(speed)
    current_level.levels()
    screen.onkeypress(timmy.moving_up, "w")
    screen.onkeypress(timmy.moving_down, "s")
    cars.motion()
    if coeff % 4 == 0:       # This coefficient is used to control the amount of cars.
        cars.creation()
    for car in cars.cars_list:
        if car.distance(timmy) < 20:
            game_over.end()
            game_on = False
    if timmy.ycor() >= 280:
        current_level.score += 1
        timmy.goto(0, -280)
        speed *= 0.5

    coeff += 1

screen.exitonclick()
