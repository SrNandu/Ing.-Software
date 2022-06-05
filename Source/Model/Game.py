from Subject import Subject
from Model.Colisiones import Colisiones
from Model.GameObject import GameObject
from Model.Tuberia import Tuberia
import pygame
import random


class Game(Subject):
    __pajaro = GameObject(pygame.image.load("Sprites/bird.png"))
    __tuberias: list[tuple[Tuberia]] = []
    __cantTuberias: int = 10
    __reloj = pygame.time.Clock()

    __ancho: int
    __alto: int

    def __init__(self, ancho: int, alto: int):
        pygame.init()

        self.__ancho = ancho
        self.__alto = alto
        self.__initTuberias()
        self.__initPajaro()

    def start(self):
        while True:
            deltaTime = self.__reloj.get_time() / 1000

            # Actualizar tuberias
            for parTuberias in self.__tuberias:
                for tuberia in parTuberias:
                    tuberia.actualizar(deltaTime)
                    if(Colisiones.colisiona(tuberia, self.__pajaro)):
                        return

                if(Colisiones.parTuberiasAfuera(parTuberias)):
                    self.__tuberias.remove(parTuberias)
                    self.__añadirParTuberias(self.__tuberias[-1][0].getPosicion()[0])

            # Notfica que cambio el modelo
            self._notify()

            self.__reloj.tick(60)

    def getState(self):
        states = []

        states.append((self.__pajaro.getSprite(), self.__pajaro.getPosicion()))
        states.extend((tub.getSprite(), tub.getPosicion())
                      for tuple in self.__tuberias for tub in tuple)

        return states

    def __initTuberias(self):
        for i in range(self.__cantTuberias):
            if i == 0:
                self.__añadirParTuberias(self.__ancho / 2)
            else:
                self.__añadirParTuberias(self.__tuberias[-1][0].getPosicion()[0])

    def __añadirParTuberias(self, x: int):
        # Crear tuberia de abajo
        tuberiaInferior = Tuberia(
            pygame.image.load("Sprites/pipe.png"), False)

        # Crear tuberia de arriba
        tuberiaSuperior = Tuberia(
            pygame.image.load("Sprites/pipe.png"), True)

        rand = random.randint(-100, 100)

        # Posicionar tuberia inferior
        tuberiaInferior.posicionarTuberia(x, self.__alto, rand)

        # Posicionar tuberia superior
        tuberiaSuperior.posicionarTuberia(x, self.__alto, rand)

        self.__tuberias.append((tuberiaInferior, tuberiaSuperior))

    def __initPajaro(self):
        self.__pajaro.mover(self.__ancho / 5, self.__alto / 2)
