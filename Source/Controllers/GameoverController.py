from Model.Game import Game
import Controllers.MenuController as menu_Controller
from Model.InputStrategy import InputStrategy
from Views.MenuView import MenuView
from Views.GameView import GameView
import Controllers.GameController as game_Controller
from Controllers.Controller import Controller
from Model.Menu import Menu
from Window import Window


class GameoverController(Controller):
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
            self.__volverMenu()

    def __startGame(self):
        self._model.desuscribirTodos()

        game = Game()
        gameView = GameView(game_Controller.GameController(game))
        Window.setViewActual(gameView)

        game.suscribirse(gameView)
        game.start()
        
    def __volverMenu(self):
        self._model.desuscribirTodos()
        
        menu = Menu(4)
        menuController = menu_Controller.MenuController(menu)
        menuView = MenuView(menuController)

        menu.suscribirse(menuView)

        Window.setViewActual(menuView)