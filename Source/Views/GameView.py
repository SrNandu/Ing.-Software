from statistics import mode
import pygame
from pygame import Surface
from Controllers.GameController import GameController
from Views.View import View
from Subject import Subject
from Observer import Observer


class GameView(View):
    __ancho = 0
    __alto = 0
    __ventana = None

    __fondo = pygame.image.load("Sprites/background.jpg")

    def __init__(self, model: Subject, ancho: int, alto: int):
        super().__init__(model)
        
        self.__alto = alto
        self.__ancho = ancho
        self.__ventana = pygame.display.set_mode((self.__ancho, self.__alto))

        self._controller = GameController(self, model, 1)

    def update(self):
        self.__actualizarVista(self._model.getState())

    def getAncho(self):
        return self.__ancho

    def getAlto(self):
        return self.__alto

    def __actualizarVista(self, gameObjectsStates: list[tuple[Surface, tuple[int, int]]]):
        # Dibujar fondo
        self.__ventana.blit(self.__fondo, (0, 0))

        # Dibujar estado del game
        self.__ventana.blits(gameObjectsStates)

        pygame.display.update()
