import time
from turtle import Turtle
from shoot import Shoot


class Cannon(Turtle):
    def __init__(self):
        super().__init__()
        # initial setup
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        self.speed = 20
        self.shot = Shoot()
        self.shot.speed *= -1
        self.shots = []


    def move_right(self):
        if self.xcor() < 380:
            new_x_cor = self.xcor() + self.speed
            self.goto(new_x_cor, self.ycor())

    def move_left(self):
        if self.xcor() > -380:
            new_x_cor = self.xcor() - self.speed
            self.goto(new_x_cor, self.ycor())

    def shot_bullet(self):
        shot = self.shot.create_bullet(x=self.xcor(), y=self.ycor(), position=10, color='blue')
        self.shots.append(shot)

    def destroy_bullet(self, bullet):
        self.shots.remove(bullet)
        bullet.clear()
        bullet.reset()
        bullet.hideturtle()

    def hit_cannon(self, bullets, board):
        for bullet in bullets:
            if self.distance(bullet) < 25:
                self.goto(0, -280)
                board.subtract_lives()
                time.sleep(0.5)