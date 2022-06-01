import pygame

from gameObject import gameObject

class vista:
    __ancho = 0
    __alto = 0   
    __ventana = None

    def __init__(self, ancho: int, alto : int):
        self.__alto = alto
        self.__ancho = ancho
        self.__ventana = pygame.display.set_mode(self.__ancho, self.__alto)

    def renderizar(self, gameObject: gameObject):
        self.__ventana.blit(gameObject.getSprite(), gameObject.getPosicion())

    def actualizarVentana(self):
        pygame.display.update()

    def getAncho(self):
        return self.__ancho

    def getAlto(self):
        return self.__alto


        