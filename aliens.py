import time
from turtle import Turtle


class Alien(Turtle):

    def __init__(self):
        super().__init__()
        # register alien shape
        self.alien_name = 'assets/alien.gif'
        self.screen.register_shape(self.alien_name)

        # aliens list
        self.aliens = []

        # initial coordinates
        self.initial_x_post = -240
        self.initial_y_post = 250

        # create aliens
        self.create_aliens()

        self.move = 20

    def create_aliens(self):
        for alien in range(1, 41):
            new_alien = self.alien()
            self.aliens.append(new_alien)
            if alien % 10 == 0:
                self.initial_x_post = -240
                self.initial_y_post -= 48
            else:
                self.initial_x_post += 48

    def alien(self):
        alien = Turtle()
        alien.shape(self.alien_name)
        alien.penup()
        alien.goto(self.initial_x_post, self.initial_y_post)
        return alien

    def move_aliens(self):

        for alien in range(1, len(self.aliens) + 1):
            new_x_cor = self.aliens[alien - 1].xcor() + self.move
            self.aliens[alien - 1].goto(new_x_cor, self.aliens[alien - 1].ycor())
            self.change_direction(self.aliens[alien - 1])

    def change_direction(self, alien: Turtle):
        if alien.xcor() >= 360 or alien.xcor() <= -360:
            self.move *= - 1