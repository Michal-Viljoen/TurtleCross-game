import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
score=Scoreboard()
screen.listen()
car_manager=CarManager()
screen.onkeypress( player.move, 'w')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            score.Lose()

    if player.ycor()>290:
        player.resets()
        car_manager.car_fast()
        score.update_score()





screen.exitonclick()