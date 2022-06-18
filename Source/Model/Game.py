from concurrent.futures import thread
from threading import Thread
from Subject import Subject
from Model.Colisiones import Colisiones
from Model.GameObject import GameObject
from Model.Tuberia import Tuberia
import pygame
import random
from PyQt5.QtCore import pyqtSignal


class Game(Subject):
    __pajaro = GameObject(pygame.image.load("Sprites/bird.png"))
    __tuberias: list[tuple[Tuberia]] = []
    __cantTuberias: int = 10
    __relojFrames = pygame.time.Clock()

    __ancho: int
    __alto: int

    __pausado: bool = False
    __gameoverSignal: pyqtSignal = pyqtSignal()
    __gameover: bool = False

    def __init__(self, ancho: int, alto: int):
        super().__init__()
        pygame.init()

        self.__ancho = ancho
        self.__alto = alto
        self.__initTuberias()
        self.__initPajaro()

    def start(self):
        """
        Lanzar el game loop en un nuevo hilo
        """

        # Comunicacion entre hilos ya que no puedo crear nueva view(GameoverView) desde el hilo nuevo
        gameLoopThread = Thread(target=self.__gameLoop)
        self.__gameoverSignal.connect(self.__onGameover)
        gameLoopThread.start()

    def pausar(self):
        pausado = True

    def despausar(self):
        pausado = False

    def getGameObjectsState(self) -> list[tuple[pygame.Surface, tuple[int, int]]]:
        """
        Devuelve el estado del juego en forma de una lista con sprites y sus posiciones
        """
        states = []

        states.append((self.__pajaro.getSprite(), self.__pajaro.getPosicion()))
        states.extend((tub.getSprite(), tub.getPosicion())
                      for tuple in self.__tuberias for tub in tuple)

        return states

    def isGameOver(self) -> bool:
        return self.__gameover

    def isPausado(self) -> bool:
        return self.__pausado

    def __initPajaro(self):
        """
        Inicializar pajaro en la posicion inicial
        """
        self.__pajaro.mover(self.__ancho / 5, self.__alto / 2)

    def __initTuberias(self):
        """
        Inicializar tuberias en posicion inicial
        """
        for i in range(self.__cantTuberias):
            if i == 0:
                # No hay tuberias entonces posicionar en la posicion de la primera tuberia
                self.__añadirParTuberias(self.__ancho / 2)
            else:
                # Posicionar detras del ultimo par de tuberias
                self.__añadirParTuberias(
                    self.__tuberias[-1][0].getPosicion()[0])

    def __añadirParTuberias(self, x: int):
        """
        Añade un par de tuberias (una superior, otra inferior) al juego

        :param x: posicion donde se posiciona el par de tuberias
        """
        # Crear tuberia de abajo
        tuberiaInferior = Tuberia(
            pygame.image.load("Sprites/pipe.png"), False)

        # Crear tuberia de arriba
        tuberiaSuperior = Tuberia(
            pygame.image.load("Sprites/pipe.png"), True)

        rand = random.randint(-100, 100)

        # Posicionar tuberia inferior
        tuberiaInferior.posicionarTuberia(x, self.__alto, rand)

        # Posicionar tuberia superior
        tuberiaSuperior.posicionarTuberia(x, self.__alto, rand)

        self.__tuberias.append((tuberiaInferior, tuberiaSuperior))

    def __gameLoop(self):
        """
        Game loop
        """
        while True:
            if not self.__pausado:
                deltaTime = self.__relojFrames.get_time() / 1000

                # Actualizar tuberias
                for parTuberias in self.__tuberias:
                    for tuberia in parTuberias:
                        # Actualizar posicion
                        tuberia.actualizar(deltaTime)

                        if(Colisiones.colisiona(tuberia, self.__pajaro)):
                            self.__gameoverSignal.emit()
                            return

                    if(Colisiones.parTuberiasAfuera(parTuberias)):
                        self.__tuberias.remove(parTuberias)
                        self.__añadirParTuberias(
                            self.__tuberias[-1][0].getPosicion()[0])

            # Notifica que cambio el modelo
            self._notify(self)

            self.__relojFrames.tick(60)

    def __onGameover(self):
        self.__gameover = True
        self._notify(self)
