from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed= STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            car = Turtle()
            car.shape('square')
            car.penup()
            random_Y = random.randint(-260, 280)
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.goto(300, random_Y)
            car.setheading(180)
            self.all_cars.append(car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def car_fast(self):
        self.car_speed=self.car_speed +MOVE_INCREMENT
