from Model.Game import Game
import Controllers.MenuController as Menu_Controller
from Controllers.Controller import Controller
from Subject import Subject
from Window import Window
from Model.Menu import Menu
from Views.GameoverView import GameoverView


class GameController(Controller):
    __input = None

    def __init__(self, game: Game):
        super().__init__(game)

    def update(self, sender: Subject):
        if isinstance(sender, Game):
            sender: Game
            if sender.isGameOver():
                menu = Menu(2)
                menuController = Menu_Controller.MenuController(menu)
                Window.setViewActual(GameoverView(
                    menuController, sender.getPuntaje()))
