from subject import subject
from colisiones import colisiones
from gameObject import gameObject
from tuberia import tuberia
import vista
import pygame
import sys


class game(subject):

    __pajaro = gameObject(pygame.image.load("Sprites/bird.png"))
    __tuberiasArriba = []
    __tuberiasAbajo = []
    __reloj = pygame.time.Clock()

    def __init__(self, ancho, alto):
        self.__initTuberias(ancho, alto)
        self.__initPajaro(ancho, alto)

    def __initTuberias(self, ancho, alto):
        for i in range(10):
            # Crear tuberia de abajo
            tuberiaAbajo = tuberia(pygame.image.load("Sprites/pipe.png"))

            # Crear tuberia de arriba
            tuberiaArriba = tuberia(pygame.image.load("Sprites/pipe.png"))

            # Posicionar tuberias
            tuberiaArriba.posicionarConRespectoAbajo(
                ancho / 2, alto, i, tuberiaAbajo)

            self.__tuberiasArriba.append(tuberiaArriba)
            self.__tuberiasAbajo.append(tuberiaAbajo)

    def __initPajaro(self, ancho, alto):
        self.__pajaro.mover(ancho / 5, alto / 2)

    def start(self):
        while True:
            # Deberia ir en input
            # Chequear si se cerro la ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

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
            if(colisiones.colisiona(self.__tuberiasArriba, self.__tuberiasAbajo, self.__pajaro)):
                return

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
