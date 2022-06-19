import pygame
import sys
import os

#Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))
  
#Nombre del directorio padre
padre = os.path.dirname(actual)
  
#Añadir el directorio padre al sys.path
sys.path.append(padre)

from PuntajeService import PuntajeService

class test_puntajeService:

    def test_get_puntaje_0():
        obj = PuntajeService()
        assert obj.getPuntajeMax == 0

    def test_get_puntaje_max():
        obj = PuntajeService()
        PuntajeService.setPuntajeIfMax(100)
        assert obj.getPuntajeMax == 100