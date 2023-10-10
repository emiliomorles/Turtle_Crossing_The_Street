from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1

        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-200, 240)
        self.color("black")
        self.write(arg=f"Level {self.level}", align="center", font=FONT)

    def player_point(self):  # It keeps track of which level the user is on.
        # Every time the turtle player does a successful crossing, the level should increase
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
