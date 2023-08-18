from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 7
MOVE_INCREMENT = 6


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.setpos(250, random.randint(-240,250))

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.setpos(new_x, self.ycor())
    
    def generate_cars(self):
        for i in range(50):
            pass
