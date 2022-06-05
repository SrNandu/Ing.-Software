from Observer import Observer
from Subject import Subject
from PyQt5.QtWidgets import QWidget, QMainWindow


class View(QWidget, Observer):
    _controller = None
    _model = None

    def __init__(self, model: Subject):
        super().__init__()

        self._model = model
        self._model.suscribirse(self)
