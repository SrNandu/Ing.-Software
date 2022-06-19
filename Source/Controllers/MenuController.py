from ast import Sub
from Model.Game import Game
from Controllers.Controller import Controller
from Model.Menu import Menu
from Subject import Subject
from Window import Window


class MenuController(Controller):
    __input = None

    def __init__(self, menu: Menu):
        super().__init__(menu)

    
