from Model.Game import Game
from Controllers.Controller import Controller
import Views.GameView as GameView


class GameController(Controller):
    __input = None

    def __init__(self, game: Game, input):
        super().__init__( game)

        self.__input = input

        # Iniciar game loop en nuevo hilo para no parar el progrma
        game.start()
