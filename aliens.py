import random
from turtle import Turtle
from shoot import Shoot

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

        # move direction
        self.direction = (20, 0)

        # shoot
        self.shots = []
        self.shot  = Shoot()

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
        for alien in self.aliens:
            alien.setpos(alien.pos() + self.direction)
            if self.aliens[::-1][0].xcor() >= 340:
                self.direction = (-20, 0)
            if self.aliens[::-1][0].xcor() <= 72:
                self.direction = (20, 0)

        # .9% probability of alien shots
        if random.random() < 0.4:
            self.shoot()
        self.shot.move_shot(self.shots)


    def shoot(self):
        if self.aliens:
            alien = random.choice(self.aliens[-10:])
            shot = self.shot.create_bullet(alien.xcor(), alien.ycor(), position=-10, color='white')
            self.shots.append(shot)

    def destroy_alien(self, shots, cannon, board):
        if self.aliens:
            for alien in self.aliens:
                for shot in shots:
                    if alien.distance(shot) < 20:
                        # destroy alien
                        try:
                            self.aliens.remove(alien)
                            self.del_turtle(alien)
                        except ValueError as e:
                            pass
                        # destroy bullet
                        cannon.destroy_bullet(shot)
                        # add score
                        board.add_score()


    @staticmethod
    def del_turtle(turtle):
        turtle.reset()
        turtle.hideturtle()
        turtle.clear()



