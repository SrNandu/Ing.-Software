import os
class PuntajeService: 
    
    __instance: None
    __puntajeMax: int
    __inputStrategy: None #Class ImputStrategy
    def __init__(self):

        if os.path.isfile('Textos/puntaje.txt'):
            with open("Textos/puntaje.txt","r") as archivo:
                for linea in archivo:
                    print(linea)
        else: 
            file = open("Textos/puntaje.txt", "w")            
            file.write("Puntaje maximo:")

    def getImputStrategy(self):
        return self.__inputStrategy

    def setImputStrategy(self, inputStrategy):
       self.__inputStrategy = inputStrategy

    def getPuntajeMax(self):
        return self.__puntajeMax

    def setPuntajeIfMax(self, puntaje):
        if(puntaje> self.__puntajeMax):
            self.__setPuntajeMax()  

    def __setPuntajeMax(self):
            file = open("Textos/puntaje.txt", "w")            
            file.write("Puntaje maximo:" + self.__puntajeMax)
