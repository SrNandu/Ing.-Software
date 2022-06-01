import pygame
from gameObject import gameObject


class test_gameObject:

    def testMoverPositivo():
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.mover(300, 250)
        assert obj.getPosicion == (300, 250)

    def testMoverNegativo():
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.mover(-300, -250)
        assert obj.getPosicion == (-300, -250)

    def testMoverCero():
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.mover(0, 0)
        assert obj.getPosicion == (0, 0)

    def testMoverAfuera():
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.mover(-1000, 1000)
        assert obj.getPosicion == (-300, -250)

    def testActualizar60fps():
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.setVelocidad(5, 7)
        obj.actualizar(0.016)
        assert obj.getPosicion() == (0.08, 0.112)

    def testActualizar20fps():
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.setVelocidad(5, 7)
        obj.actualizar(0.05)
        assert obj.getPosicion() == (0.25, 0.35)

    def testActualizar100fps():
        obj = gameObject(pygame.image.load("Sprites/bird.png"))
        obj.setVelocidad(5, 7)
        obj.actualizar(0.01)
        assert obj.getPosicion() == (0.05, 0.07)
