from io import TextIOWrapper
import os
class PuntajeService: 
    
    __puntajeMax: int = 0
    __inputStrategy: None #Class ImputStrategy
    def __init__(self):
        file: TextIOWrapper
        if os.path.isfile('Textos/puntaje.txt'):
            
            with open("Textos/puntaje.txt","r") as file:
                
               __puntajeMax = int(file.read()) 
                
        else: 
            file = open("Textos/puntaje.txt", "w")            
            file.write("0")
            __puntajeMax = int(file.read)



    def getImputStrategy(self):
        return self.__inputStrategy

    def setImputStrategy(self, inputStrategy ):#:ImputStategy
       self.__inputStrategy = inputStrategy

    def getPuntajeMax(self):
        return self.__puntajeMax

    def setPuntajeIfMax(self, puntaje :int):
        if(puntaje> self.__puntajeMax):
            self.__setPuntajeMax(puntaje)  

    def __setPuntajeMax(self, puntaje :int):
        self.__puntajeMax = puntaje        
        with open("Textos/puntaje.txt", "w") as file: 
            file.write("Puntaje maximo:" + self.__puntajeMax)
