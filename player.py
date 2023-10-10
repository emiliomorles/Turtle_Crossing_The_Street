from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.fillcolor("forest green")
        self.reset_position()
        self.setheading(90)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move_up(self):  # A turtle moves forwards when you press the "Up" key.
        # It can only move forwards, not back, left or right.
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
