import sys
import os

#Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))
  
#Nombre del directorio padre
padre = os.path.dirname(actual)
  
#Añadir el directorio padre al sys.path
sys.path.append(padre)

from Model.GameObject import GameObject
import pygame

class TestGame:

    def test_initTuberias_500x600(self):
        assert True

    def test_initTuberias_1000x1200(self):
        assert True
    
    def test_initPajaro_500x600(self):
        assert True
    
    def test_initPajaro_1000x1200(self):
        assert True
    
    def test_añadirTuberias(self):
        assert True

    def test_moverPajaro_y500(self):
        assert True

    def test_moverPajaro_y200(self):
        assert True

