import numpy as np
import pygame
from pygame import Color, Surface
from Model.Game import Game
from Controllers.Controller import Controller
from Model.Camara import Camara
from Views.View import View
from Subject import Subject
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget
from Window import Window
import cv2
from PuntajeService import PuntajeService


class GameView(View):
    __gameSurface: Surface
    __imagenGame: QtGui.QImage

    __fondo = pygame.image.load("Sprites/background.jpg")
    __pausa: Surface
    __font: pygame.font.Font
    __pauseText: Surface
    __puntajeText: Surface
    __puntajeMaxText: Surface
    __escaladoX: float
    __escaladoY: float
    __camara: Camara = Camara()
    __camaraFrame = np.array([])

    __puntajeService = PuntajeService()

    def __init__(self, controller: Controller):
        super().__init__(controller)

        self.__pausa = Surface(
            (640, 360), pygame.SRCALPHA)
        self.__pausa.fill(Color(0, 0, 0, 130))

        self.__font = pygame.font.SysFont(None, 24)
        puntajeMax = str(self.__puntajeService.getPuntajeMax())
        self.__puntajeMaxText = self.__font.render(
            'PUNTAJE MAXIMO: ' + puntajeMax, True, Color(255, 255, 255))
        self.__puntajeText = self.__font.render(
            'PUNTAJE: 0', True, Color(255, 255, 255))
        self.__pauseText = self.__font.render(
            'PAUSA', True, Color(255, 255, 255))

        self.__gameSurface = pygame.Surface(
            (640, 360), pygame.SRCALPHA)

        self.__imagenGame = QtGui.QImage(self.__gameSurface.get_buffer().raw,
                                         self.__gameSurface.get_width(),
                                         self.__gameSurface.get_height(), QtGui.QImage.Format.Format_RGB32)

    def update(self, sender: Subject):
        if isinstance(sender, Camara):
            sender: Camara
            self.__camaraFrame = self.__camara.getFrame()
        if isinstance(sender, Game):
            sender: Game
            self.__actualizarGame(
                sender.getGameObjectsState(), sender.isPausado(), sender.getPuntaje())

        # Llama el paintEvent
        QWidget.update(self)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)

        qp.drawImage(0, 0, self.__imagenGame.scaled(
            Window.getWidth(), Window.getHeight()))
        qp.end()

    def __actualizarGame(self, gameObjectsStates: list[tuple[Surface, tuple[int, int]]], pausado: bool, puntaje: int):
        """
        Renderiza los sprites de los gameObjects en una imagen

        :param gameObjectsStates: Lista con tuplas con sprite y coordenadas de posicion del objecto (x,y)
        """
        # Dibujar fondo
        # self.__gameSurface.blit(self.__fondo, (0, 0))

        # Dibujar Camara de fondo
        if len(self.__camaraFrame):
            camaraSurf = pygame.surfarray.make_surface(cv2.rotate(
                self.__camaraFrame, cv2.ROTATE_90_COUNTERCLOCKWISE))
            self.__gameSurface.blit(camaraSurf, (0, 0))

        self.__gameSurface.blits(gameObjectsStates)

        ancho = self.__gameSurface.get_width()
        alto = self.__gameSurface.get_height()

        # Renderizar puntaje actual
        self.__puntajeText = self.__font.render(
            'PUNTAJE: '+str(puntaje), True, Color(255, 255, 255))
        self.__gameSurface.blit(self.__puntajeText, (0, 0))
        # Renderizar puntaje maximo
        textRect = self.__puntajeMaxText.get_rect(
                top=self.__puntajeText.get_height())
        self.__gameSurface.blit(self.__puntajeMaxText, textRect)

        if pausado:
            self.__gameSurface.blit(self.__pausa, (0, 0))
            textRect = self.__pauseText.get_rect(
                center=self.__gameSurface.get_rect().center)
            self.__gameSurface.blit(self.__pauseText, textRect)

        self.__imagenGame = QtGui.QImage(self.__gameSurface.get_buffer().raw,
                                         ancho,
                                         alto,
                                         QtGui.QImage.Format.Format_RGB32)
