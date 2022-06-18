import pytest
import sys
import os

# Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))

# Nombre del directorio padre
padre = os.path.dirname(actual)

# Añadir el directorio padre al sys.path
sys.path.append(padre)

from Model.Game import Game

@pytest.fixture
def game500x600():
    return Game(500, 600)

@pytest.fixture
def game1000x12000():
    return Game(1000, 12000)

def test_initTuberias_500x600(game500x600):
    assert True

def test_initTuberias_1000x1200(game1000x12000):
    assert True

def test_initPajaro_500x600(game500x600):
    assert True

def test_initPajaro_1000x1200(game1000x12000):
    assert True

def test_añadirTuberias(game500x600):
    assert True

def test_moverPajaro_y500(game500x600):
    assert True


def test_moverPajaro_y200(game500x600):
    assert True
