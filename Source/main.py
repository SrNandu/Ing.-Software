from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sys
from Model.Game import Game
from Controllers.GameController import GameController
from Views.View import View
from Views.GameView import GameView


class Window:
    __app: QApplication
    __window: QMainWindow
    __stackedWidget: QStackedWidget

    def createWindow(ancho: int, alto: int):
        Window.__window = QMainWindow()
        Window.__window.setFixedWidth(ancho)
        Window.__window.setFixedHeight(alto)

        Window.__stackedWidget = QStackedWidget()
        Window.__window.setCentralWidget(Window.__stackedWidget)
        
        Window.__window.show()

    def setViewActual(view: View):
        if Window.__stackedWidget.indexOf(view) == -1:
            #Vista no añadida
            Window.__stackedWidget.addWidget(view)

        Window.__stackedWidget.setCurrentWidget(view)

    def removeView(view: View):
        Window.__stackedWidget.removeWidget(view)       


app = QApplication(sys.argv)
Window.createWindow(600, 500)

game = Game(600, 500)
gameController = GameController(game, 1)
gameView = GameView(gameController, 600, 500)

game.suscribirse(gameView)

Window.setViewActual(gameView)
        
app.exec_()
