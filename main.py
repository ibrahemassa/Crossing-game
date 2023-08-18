import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import car_manager
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")

# car = CarManager()
cars = []

score = Scoreboard()


game_is_on = True
while game_is_on:
    num = random.randint(1,3)
    if num == 1:
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move()
        if player.distance(car) < 20:
            score.gameover()
            game_is_on = False
    time.sleep(0.1)
    if player.finish_level():
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
        score.next_level()

    screen.update()

screen.exitonclick()