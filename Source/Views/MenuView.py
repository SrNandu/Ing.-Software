from Model.Menu import Menu
from PuntajeService import PuntajeService
from Views.View import View
from Controllers.Controller import Controller
from PyQt5.QtWidgets import QGridLayout, QPushButton, QLabel, QWidget
from PyQt5.QtCore import *
from PyQt5 import QtGui
from Model.Camara import Camara
import numpy as np
from Window import Window


class MenuView(View):
    __botones: list[QPushButton] = []
    __puntajeText: QLabel
    __puintajeService: PuntajeService = PuntajeService()
    __camara = Camara()
    __camaraFrame: QtGui.QImage = QtGui.QImage()

    def __init__(self, controller: Controller):
        super().__init__(controller)

        self.__botones.append(QPushButton("Jugar"))
        self.__botones.append(QPushButton("InputCabeza"))
        self.__botones.append(QPushButton("InputMano"))
        self.__botones.append(QPushButton("Salir"))

        puntaje = str(self.__puintajeService.getPuntajeMax())
        self.__puntajeText = QLabel("Puntaje Máximo: " + puntaje)
        self.__puntajeText.setAlignment(Qt.AlignHCenter)

        main_layout = QGridLayout(self)
        main_layout.setHorizontalSpacing(15)
        main_layout.setVerticalSpacing(15)

        main_layout.addWidget(self.__botones[0], 0, 0, 1, 2)
        main_layout.addWidget(self.__botones[2], 1, 1, 1, 1)
        main_layout.addWidget(self.__botones[1], 1, 0, 1, 1)
        main_layout.addWidget(self.__puntajeText, 2, 0, 1, 2)
        main_layout.addWidget(self.__botones[3], 3, 0, 1, 2)

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
