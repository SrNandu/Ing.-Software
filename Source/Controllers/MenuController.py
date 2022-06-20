from Model.Game import Game
from Model.InputStrategy import InputStrategy
from Views.GameView import GameView
from Controllers.GameController import GameController
from Controllers.Controller import Controller
from Model.Menu import Menu
from Window import Window


class MenuController(Controller):
    __input = None

    def __init__(self, menu: Menu):
        super().__init__(menu)

    def update(self, sender):
        if isinstance(sender, InputStrategy):
            sender: InputStrategy
            gesto = sender.getGesto()
            if gesto == "Boca":
                self._model.botonSig()
            elif gesto == "BocaLargo":
                self.__enter()

    def __enter(self):
        boton = self._model.getBoton()

        if boton == 0:
            self.__startGame()
        else:
            pass

    def __startGame(self):
        game = Game()
        gameView = GameView(GameController(game))
        Window.setViewActual(gameView)

        game.suscribirse(gameView)
        game.start()
        pass
