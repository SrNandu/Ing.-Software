from Subject import Subject


class Menu(Subject):
    __boton: int = 0
    __cantBotones: int

    def __init__(self, cantBotones):
        super().__init__()
        self.__cantBotones = cantBotones

    def botonSig(self):
        self.__boton = self.__boton + 1
        if self.__boton == self.__cantBotones:
            self.__boton = 0

        self._notify(self)

    def botonAnt(self):
        self.__boton = self.__boton - 1
        if self.__boton == -1:
            self.__boton = self.__cantBotones
        
        self._notify(self)

    def getBoton(self):
        return self.__boton