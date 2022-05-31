from curses import window
import pygame


class vista:
    __anchoVentana =600
    __altoVentana =500
    
    ventana = pygame.display.set_mode((__anchoVentana,__altoVentana))

    def renderizar(self):
        window.blit(pygame.image.load("Sprites/background.png"), (0, 0))
        window.blit(pygame.image.load("Sprites/bird.png"), (120, 250))