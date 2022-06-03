from Observer import Observer
from Subject import Subject

class View(Observer):
    _controller = None
    _model = None

    def __init__(self, model: Subject):
        self._model = model
        self._model.suscribirse(self)
