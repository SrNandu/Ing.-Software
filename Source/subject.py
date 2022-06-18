from Observer import Observer

class Subject(object):
    __observers: list[Observer] = []
    
    def suscribirse(self, observer: Observer):
        self.__observers.append(observer)

    def desuscribirse(self, observer: Observer):
        self.__observers.remove(observer)

    def _notify(self, sender):
        for observer in self.__observers:
            observer.update(self)
