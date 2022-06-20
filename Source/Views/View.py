from Observer import Observer
import Controllers.Controller as Controller
from Subject import Subject
from PyQt5.QtWidgets import QWidget, QMainWindow


class View(QWidget, Observer):
    _controller: Controller

    def __init__(self, controller: Controller):
        super().__init__()

        self._controller = controller
