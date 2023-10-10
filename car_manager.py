from turtle import Turtle
import random

COLORS = ["red", "dark orange", "yellow", "lime", "blue", "black", "white"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):  # Cars are randomly generated along the y-axis.
        random_change = random.randint(1, 6)  # Random chance to create a car.
        if random_change == 1:  # If the number is 1 then create a new car.
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color("black")
            new_car.fillcolor(random.choice(COLORS))
            random_y = random.randint(-240, 240)
            new_car.goto(x=300 - STARTING_MOVE_DISTANCE, y=random_y)
            self.all_cars.append(new_car)

    def move_left(self):  # Cars move from the right edge of the screen to the left edge.
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):  # The cars are faster
        self.car_speed += MOVE_INCREMENT
