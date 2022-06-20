import numpy as np
from Model.Menu import Menu
from Model.Camara import Camara
from Views.View import View
from Controllers.Controller import Controller
from PyQt5.QtWidgets import QGridLayout, QPushButton, QLabel, QWidget
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PuntajeService import PuntajeService
from Window import Window


class GameoverView(View):
    __botones: list[QPushButton] = []
    __puntajeText: QLabel
    __puntajeMaxText: QLabel
    __recordText: QLabel
    __puintajeService: PuntajeService = PuntajeService()
    __camara = Camara()
    __camaraFrame: QtGui.QImage = QtGui.QImage()

    def __init__(self, controller: Controller, puntajeConseguido: int):
        super().__init__(controller)

        self.__botones.append(QPushButton("Nueva Partida"))
        self.__botones.append(QPushButton("Menu"))

        self.__puntajeText = QLabel("Puntaje Conseguido: " + str(puntajeConseguido))
        self.__puntajeText.setAlignment(Qt.AlignHCenter)

        puntajeMax = self.__puintajeService.getPuntajeMax()
        self.__puntajeMaxText = QLabel("Puntaje Máximo: " + str(puntajeMax))
        self.__puntajeMaxText.setAlignment(Qt.AlignHCenter)

        self.__recordText = QLabel("Nuevo Puntaje Maximo!")
        self.__recordText.setAlignment(Qt.AlignHCenter)
        self.__recordText.setVisible(puntajeConseguido > puntajeMax)

        main_layout = QGridLayout(self)
        main_layout.setHorizontalSpacing(15)
        main_layout.setVerticalSpacing(15)

        main_layout.addWidget(self.__puntajeText, 0, 0, 1, 2)
        main_layout.addWidget(self.__puntajeMaxText, 1, 0, 1, 2)
        main_layout.addWidget(self.__recordText, 2, 0, 1, 2)
        main_layout.addWidget(self.__botones[0], 3, 0, 1, 1)
        main_layout.addWidget(self.__botones[1], 3, 1, 1, 1)

        self.setLayout(main_layout)
        self.setVisible(True)

        self.__actualizarMenu(0)
        self.__camara.suscribirse(self)        

    def update(self, sender):
        if isinstance(sender, Menu):
            sender: Menu
            self.__actualizarMenu(sender.getBoton())
        if isinstance(sender, Camara):
            sender: Camara
            self.__renderCamara(sender.getFrame())

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.__camaraFrame.scaled(
            Window.getWidth(), Window.getHeight()))
        qp.end()

    def __actualizarMenu(self, botonActual: int):
        for boton in self.__botones:
            boton.setStyleSheet("background-color : white")

        self.__botones[botonActual].setStyleSheet("background-color : yellow")

    def __renderCamara(self, frame):
        im_np = np.transpose(frame, (1, 0, 2)).copy()

        self.__camaraFrame = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                                        QtGui.QImage.Format_RGB888)
        # Llama el paintEvent
        QWidget.update(self)