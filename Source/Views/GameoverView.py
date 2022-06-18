from Source.Subject import Subject
from View import View
from Controllers.Controller import Controller
from PyQt5.QtWidgets import QMainWindow


class GameoverView(View):

    def __init__(self,controller: Controller):
        super().__init__(self,controller)
