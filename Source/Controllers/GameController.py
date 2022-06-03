from Model.Game import Game
from Controllers.Controller import Controller
import Views.GameView as GameView


class GameController(Controller):

    def __init__(self, vista: GameView, game: Game, input):
        super().__init__(vista, game)

        self.__input = input
        
        game.start()
