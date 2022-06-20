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
def game():
    return Game()


def test_makeTuberias(game):
    tuberias: list[tuple[Tuberia]] = game._Game__makeTuberias()

    #Chequa que este bien separadas y que esten alineadas verticalmente
    for i in range(len(tuberias)):
        if i == 0:
            if tuberias[i][0].getPosicion()[0] - 640 / 2 != Tuberia._Tuberia__espacioX:
                assert False
        else:
            if tuberias[i][0].getPosicion()[0] - tuberias[i-1][0].getPosicion()[0] != Tuberia._Tuberia__espacioX:
                assert False

        #Alineamiento vertical
        if tuberias[i][0].getPosicion()[0] != tuberias[i][1].getPosicion()[0]:
            assert False

    assert True


def test_initPajaro(game: Game):
    assert game._Game__pajaro.getPosicion() == (128, 180)


def test_makeParTuberias(game: Game):
    parTuberias: tuple[Tuberia] = game._Game__makeParTuberias(200)

    #Alineamiento vertical
    if parTuberias[0].getPosicion()[0] != parTuberias[1].getPosicion()[0]:
        assert False

    #Espaciado vertical correcto
    if parTuberias[1].getPosicion()[1] - (parTuberias[0].getPosicion()[1] + parTuberias[0].getSprite().get_height()) != Tuberia._Tuberia__espacioY * 2:
        assert False

    assert True


def test_moverPajaro_y500(game):
    assert True


def test_moverPajaro_y200(game):
    assert True
