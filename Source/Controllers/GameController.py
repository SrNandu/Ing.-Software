from Observer import Observer
from Model.Game import Game
from Views.GameView import GameView


class GameController(Observer):
    __vista = None
    __game = None
    __input = None

    def __init__(self, input):
        self.__input = input
        self.__game = Game(600, 500)
        self.__vista = GameView(600, 500)
        self.__game.suscribirse(self.__vista)
        self.__game.start()
