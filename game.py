import random
from turtle import Screen, Turtle
from aliens import Alien
from scoreboard import ScoreBoard
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
        self.scoreboard = ScoreBoard()

        # move cannon
        self.screen.listen()
        self.screen.onkeypress(key='Right', fun=self.cannon.move_right)
        self.screen.onkeypress(key='Left', fun=self.cannon.move_left)
        self.screen.onkeypress(key='space', fun=self.cannon.shot_bullet)

    def play_game(self):

        while True:
            time.sleep(0.1)
            self.screen.update()
            # move aliens
            self.aliens.move_aliens()
            # move bullets of cannon
            self.cannon.shot.move_shot(self.cannon.shots)
            # destroy aliens
            if self.cannon.shots:
                self.aliens.destroy_alien(self.cannon.shots, self.cannon, self.scoreboard)