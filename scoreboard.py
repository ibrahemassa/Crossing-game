from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.current_level = 1
        self.setpos(-244,266)
        self.write(f"Level: {self.current_level}", align="center", font = ("Arial", 22, "normal"))
        self.ht()
    
    def next_level(self):
        self.current_level += 1
        self.clear()
        self.write(f"Level: {self.current_level}", align="center", font = ("Arial", 22, "normal"))
    
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAMEOVER", align="center", font=('Arial', 40, 'normal'))
