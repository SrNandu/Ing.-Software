import pygame
from pygame import Surface
from Controllers.GameController import GameController
from Views.View import View
from Subject import Subject
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget


class GameView(View):
    __vista: Surface
    __fondo = pygame.image.load("Sprites/background.jpg")
    __imagen: QtGui.QImage

    def __init__(self, model: Subject, ancho: int, alto: int):
        super().__init__(model)
        self.__vista = pygame.Surface((ancho, alto))

        self._controller = GameController(self, model, 1)

        self.__imagen = QtGui.QImage(self.__vista.get_buffer().raw,
        self.__vista.get_width(),
        self.__vista.get_height(), QtGui.QImage.Format.Format_RGB32)

    def update(self, mensaje: list[tuple[Surface, tuple[int, int]]]):
        self.__actualizarVista(mensaje)
        #Llama el paintEvent
        QWidget.update(self)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.__imagen)
        qp.end()

    def __actualizarVista(self, gameObjectsStates: list[tuple[Surface, tuple[int, int]]]):
        """
        Renderiza los sprites de los gameObjects en una imagen

        :param gameObjectsStates: Lista con tuplas con sprite y coordenadas de posicion del objecto (x,y)
        """
        # Dibujar fondo
        self.__vista.blit(self.__fondo, (0, 0))

        # Dibujar estado del game
        self.__vista.blits(gameObjectsStates)

        self.__imagen = QtGui.QImage(self.__vista.get_buffer().raw,
        self.__vista.get_width(),
        self.__vista.get_height(), QtGui.QImage.Format.Format_RGB32)
