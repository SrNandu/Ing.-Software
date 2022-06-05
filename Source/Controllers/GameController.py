from Model.Game import Game
from Controllers.Controller import Controller
import Views.GameView as GameView
from threading import Thread


class GameController(Controller):

    def __init__(self, vista: GameView, game: Game, input):
        super().__init__(vista, game)

        self.__input = input

        # Iniciar game loop en nuevo hilo para no parar el progrma
        gameThread = Thread(target=game.start)
        gameThread.start()
