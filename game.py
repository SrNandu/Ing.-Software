from ast import Import
from Object import Object 
import pygame

class Game:

    __pajaro = Object(pygame.image.load("Sprites/bird.png"))
    __tuberiasArriba = []
    __tuberiasAbajo = []
    __input = None

    __puntaje = 0

    def __init__(self,input):
        self.__input = input
        
    def Loop(self):
        while True:

            if(self.Choco(self.__tuberiasArriba,self.__tuberiasAbajo,self.__pajaro)):
                pass

            if(self.Gol(self.__tuberiasArriba,self.__tuberiasAbajo,self.__pajaro)):
                self.__puntaje += 1
            
    def Choco(tuberiasArriba,tuberiasAbajo,pajaro):
        return False

    def Gol(tuberiasArriba,tuberiasAbajo,pajaro):
        return False
