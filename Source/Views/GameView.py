import pygame
from pygame import Surface
from Subject import Subject
from Observer import Observer


class GameView(Observer):
    __ancho = 0
    __alto = 0
    __ventana = None

    __fondo = pygame.image.load("Sprites/background.jpg")

    def __init__(self, ancho: int, alto: int):
        self.__alto = alto
        self.__ancho = ancho
        self.__ventana = pygame.display.set_mode((self.__ancho, self.__alto))

    def update(self, subject : Subject):
        self.__actualizarVista(subject.getState())

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
