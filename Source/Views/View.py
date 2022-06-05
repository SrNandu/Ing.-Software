from Observer import Observer
from Subject import Subject
from PyQt5.QtWidgets import QWidget, QMainWindow


class View(QWidget, Observer):
    _controller = None
    _model = None

    def __init__(self, model: Subject, parent: QMainWindow = None):
        super().__init__(parent)

        self._model = model
        self._model.suscribirse(self)
