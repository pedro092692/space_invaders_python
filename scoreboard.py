from turtle import Turtle
FONT = ('helvetica', 16, 'normal')
ALIGNMENT = 'center'
STARTING_POSITION = (-360, 270)
SCORE_POSITION = (90, 270)
MAX_SCORE_POSITION = (-200, 270)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(STARTING_POSITION)
        self.lives = 4
        self.score = 0

        # start
        self.subtract_lives()
        self.score_label = CreateLabel(color='white', position=SCORE_POSITION, text='score 0')
        self.max_s = int(self.get_max_score())
        self.max_score = CreateLabel(color='white', position=MAX_SCORE_POSITION, text=f'max score: {self.max_s}')

    def subtract_lives(self):
        self.lives -= 1
        self.write(f'Lives: {self.lives}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score_label.clear()
        self.score += 2
        self.score_label.write(f'score: {self.score}', align=ALIGNMENT, font=FONT)

    @staticmethod
    def get_max_score():
        with open('max_score.txt', mode='r') as max_score:
            score = max_score.readline()
        return score

class CreateLabel(Turtle):
    def __init__(self, color, position, text):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(color)
        self.goto(position)
        self.write(text, align=ALIGNMENT, font=FONT)