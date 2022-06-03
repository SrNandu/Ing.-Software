from Observer import Observer

class Subject(object):
    __observers = []
    
    def suscribirse(self, observer: Observer):
        self.__observers.append(observer)

    def desuscribirse(self, observer: Observer):
        self.__observers.remove(observer)
    
    def getState(self):
        pass

    def _notify(self):
        for observer in self.__observers:
            observer.update()
