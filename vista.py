import pygame

from gameObject import gameObject

class vista:
    ANCHO_VENTANA = 600
    ALTO_VENTANA = 500
    
    __ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

    def renderizar(self, gameObject:gameObject):
        self.__ventana.blit(gameObject.getSprite(), (gameObject.getPosicionX(), gameObject.getPosicionY()))
        