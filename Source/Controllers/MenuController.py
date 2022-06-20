from attr import s
from Model.Game import Game
from Model.InputStrategy import InputStrategy
from Model.InputCabezaStrategy import InputCabezaStrategy
from Model.InputManoStrategy import InputManoStrategy
from Views.GameView import GameView
from Controllers.GameController import GameController
from Controllers.Controller import Controller
from Model.Menu import Menu
from Window import Window
from PuntajeService import PuntajeService
from Model.Camara import Camara
from PyQt5.QtWidgets import QApplication


class MenuController(Controller):
    __input = None
    __puntajeService = PuntajeService()

    def __init__(self, menu: Menu):
        super().__init__(menu)

    def update(self, sender):
        if isinstance(sender, InputStrategy):
            sender: InputStrategy
            gesto = sender.getGesto()
            if gesto == "Boca":
                self._model.botonSig()
            elif gesto == "BocaLargo":
                self.__enter()

    def __enter(self):
        boton = self._model.getBoton()

        if boton == 0:
            self.__startGame()
        elif boton == 1:
            inputStrategy = InputCabezaStrategy()
            self.__puntajeService.setImputStrategy(inputStrategy)
            Camara().setInputStrategy(inputStrategy)
        elif boton == 2:
            inputStrategy = InputManoStrategy()
            self.__puntajeService.setImputStrategy(inputStrategy)
            Camara().setInputStrategy(inputStrategy)
        elif boton == 3:
            QApplication.quit()
            
    def __startGame(self):
        self._model.desuscribirTodos()

        game = Game()
        gameView = GameView(GameController(game))
        Window.setViewActual(gameView)

        game.suscribirse(gameView)
        game.start()
        pass
