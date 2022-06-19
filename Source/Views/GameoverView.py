from Views.View import View
from Controllers.Controller import Controller
from PyQt5.QtWidgets import QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import *
from PuntajeService import PuntajeService


class GameoverView(View):
    __puntajeText: QLabel
    __puntajeMaxText: QLabel
    __recordText: QLabel
    __puintajeService: PuntajeService = PuntajeService()

    def __init__(self, controller: Controller, puntajeConseguido: int):
        super().__init__(controller)

        self.__botones.append(QPushButton("Nueva Partida"))
        self.__botones.append(QPushButton("Menu"))

        self.__puntajeText = QLabel("Puntaje Conseguido: " + puntajeConseguido)
        self.__puntajeText.setAlignment(Qt.AlignHCenter)

        puntajeMax = str(self.__puintajeService.getPuntajeMax())
        self.__puntajeMaxText = QLabel("Puntaje Máximo: " + puntajeMax)
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

    def __actualizarMenu(self, botonActual: int):
        for boton in self.__botones:
            boton.setStyleSheet("background-color : white")

        self.__botones[botonActual].setStyleSheet("background-color : yellow")