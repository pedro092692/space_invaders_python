import random
from turtle import Screen, Turtle
from aliens import Alien
from shoot import Shoot
from cannon import Cannon
import time

class Game:
    def __init__(self, title: str, size: tuple, bg: str):
        self.screen = Screen()
        self.screen.setup(width=size[0], height=size[1])
        self.screen.title(title.upper())
        self.screen.colormode(255)
        self.screen.bgcolor(bg)
        self.screen.tracer(0)
        self.aliens = Alien()
        self.cannon = Cannon()

        # move cannon
        self.screen.listen()
        self.screen.onkeypress(key='Right', fun=self.cannon.move_right)
        self.screen.onkeypress(key='Left', fun=self.cannon.move_left)

    def play_game(self):

        while True:

            time.sleep(0.1)
            self.screen.update()
            self.aliens.move_aliens()