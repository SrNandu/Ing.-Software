import pytest
import sys
import os

# Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))

# Nombre del directorio padre
padre = os.path.dirname(actual)

# Añadir el directorio padre al sys.path
sys.path.append(padre)

from Model.Tuberia import Tuberia
from Model.Game import Game


@pytest.fixture
def game500x600():
    return Game(500, 600)


@pytest.fixture
def game1000x1200():
    return Game(1000, 1200)


def test_initTuberias_500x600(game500x600):
    tuberias: list[tuple[Tuberia]] = game500x600._Game__tuberias

    #Chequa que este bien separadas y que esten alineadas verticalmente
    for i in range(len(tuberias)):
        if i == 0:
            if tuberias[i][0].getPosicion()[0] - 500 / 2 != Tuberia._Tuberia__espacioX:
                assert False
        else:
            if tuberias[i][0].getPosicion()[0] - tuberias[i-1][0].getPosicion()[0] != Tuberia._Tuberia__espacioX:
                assert False

        #Alineamiento vertical
        if tuberias[i][0].getPosicion()[0] != tuberias[i][1].getPosicion()[0]:
            assert False

    assert True


def test_initTuberias_1000x1200(game1000x1200):
    tuberias: list[tuple[Tuberia]] = game1000x1200._Game__tuberias

    #Chequa que este bien separadas y que esten alineadas verticalmente
    for i in range(len(tuberias)):
        if i == 0:
            if tuberias[i][0].getPosicion()[0] - 1000 / 2 != Tuberia._Tuberia__espacioX:
                assert False
        else:
            if tuberias[i][0].getPosicion()[0] - tuberias[i-1][0].getPosicion()[0] != Tuberia._Tuberia__espacioX:
                assert False

        #Alineamiento vertical
        if tuberias[i][0].getPosicion()[0] != tuberias[i][1].getPosicion()[0]:
            assert False

    assert True


def test_initPajaro_500x600(game500x600: Game):
    assert game500x600._Game__pajaro.getPosicion() == (100, 300)


def test_initPajaro_1000x1200(game1000x1200: Game):
    assert game1000x1200._Game__pajaro.getPosicion() == (200, 600)


def test_añadirTuberias(game500x600: Game):
    tuberiasAnterior: list[tuple[Tuberia]] = len(game500x600._Game__tuberias)

    game500x600._Game__añadirParTuberias(200)

    tuberias: list[tuple[Tuberia]] = len(game500x600._Game__tuberias)

    assert tuberiasAnterior + 1 == tuberias


def test_moverPajaro_y500(game500x600):
    assert True


def test_moverPajaro_y200(game500x600):
    assert True
