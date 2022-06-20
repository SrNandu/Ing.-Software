import pygame
import sys
import os

# Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))

# Nombre del directorio padre
padre = os.path.dirname(actual)

# Añadir el directorio padre al sys.path
sys.path.append(padre)

from Model.Colisiones import Colisiones
from Model.GameObject import GameObject
from Model.Tuberia import Tuberia
import pytest

@pytest.fixture
def gameObject():
    return GameObject(pygame.image.load("Sprites/bird.png"))

@pytest.fixture
def tuberia():
    return Tuberia(pygame.image.load("Sprites/pipe.png"), False)

def test_interseccionRectangulos_intersectanHorizontal():
    
    assert Colisiones._Colisiones__intersectanRectangulos([1,1],[5,2],[6,1],[4,2]) == True

def test_interseccionRectangulos_intersectanVertical():
    
    assert Colisiones._Colisiones__intersectanRectangulos([1,1],[1,2],[1,2],[1,2]) == True

def test_interseccionRectangulos_noIntersectanHorizontal():
    
    assert Colisiones._Colisiones__intersectanRectangulos([1,1],[4,1],[6,1],[1,2]) == False

def test_interseccionRectangulos_noIntersectanVertical():
    
    assert Colisiones._Colisiones__intersectanRectangulos([1,1],[1,2],[4,1],[1,2]) == False

def test_colisiona_colisionIzquierda(gameObject : GameObject, tuberia : Tuberia):
    gameObject.mover(1,1)
    tuberia.mover(40,1)
    assert Colisiones.colisiona(gameObject,tuberia) == True

def test_colisiona_colisionDerecha(gameObject : GameObject, tuberia : Tuberia):
    gameObject.mover(40,1)
    tuberia.mover(1,1)
    assert Colisiones.colisiona(gameObject,tuberia) == True

def test_colisiona_colisionArriba(gameObject : GameObject, tuberia : Tuberia):
    gameObject.mover(1,40)
    tuberia.mover(1,1)
    assert Colisiones.colisiona(gameObject,tuberia) == True

def test_colisiona_colisionAbajo(gameObject : GameObject, tuberia : Tuberia):
    gameObject.mover(1,1)
    tuberia.mover(1,300)
    assert Colisiones.colisiona(gameObject,tuberia) == True

def test_colisiona_noColisionIzquierda(gameObject : GameObject, tuberia : Tuberia):
    gameObject.mover(1,1)
    tuberia.mover(60,1)
    assert Colisiones.colisiona(gameObject,tuberia) == False

def test_colisiona_noColisionDerecha(gameObject : GameObject, tuberia : Tuberia):
    gameObject.mover(60,1)
    tuberia.mover(1,1)
    assert Colisiones.colisiona(gameObject,tuberia) == False

def test_colisiona_noColisionArriba(gameObject : GameObject, tuberia : Tuberia):
    gameObject.mover(1,60)
    tuberia.mover(1,1)
    assert Colisiones.colisiona(gameObject,tuberia) == False

def test_colisiona_noColisionAbajo(gameObject : GameObject, tuberia : Tuberia):
    gameObject.mover(1,1)
    tuberia.mover(1,330)
    assert Colisiones.colisiona(gameObject,tuberia) == False

def test_parTuberiasAfuera_x_100(tuberia0 : Tuberia, tuberia1 : Tuberia):
    tuberia0.mover(-100,1)
    tuberia1.mover(-100,400)
    assert Colisiones.parTuberiasAfuera([tuberia0, tuberia1]) == True

def test_parTuberiasAfuera_x100(tuberia0 : Tuberia, tuberia1 : Tuberia):
    tuberia0.mover(100,1)
    tuberia1.mover(100,400)
    assert Colisiones.parTuberiasAfuera([tuberia0, tuberia1]) == False