from ast import Import
from gameObject import gameObject 
from vista import vista
import pygame

class Game:

    __pajaro = gameObject(pygame.image.load("Sprites/bird.png"))
    __tuberiasArriba = []
    __tuberiasAbajo = []
    __input = None

    __puntaje = 0

    def __init__(self,input):
        self.__input = input

    def initTuberias(self):
        for i in range(10):
            espacio = 30

            tuberiaArriba = gameObject(pygame.image.load("Sprites/pipe.png"))

            alto = tuberiaArriba.getSprite().get_size()[1]
            tuberiaArriba.mover(20 * i, vista.ALTO_VENTANA / 2 + espacio)

            self.__tuberiasArriba.append(tuberiaArriba)

            tuberiaAbajo = gameObject(pygame.image.load("Sprites/pipe.png"))
            tuberiaAbajo.mover(20 * i, vista.ALTO_VENTANA / 2 - espacio - alto)

            self.__tuberiasAbajo.append(tuberiaAbajo)
        
    def loop(self):
        while True:

            if(self.colisiona(self.__tuberiasArriba,self.__tuberiasAbajo,self.__pajaro)):
                pass

            if(self.gol(self.__tuberiasArriba,self.__tuberiasAbajo,self.__pajaro)):
                self.__puntaje += 1
            
    def colisiona(tuberiasArriba : list[gameObject], tuberiasAbajo: list[gameObject], pajaro : gameObject):
        return False

    def gol(tuberiasArriba : list[gameObject], tuberiasAbajo: list[gameObject], pajaro : gameObject):
        return False
