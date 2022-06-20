import sys
import pytest
import os

# Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))

# Nombre del directorio padre
padre = os.path.dirname(actual)

# Añadir el directorio padre al sys.path
sys.path.append(padre)

from Model.Menu import Menu

@pytest.fixture
def menu5():
    return Menu(5)

def test_seleccionarSiguiente(menu5: Menu):
    menu5.botonSig()

    assert menu5._Menu__boton == 1

def test_seleccionarSiguienteLimite(menu5: Menu):
    menu5._Menu__boton = 4
    menu5.botonSig()

    assert menu5._Menu__boton == 0

def test_seleccionarAnterior(menu5: Menu):
    menu5._Menu__boton = 1
    menu5.botonAnt()

    assert menu5._Menu__boton == 0

def test_seleccionarAnteriorLimite(menu5: Menu):
    menu5.botonAnt()

    assert menu5._Menu__boton == 4