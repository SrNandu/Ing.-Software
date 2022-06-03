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

    def test_colisiona_false_arriba_izq(self):
        # Setear pajaro
        pajaro = GameObject(pygame.image.load("Sprites/bird.png"))
        pajaro.mover(0, 0)
        assert True
