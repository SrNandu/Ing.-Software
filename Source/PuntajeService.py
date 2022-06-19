from io import TextIOWrapper
import os
from Model.InputStrategy import InputStrategy
from Model.InputCabezaStrategy import InputCabezaStrategy
from Model.InputManoStrategy import InputManoStrategy



class PuntajeService:

    __puntajeMax: int = 0
    __inputStrategy: InputStrategy = InputCabezaStrategy()

    def __init__(self):
        file: TextIOWrapper
        if os.path.isfile('puntaje.txt'):
            with open("puntaje.txt", "r") as file:
                self.__puntajeMax = int(file.readline())
                input = file.readline()

                if input == "InputManoStrategy":
                    self.__inputStrategy = InputManoStrategy()

        else:
            self.__escribirArchivo()

    def setImputStrategy(self, inputStrategy: InputStrategy):  # :ImputStategy
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
            file.write(self.__inputStrategy.__class__.__name__)
