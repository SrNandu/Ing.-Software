from PyQt5.QtWidgets import QApplication
from Views.MenuView import MenuView
from Model.Menu import Menu
from Controllers.MenuController import MenuController
from Window import Window
import sys
from PuntajeService import PuntajeService
from Model.Camara import Camara

app = QApplication(sys.argv)
Window.createWindow(1280, 720)

camara = Camara()
service = PuntajeService()
camara.setInputStrategy(service.getImputStrategy())
camara.start()

#game = Game(600, 500)
#gameController = GameController(game, 1)
#gameView = GameView(gameController, 600, 500)

#game.suscribirse(gameView)
#game.start()

menu = Menu(3)
menuController = MenuController(menu)
menuView = MenuView(menuController)

menu.suscribirse(menuView)

Window.setViewActual(menuView)
        
app.exec_()