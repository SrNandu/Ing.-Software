from ast import Import
from gameObject import gameObject 
from vista import vista
import pygame
import sys

class game:

    __pajaro = gameObject(pygame.image.load("Sprites/bird.png"))
    __tuberiasArriba = []
    __tuberiasAbajo = []
    __input = None
    __ventana = vista(800,640)
    __reloj = pygame.time.Clock()

    __puntaje = 0

    def __init__(self, input):
        self.__input = input
        self.__initTuberias()
        self.__initPajaro()

    def __initTuberias(self):
        for i in range(10):
            espacio = 30

            tuberiaArriba = gameObject(pygame.image.load("Sprites/pipe.png"))

            alto = tuberiaArriba.getSprite().get_size()[1]
            tuberiaArriba.mover(self.__ventana.getAncho() / 2 + 100 * i, self.__ventana.getAlto() / 2 + espacio)

            self.__tuberiasArriba.append(tuberiaArriba)

            tuberiaAbajo = gameObject(pygame.image.load("Sprites/pipe.png"))
            tuberiaAbajo.mover(self.__ventana.getAncho() / 2 + 100 * i, self.__ventana.getAlto() / 2 - espacio - alto)

            self.__tuberiasAbajo.append(tuberiaAbajo)

    def __initPajaro(self):
        self.__pajaro.mover(self.__ventana.getAncho() / 5,self.__ventana.getAlto() / 2)
        
    def loop(self):
        while True:

            #Deberia ir en input
            #Chequear si se cerro la ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()			    

            if(game.__colisiona(self.__tuberiasArriba,self.__tuberiasAbajo,self.__pajaro)):
                pass

            if(game.__gol(self.__tuberiasArriba,self.__tuberiasAbajo,self.__pajaro)):
                self.__puntaje += 1

            self.__dibujar()
            
    def __colisiona(tuberiasArriba : list[gameObject], tuberiasAbajo: list[gameObject], pajaro : gameObject):
        return False

    def __gol(tuberiasArriba : list[gameObject], tuberiasAbajo: list[gameObject], pajaro : gameObject):
        return False

    def __dibujar(self):

        #Renderizar pajaro
        self.__ventana.renderizar(self.__pajaro)

        #Renderizar tuberias inferiores
        for i in range(len(self.__tuberiasAbajo)):
            self.__ventana.renderizar(self.__tuberiasAbajo[i])

        #Renderizar tuberias superiores
        for i in range(len(self.__tuberiasArriba)):
            self.__ventana.renderizar(self.__tuberiasArriba[i])

        #Actualizar vista
        self.__ventana.actualizarVentana()
        self.__reloj.tick(30)
