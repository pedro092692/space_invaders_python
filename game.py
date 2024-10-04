from turtle import Screen, Turtle
from aliens import Alien
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

    def play_game(self):

        while True:
            self.screen.update()
            self.aliens.move_aliens()

            time.sleep(0.3)