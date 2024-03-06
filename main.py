# Use "Up" and "Down" to move the turtle down.

from turtle import Screen
from timmy import Timmy
from cars import Cars
import time
from statement import Statements

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

statement = Statements()
timmy = Timmy()
cars = Cars()

game_on = True
coeff = 0
speed = 0.2

screen.onkeypress(timmy.moving_up, "Up")
screen.onkeypress(timmy.moving_down, "Down")

while game_on:
    screen.update()
    time.sleep(speed)
    statement.current_level()
    cars.motion()
    if coeff % 4 == 0:       # This coefficient is used to control the cars traffic density.
        cars.creation()
    for car in cars.cars_list:
        if car.distance(timmy) < 20:
            statement.game_over()
            game_on = False

    # When the turtle crosses the road, and we move to the next level.
    if timmy.ycor() >= 280:
        statement.score += 1
        timmy.goto(0, -280)
        speed *= 0.5

    coeff += 1

screen.exitonclick()
