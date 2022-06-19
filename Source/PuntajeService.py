from io import TextIOWrapper
import os


class PuntajeService:

    __puntajeMax: int = 0
    __inputStrategy: str

    def __init__(self):
        file: TextIOWrapper
        if os.path.isfile('Textos/puntaje.txt'):
            with open("Textos/puntaje.txt", "r") as file:
                self. __puntajeMax = int(file.read())

        else:
            with open("Textos/puntaje.txt", "w") as file:
                file.write("0")
                self.__puntajeMax = int(file.readline())
                self.__inputStrategy = file.readline()

    def getInputStrategy(self):
        return self.__inputStrategy

    def setInputStrategy(self, inputStrategy):  # :InputStategy
        self.__inputStrategy = inputStrategy
        with open("Textos/puntaje.txt", "r+") as file:
            textoLineas = file.readlines()
            textoLineas[1] = type(self.__inputStrategy)
            file.write(textoLineas)

    def getPuntajeMax(self):
        return self.__puntajeMax

    def setPuntajeIfMax(self, puntaje: int):
        if(puntaje > self.__puntajeMax):
            self.__setPuntajeMax(puntaje)

    def __setPuntajeMax(self, puntaje: int):
        self.__puntajeMax = puntaje
        with open("Textos/puntaje.txt", "r+") as file:
            textoLineas = file.readlines()
            textoLineas[0] = self.__puntajeMax
            file.write(textoLineas)
