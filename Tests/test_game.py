from gameObject import gameObject
import pygame


class TestGame:

    def test():
        assert 1 == 1

    def test_colisiona_false_arriba_izq():
        # Setear pajaro
        pajaro = gameObject(pygame.image.load("Sprites/bird.png"))
        pajaro.mover(0, 0)
