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

def test_interseccionRectangulos_intersectanHorizontal():
    
    assert Colisiones._Colisiones__intersectanRectangulos([1,1],[5,2],[6,1],[4,2]) == True

def test_interseccionRectangulos_intersectanVertical():
    
    assert Colisiones._Colisiones__intersectanRectangulos([1,1],[1,2],[1,2],[1,2]) == True

def test_interseccionRectangulos_noIntersectanHorizontal():
    
    assert Colisiones._Colisiones__intersectanRectangulos([1,1],[4,1],[6,1],[1,2]) == False

def test_interseccionRectangulos_noIntersectanVertical():
    
    assert Colisiones._Colisiones__intersectanRectangulos([1,1],[1,2],[4,1],[1,2]) == False

def test_Colisiona():
    assert None
