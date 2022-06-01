from observer import observer

class subject(object):
    __observers = []
    
    def suscribirse(self, observer: observer):
        self.__observers.append(observer)

    def desuscribirse(self, observer: observer):
        self.__observers.remove(observer)

    def _notify(self):
        for observer in self.__observers:
            observer.update()
