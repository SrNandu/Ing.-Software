from ast import Sub
from typing import ValuesView
from Observer import Observer
from Subject import Subject
from Views.View import View


class Controller(Observer):
    _view: View
    _model: Subject

    def __init__(self, view : View, model: Subject):
        self._view = view
        
        self._model = model
        self._model.suscribirse(self)