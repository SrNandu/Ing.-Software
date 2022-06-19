from io import TextIOWrapper
import os


class PuntajeService:

    __puntajeMax: int = 0
    __inputStrategy: str = "InputCabezaStrategy"

    def __init__(self):
        file: TextIOWrapper
        if os.path.isfile('puntaje.txt'):
            with open("puntaje.txt", "r") as file:
                self.__puntajeMax = int(file.readline())
                self.__inputStrategy = file.readline()

        else:
            self.__escribirArchivo()

    def setImputStrategy(self, inputStrategy):  # :ImputStategy
        self.__inputStrategy = inputStrategy
        self.__escribirArchivo()  

    def setPuntajeIfMax(self, puntaje: int):
        if(puntaje > self.__puntajeMax):
            self.__puntajeMax = puntaje
            self.__escribirArchivo()     

    def getImputStrategy(self):
        return self.__inputStrategy

    def getPuntajeMax(self):
        return self.__puntajeMax

    def __escribirArchivo(self):
        with open("puntaje.txt", "w") as file:
            file.write(str(self.__puntajeMax))
            file.write("\n")
            file.write(self.__inputStrategy)
