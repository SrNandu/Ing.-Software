from concurrent.futures import thread
from PuntajeService import PuntajeService
from threading import Thread
from Subject import Subject
from Model.Colisiones import Colisiones
from Model.GameObject import GameObject
from Model.Tuberia import Tuberia
import pygame
import random
from PyQt5.QtCore import pyqtSignal
from Window import Window


class Game(Subject):
    __pajaro = GameObject(pygame.image.load("Sprites/bird.png"))
    __tuberias: list[tuple[Tuberia]] = []
    __cantTuberias: int = 10
    __relojFrames: pygame.time.Clock
    __puntaje: int = 0
    __puntajeService: PuntajeService = PuntajeService()

    __ancho: int
    __alto: int

    __pausado: bool = False
    __gameoverSignal: pyqtSignal = pyqtSignal()
    __gameover: bool = False

    def __init__(self):
        super().__init__()

        self.__ancho = 640
        self.__alto = 360
        self.__tuberias = self.__makeTuberias()
        self.__initPajaro()

        self.__relojFrames = pygame.time.Clock()

    def start(self):
        """
        Lanzar el game loop en un nuevo hilo
        """

        # Comunicacion entre hilos ya que no puedo crear nueva view(GameoverView) desde el hilo nuevo
        gameLoopThread = Thread(target=self.__gameLoop)
        self.__gameoverSignal.connect(self.__onGameover)
        gameLoopThread.start()

    def setPausa(self, pausado: bool):
        self.__pausado = pausado

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

    def getPuntaje(self) -> int:
        return self.__puntaje

    def moverPajaro(self, posY):
        if not self.__pausado:
            self.__pajaro.mover(self.__pajaro.getPosicion()[0], posY)

    def __initPajaro(self):
        """
        Inicializar pajaro en la posicion inicial
        """
        self.__pajaro.mover(self.__ancho / 5, self.__alto / 2)

    def __makeTuberias(self) -> list[tuple[Tuberia]]:
        """
        Inicializar tuberias en posicion inicial
        """
        tuberias: list[tuple[Tuberia]] = []

        for i in range(self.__cantTuberias):
            if i == 0:
                # No hay tuberias entonces posicionar en la posicion de la primera tuberia
                tuberias.append(self.__makeParTuberias(self.__ancho / 2))
            else:
                # Posicionar detras del ultimo par de tuberias
                tuberias.append(self.__makeParTuberias(
                    tuberias[-1][0].getPosicion()[0]))

        return tuberias

    def __makeParTuberias(self, x: int) -> tuple[Tuberia]:
        """
        Añade un par de tuberias (una superior, otra inferior) al juego

        :param x: posicion donde se posiciona el par de tuberias
        """
        # Crear tuberia de abajo
        tuberiaInferiorSurface = pygame.transform.rotate(
            pygame.image.load("Sprites/pipe.png"), 180)
        tuberiaInferior = Tuberia(tuberiaInferiorSurface, False)

        # Crear tuberia de arriba
        tuberiaSuperior = Tuberia(pygame.image.load("Sprites/pipe.png"), True)

        rand = random.randint(-100, 100)

        # Posicionar tuberia inferior
        tuberiaInferior.posicionarTuberia(x, self.__alto, rand)

        # Posicionar tuberia superior
        tuberiaSuperior.posicionarTuberia(x, self.__alto, rand)

        return (tuberiaInferior, tuberiaSuperior)

    def __gameLoop(self):
        """
        Game loop
        """
        indice: int = 0
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
                    self.__tuberias.append(self.__makeParTuberias(
                        self.__tuberias[-1][0].getPosicion()[0]))
                    indice = indice-1

                # actualizo el puntaje de manera media chota perdon nandu

            if(Colisiones.atravesoTuberias(self.__tuberias[indice], self.__pajaro)):
                self.__puntaje = self.__puntaje + 1
                indice = indice + 1
                self.__puntajeService.setPuntajeIfMax(self.__puntaje)

            # Notifica que cambio el modelo
            self._notify(self)

            self.__relojFrames.tick(60)

    def __onGameover(self):
        self.__gameover = True
        self._notify(self)
