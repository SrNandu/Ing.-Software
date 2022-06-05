from Subject import Subject
from Model.Colisiones import Colisiones
from Model.GameObject import GameObject
from Model.Tuberia import Tuberia
import pygame


class Game(Subject):
    __pajaro = GameObject(pygame.image.load("Sprites/bird.png"))
    __tuberiasArriba = []
    __tuberiasAbajo = []
    __reloj = pygame.time.Clock()

    def __init__(self, ancho: int, alto: int):
        pygame.init()
        
        self.__initTuberias(ancho, alto)
        self.__initPajaro(ancho, alto)

    def start(self):
        while True:
            deltaTime = self.__reloj.get_time() / 1000

            # Actualizar tuberias inferiores
            for i in range(len(self.__tuberiasAbajo)):
                # Pasar posicion de ultima tuberia
                self.__tuberiasAbajo[i].actualizar(deltaTime)

            # Actualizar tuberias superiores
            for i in range(len(self.__tuberiasArriba)):
                # Pasar posicion de ultima tuberia
                self.__tuberiasArriba[i].actualizar(deltaTime)

            # Chequear colision
            if(Colisiones.colisiona(self.__tuberiasArriba, self.__tuberiasAbajo, self.__pajaro)):
                return

            #Notfica que cambio el modelo
            self._notify()

            self.__reloj.tick(60)

    def getState(self):
        states = []

        states.append((self.__pajaro.getSprite(), self.__pajaro.getPosicion()))
        states.extend((o.getSprite(), o.getPosicion())
                      for o in self.__tuberiasAbajo)
        states.extend((o.getSprite(), o.getPosicion())
                      for o in self.__tuberiasArriba)

        return states

    def __initTuberias(self, ancho: int, alto: int):
        for i in range(10):
            # Crear tuberia de abajo
            tuberiaAbajo = Tuberia(pygame.image.load("Sprites/pipe.png"))

            # Crear tuberia de arriba
            tuberiaArriba = Tuberia(pygame.image.load("Sprites/pipe.png"))

            # Posicionar tuberias
            tuberiaArriba.posicionarConRespectoAbajo(
                ancho / 2, alto, i, tuberiaAbajo)

            self.__tuberiasArriba.append(tuberiaArriba)
            self.__tuberiasAbajo.append(tuberiaAbajo)

    def __initPajaro(self, ancho: int, alto: int):
        self.__pajaro.mover(ancho / 5, alto / 2)
