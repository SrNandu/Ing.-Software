from PyQt5.QtWidgets import QApplication
from Views.MenuView import MenuView
from Model.Menu import Menu
from Controllers.MenuController import MenuController
from Window import Window
import sys
from PuntajeService import PuntajeService

app = QApplication(sys.argv)
Window.createWindow(600, 500)

service = PuntajeService()

inputStrategy = service.getImputStrategy()

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