from turtle import Turtle


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

    def move_right(self):
        if self.xcor() < 380:
            new_x_cor = self.xcor() + self.speed
            self.goto(new_x_cor, self.ycor())

    def move_left(self):
        if self.xcor() > -380:
            new_x_cor = self.xcor() - self.speed
            self.goto(new_x_cor, self.ycor())