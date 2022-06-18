from Source.Subject import Subject
from View import View
from PyQt5.QtWidgets import QMainWindow


class GameoverView(View):

    def __init__(self, window: QMainWindow, model: Subject):
        super().__init__(window, model)
