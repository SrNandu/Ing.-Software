from Observer import Observer
import Controllers.Controller as Controller
from Subject import Subject
from PyQt5.QtWidgets import QWidget, QMainWindow


class View(QWidget, Observer):
    _controller: Controller
    _model: Subject

    def __init__(self, window: QMainWindow, model: Subject):
        super().__init__()
        window.setCentralWidget(self)

        self._model = model
        self._model.suscribirse(self)
