from PyQt5.QtWidgets import QApplication
from Model.Game import Game
from Controllers.GameController import GameController
from Views.GameView import GameView
from Window import Window
import sys

app = QApplication(sys.argv)
Window.createWindow(600, 500)

game = Game(600, 500)
gameController = GameController(game, 1)
gameView = GameView(gameController, 600, 500)

game.suscribirse(gameView)
game.start()

Window.setViewActual(gameView)
        
app.exec_()