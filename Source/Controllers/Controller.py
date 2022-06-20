from Observer import Observer
from Subject import Subject



class Controller(Observer):
    _model: Subject

    def __init__(self, model: Subject):
      
        self._model = model
        self._model.suscribirse(self)