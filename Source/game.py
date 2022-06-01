from ast import Import
from gameObject import gameObject
from tuberia import tuberia
from vista import vista
import pygame
import sys


class game:

    __fondo = gameObject(pygame.image.load("Sprites/background.jpg"))
    __pajaro = gameObject(pygame.image.load("Sprites/bird.png"))
    __tuberiasArriba = []
    __tuberiasAbajo = []
    __input = None
    __vista = vista(800, 640)
    __reloj = pygame.time.Clock()

    __puntaje = 0

    def __init__(self, input):
        self.__input = input
        self.__initTuberias()
        self.__initPajaro()

    def __initTuberias(self):
        for i in range(10):
            # Crear tuberias de arriba
            tuberiaArriba = tuberia(pygame.image.load("Sprites/pipe.png"))
            tuberiaArriba.posicionar(
                self.__vista.getAncho(), self.__vista.getAlto(), i, True)
            self.__tuberiasArriba.append(tuberiaArriba)

            # Crear tuberias de abajo
            tuberiaAbajo = tuberia(pygame.image.load("Sprites/pipe.png"))
            tuberiaAbajo.posicionar(
                self.__vista.getAncho(), self.__vista.getAlto(), i, False)
            self.__tuberiasAbajo.append(tuberiaAbajo)

    def __initPajaro(self):
        self.__pajaro.mover(self.__vista.getAncho() / 5,
                            self.__vista.getAlto() / 2)

    def loop(self):
        while True:
            # Deberia ir en input
            # Chequear si se cerro la ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime = self.__reloj.get_time() / 1000

            # Actualizar tuberias inferiores
            for i in range(len(self.__tuberiasAbajo)):
                self.__tuberiasAbajo[i].actualizar(deltaTime)

            # Actualizar tuberias superiores
            for i in range(len(self.__tuberiasArriba)):
                self.__tuberiasArriba[i].actualizar(deltaTime)

            if(game.__colisiona(self.__tuberiasArriba, self.__tuberiasAbajo, self.__pajaro)):
                pass

            if(game.__gol(self.__tuberiasArriba, self.__tuberiasAbajo, self.__pajaro)):
                self.__puntaje += 1

            self.__dibujar()

    def __colisiona(tuberiasArriba: list[gameObject], tuberiasAbajo: list[gameObject], pajaro: gameObject):
        return False

    def __gol(tuberiasArriba: list[gameObject], tuberiasAbajo: list[gameObject], pajaro: gameObject):
        return False

    def __dibujar(self):

        # Renderizar fondo
        self.__vista.renderizar(self.__fondo)

        # Renderizar pajaro
        self.__vista.renderizar(self.__pajaro)

        # Renderizar tuberias inferiores
        for i in range(len(self.__tuberiasAbajo)):
            self.__vista.renderizar(self.__tuberiasAbajo[i])

        # Renderizar tuberias superiores
        for i in range(len(self.__tuberiasArriba)):
            self.__vista.renderizar(self.__tuberiasArriba[i])

        # Actualizar vista
        self.__vista.actualizarVentana()
        self.__reloj.tick(60)
