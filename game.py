from turtle import Screen


class Game:
    def __init__(self, title: str, size: tuple, bg: str):
        self.screen = Screen()
        self.screen.setup(width=size[0], height=size[1])
        self.screen.title(title.upper())
        self.screen.colormode(255)
        self.screen.bgcolor(bg)

