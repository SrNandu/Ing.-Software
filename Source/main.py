from PyQt5.QtWidgets import QApplication
from Views.MenuView import MenuView
from Model.Menu import Menu
from Controllers.MenuController import MenuController
from Window import Window
import sys
from PuntajeService import PuntajeService
from Model.Camara import Camara
import pygame

pygame.init()

app = QApplication(sys.argv)
Window.createWindow(1280, 720)

camara = Camara()
service = PuntajeService()
camara.setInputStrategy(service.getImputStrategy())
camara.start()

menu = Menu(4)
menuController = MenuController(menu)
menuView = MenuView(menuController)

menu.suscribirse(menuView)

Window.setViewActual(menuView)
        
app.exec_()

camara.stop()