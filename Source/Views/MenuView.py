from Views.View import View
from Controllers.Controller import Controller
from PyQt5.QtWidgets import QGridLayout, QPushButton


class MenuView(View):

    __botones: list[ QPushButton] = []

    def __init__(self, controller: Controller):
        super().__init__(controller)

        self.__botones.append(QPushButton("Jugar"))
        self.__botones.append(QPushButton("InputCabeza"))
        self.__botones.append(QPushButton("InputMano"))

        main_layout = QGridLayout(self)
        main_layout.setHorizontalSpacing(15)
        main_layout.setVerticalSpacing(15)

        main_layout.addWidget(self.__botones[0], 0, 0, 1, 2)
        main_layout.addWidget(self.__botones[1], 1, 1, 1, 1)
        main_layout.addWidget(self.__botones[2], 1, 0, 1, 1)

        self.setLayout(main_layout)
        self.setVisible(True)

    
