from Model.Game import Game
from Controllers.MenuController import MenuController
from Views.MenuView import MenuView
from Views.GameView import GameView
from Controllers.GameController import GameController
from Controllers.Controller import Controller
from Model.Menu import Menu
from Window import Window


class GameoverController(Controller):
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
        
    def __volverMenu(self):
        menu = Menu(3)
        menuController = MenuController(menu)
        menuView = MenuView(menuController)

        menu.suscribirse(menuView)

        Window.setViewActual(menuView)