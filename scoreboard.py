from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level=1
        self.goto(-220,250)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        self.clear()
        self.level= self.level + 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def Lose(self):
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 24, "normal"))





