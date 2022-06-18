from time import sleep
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import sys
from Model.Game import Game
from Views.GameView import GameView

app = QApplication(sys.argv)
window = QMainWindow()
window.setFixedWidth(600)
window.setFixedHeight(500)

game = Game(600, 500)
gameView = GameView(window, game, 600, 500)

window.show()
app.exec_()
