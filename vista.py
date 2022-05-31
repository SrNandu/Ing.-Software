from curses import window
import pygame


class vista:
    __anchoVentana =600
    __altoVentana =500
    
    ventana = pygame.display.set_mode((__anchoVentana,__altoVentana))

    def renderizar(self, gameObject):
        window.blit(gameObject.getSprite(), (gameObject.getPosicionx(), gameObject.getPosicionY()))
        