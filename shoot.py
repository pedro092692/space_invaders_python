import time
from turtle import Turtle, Screen
import random


class Shoot:

    def __init__(self):
        self.speed = -10

    def create_bullet(self, x, y, position):
        shot = Turtle('square')
        shot.resizemode('user')
        shot.shapesize(0.9, 0.1, 1)
        shot.color('white')
        shot.penup()
        shot.hideturtle()
        shot.setposition(x, y + position)
        return shot


    def move_shot(self, shots: list):
        for shot in shots:
            shot.showturtle()
            new_y_cor = shot.ycor()
            new_y_cor += self.speed
            shot.sety(new_y_cor)



    @staticmethod
    def randon_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color_rgb = (r, g, b)
        return color_rgb