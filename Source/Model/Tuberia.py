import random
from pygame import Surface
from Model.GameObject import GameObject

class Tuberia(GameObject):
    __espacioX = 150
    __espacioY = 60

    def __init__(self, sprite: Surface):
        self._velocidadX = -30
        super().__init__(sprite)

    def actualizar(self, deltaTime: float):
        super().actualizar(deltaTime)

    def posicionarConRespectoAbajo(self, inicioX: int, altoVentana: int, i: int, tuberiaInferior : "Tuberia"):
        rand = random.randint(-100, 100)

        alto = self._sprite.get_size()[1]

        self.mover(inicioX + self.__espacioX * i,
                   altoVentana / 2 + rand + self.__espacioY)

        tuberiaInferior.mover(inicioX + self.__espacioX * i,
                              altoVentana / 2 + rand - self.__espacioY - alto)
