FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-220, 260)
        self.write(f"Level: {self.score + 1}", align="center", font=FONT)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.score + 1}", align="center", font=FONT)

    def point(self):
        self.score += 1

        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font= ("Courier", 75, "normal"))