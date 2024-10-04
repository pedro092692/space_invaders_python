from game import Game
from aliens import Alien

game = Game(title='Ultimate Space Invaders', size=(800, 600), bg='black')
game.play_game()


game.screen.exitonclick()