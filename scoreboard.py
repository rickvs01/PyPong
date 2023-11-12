from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-500, 340)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(500, 340)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    # def increase_score(self):
    #     self.clear()
    #     self.score += 1
    #     self.color("white")
    #     self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
