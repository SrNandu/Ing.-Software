import pygame
import sys
import os

#Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))
  
#Nombre del directorio padre
padre = os.path.dirname(actual)
  
#Añadir el directorio padre al sys.path
sys.path.append(padre)

from gameObject import gameObject


class test_gameObject:

    def testMoverPositivo(self):
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.mover(300, 250)
        assert obj.getPosicion == (300, 250)

    def testMoverNegativo(self):
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.mover(-300, -250)
        assert obj.getPosicion == (-300, -250)

    def testMoverCero(self):
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.mover(0, 0)
        assert obj.getPosicion == (0, 0)

    def testMoverAfuera(self):
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.mover(-1000, 1000)
        assert obj.getPosicion == (-300, -250)

    def testActualizar60fps(self):
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.setVelocidad(5, 7)
        obj.actualizar(0.016)
        assert obj.getPosicion() == (0.08, 0.112)

    def testActualizar20fps(self):
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.setVelocidad(5, 7)
        obj.actualizar(0.05)
        assert obj.getPosicion() == (0.25, 0.35)

    def testActualizar100fps(self):
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.setVelocidad(5, 7)
        obj.actualizar(0.01)
        assert obj.getPosicion() == (0.05, 0.07)
