from Model.Game import Game
from Controllers.Controller import Controller
from Subject import Subject
from Window import Window
from Views.GameoverView import GameoverView

class GameController(Controller):
    __input = None

    def __init__(self, game: Game):
        super().__init__( game)

    def update(self, sender: Subject):
        if isinstance(sender, Game):
            sender: Game
            if sender.isGameOver():
                Window.setViewActual(GameoverView(Controller(Subject())))

