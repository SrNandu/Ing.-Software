import sys
import os

# Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))

# Nombre del directorio padre
padre = os.path.dirname(actual)

# Añadir el directorio padre al sys.path
sys.path.append(padre)

from Model.GameObject import GameObject
import pytest
import pygame

@pytest.fixture
def gameObject():
    return GameObject(pygame.image.load("Sprites/bird.png"))

def test_mover_positivo(gameObject: GameObject):
    gameObject.mover(300, 250)
    assert gameObject.getPosicion() == (300, 250)


def test_mover_Negativo(gameObject: GameObject):
    gameObject.mover(-300, -250)
    assert gameObject.getPosicion() == (-300, -250)


def test_mover_Cero(gameObject: GameObject):
    gameObject.mover(0, 0)
    assert gameObject.getPosicion() == (0, 0)


def test_mover_Afuera(gameObject: GameObject):
    gameObject.mover(-1000, 1000)
    assert gameObject.getPosicion() == (-1000, 1000)


def test_actualizar_60fps(gameObject: GameObject):
    gameObject.setVelocidad(5, 7)
    gameObject.actualizar(0.016)
    assert gameObject.getPosicion() == (0.08, 0.112)


def test_actualizar_20fps(gameObject: GameObject):
    gameObject.setVelocidad(5, 8)
    gameObject.actualizar(0.05)
    assert gameObject.getPosicion() == (0.25, 0.40)


def test_actualizar_100fps(gameObject: GameObject):
    gameObject.setVelocidad(5, 7)
    gameObject.actualizar(0.01)
    assert gameObject.getPosicion() == (0.05, 0.07)
