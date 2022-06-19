from ast import Sub
from Model.Game import Game
from Views.GameView import GameView
from Controllers.GameController import GameController
from Controllers.Controller import Controller
from Model.Menu import Menu
from Subject import Subject
from Window import Window


class MenuController(Controller):
    __input = None

    def __init__(self, menu: Menu):
        super().__init__(menu)

    def update(self, sender):
        return super().update(sender)

    def __startGame(self):
        game = Game()
        gameView = GameView(GameController(game))
        Window.setViewActual(gameView)

        game.suscribirse(gameView)
        game.start()
        pass
