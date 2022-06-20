from Model.Game import Game
from Controllers.GameoverController import GameoverController
from Controllers.Controller import Controller
from Model.InputStrategy import InputStrategy
from Subject import Subject
from Window import Window
from Model.Menu import Menu
from Views.GameoverView import GameoverView


class GameController(Controller):
    __input = None

    def __init__(self, game: Game):
        super().__init__(game)

    def update(self, sender: Subject):
        if isinstance(sender,InputStrategy):
            sender: InputStrategy
            self._model.moverPajaro(sender.getPos())
        if isinstance(sender, Game):
            sender: Game
            if sender.isGameOver():
                self._model.desuscribirTodos()

                menu = Menu(2)
                menuController = GameoverController(menu)
                Window.setViewActual(GameoverView(
                    menuController, sender.getPuntaje()))
