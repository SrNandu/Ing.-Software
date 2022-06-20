from Observer import Observer
from PyQt5.QtCore import QObject

class Subject(QObject):
    __observers: list[Observer] = []
    
    def suscribirse(self, observer: Observer):
        self.__observers.append(observer)

    def desuscribirse(self, observer: Observer):
        self.__observers.remove(observer)

    def desuscribirTodos(self):
        self.__observers.clear()

    def _notify(self, sender):
        for observer in self.__observers:
            observer.update(self)
