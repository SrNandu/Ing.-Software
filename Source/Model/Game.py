from Subject import Subject
from Model.Colisiones import Colisiones
from Model.GameObject import GameObject
from Model.Tuberia import Tuberia
import pygame
import random


class Game(Subject):
    __pajaro = GameObject(pygame.image.load("Sprites/bird.png"))
    __tuberias: list[Tuberia] = []
    __cantTuberias: int = 10
    __reloj = pygame.time.Clock()

    def __init__(self, ancho: int, alto: int):
        pygame.init()

        self.__initTuberias(ancho, alto)
        self.__initPajaro(ancho, alto)

    def start(self):
        while True:
            deltaTime = self.__reloj.get_time() / 1000

            # Actualizar tuberias
            for i in range(len(self.__tuberias)):
                self.__tuberias[i].actualizar(deltaTime)

            # Chequear colision
            if(Colisiones.colisiona(self.__tuberias, self.__pajaro)):
                return

            # Notfica que cambio el modelo
            self._notify()

            self.__reloj.tick(60)

    def getState(self):
        states = []

        states.append((self.__pajaro.getSprite(), self.__pajaro.getPosicion()))
        states.extend((o.getSprite(), o.getPosicion())
                      for o in self.__tuberias)

        return states

    def __initTuberias(self, ancho: int, alto: int):
        for i in range(self.__cantTuberias):
            if i == 0:
                self.__añadirParTuberias(ancho / 2, alto)
            else:
                self.__añadirParTuberias(self.__tuberias[-1].getPosicion()[0], alto)

    def __añadirParTuberias(self, x: int, alto: int):
            # Crear tuberia de abajo
            tuberiaInferior = Tuberia(
                pygame.image.load("Sprites/pipe.png"), False)

            # Crear tuberia de arriba
            tuberiaSuperior = Tuberia(
                pygame.image.load("Sprites/pipe.png"), True)

            rand = random.randint(-100, 100)

            # Posicionar tuberia inferior
            tuberiaInferior.posicionarTuberia(x, alto, rand)

            #Posicionar tuberia superior
            tuberiaSuperior.posicionarTuberia(x, alto, rand)

            self.__tuberias.append(tuberiaSuperior)
            self.__tuberias.append(tuberiaInferior)

    def __initPajaro(self, ancho: int, alto: int):
        self.__pajaro.mover(ancho / 5, alto / 2)
