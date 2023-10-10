import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("silver")
screen.title("Turtle Crossing Street by @Emilio_Morles")
screen.tracer(0)

car_manager = CarManager()
player_score = ScoreBoard()
player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_left()

    for car in car_manager.all_cars:  # It detects when the turtle player collides with a car and
        # stop the game if this happens.
        if player.distance(car) < 25:
            game_is_on = False
            player_score.game_over()  # When the turtle hits a car, GAME OVER should be displayed in the centre.

    if player.ycor() > 280:  # When the turtle hits the top edge of the screen, it moves back to the
        # original position and the player levels up. On the next level, the car speed increases.
        player.reset_position()
        player_score.player_point()
        car_manager.level_up()  # The cars are faster every time the turtle reset starting position.
        # player.score_increase()

screen.exitonclick()
