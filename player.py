from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 13
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.shapesize(1.5, 1.5)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setpos(self.xcor(), new_y)
    
    def finish_level(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
    
