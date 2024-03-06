# Turtle Crossing Game

---

- The goal of this game is to make the turtle cross the road without being hit by a car.
- When that happens you move to the next level where the cars become faster.

![turtle_screenshot_1](https://github.com/Abdelrahman-Elsaudy/Turtle-Crossing-Game/assets/158151388/8c30fcd1-1d26-4ce5-b4be-18ee9e62b699)
![turtle_screenshot_2](https://github.com/Abdelrahman-Elsaudy/Turtle-Crossing-Game/assets/158151388/c267ea42-709e-493c-9598-fdf158e0b52e)
---

## Applied Skills:

---

**1. Object-Oriented Programming**

Dividing the project into:
- `timmy.py` that creates the turtle, positions it and moves it.
- `cars.py` that creates the cars randomly and moves them across the screen.
- `statement.py` which displays the current level and indicates when the game is over.
- `main.py` on which all of the above is called, the screen is set and the game_on loop works.


**2. Game Concept**

- The screen is updated inside a while loop on `main.py`, and each time it's updated a car is created and moves a step from the right 
of the screen to the left, cars creation is done on `cars.py`.
- Cars are created according to a coefficient on `main.py` which can be changed to change the traffic, I found `if coeff % 4 == 0:` suitable.
```
while game_on:
    screen.update()
    time.sleep(speed)
    cars.motion()
    if coeff % 4 == 0:
        cars.creation()
```
- The turtle can move up and down, when it collides with a car the game is over.
```
    for car in cars.cars_list:
        if car.distance(timmy) < 20:
            statement.game_over()
            game_on = False
```
- When the turtle crosses the road, the score increases, the turtle returns to its starting place and 
the speed of the game increases.
```
    if timmy.ycor() >= 280:
        statement.score += 1
        timmy.goto(0, -280)
        speed *= 0.5
```

---


_Credits to: 100-Days of Code Course on Udemy._