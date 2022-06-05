from statistics import mode
import pygame
from pygame import Surface
from Controllers.GameController import GameController
from Views.View import View
from Subject import Subject
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget


class GameView(View):
    __vista = None

    __fondo = pygame.image.load("Sprites/background.jpg")

    def __init__(self, model: Subject, ancho: int, alto: int):
        super().__init__(model)
        self.__vista = pygame.Surface((ancho, alto))

        self._controller = GameController(self, model, 1)
        self.__actualizarVista(model.getState())

    def update(self):
        self.__actualizarVista(self._model.getState())
        QWidget.update(self)

    def getAncho(self):
        return self.__vista.get_width()

    def getAlto(self):
        return self.__vista.get_height()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.__image)
        qp.end()

    def __actualizarVista(self, gameObjectsStates: list[tuple[Surface, tuple[int, int]]]):
        # Dibujar fondo
        self.__vista.blit(self.__fondo, (0, 0))

        # Dibujar estado del game
        self.__vista.blits(gameObjectsStates)

        self.__image = QtGui.QImage(self.__vista.get_buffer().raw,
        self.getAncho(),
        self.getAlto(), QtGui.QImage.Format.Format_RGB32)
