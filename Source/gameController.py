from game import game
from vista import vista
from subject import subject


class gameController(subject):
    __vista = None
    __game = None
    __input = None

    def __init__(self, input):
        self.__input = input
        self.__game = game(600, 500)
        self.__vista = vista(600, 500, self.__game)
        self.__game.start()
