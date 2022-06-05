from pygame import Surface
from Model.GameObject import GameObject


class Tuberia(GameObject):
    __superior: bool
    __espacioX = 150
    __espacioY = 60

    def __init__(self, sprite: Surface, superior: bool):
        super().__init__(sprite)
        self._velocidadX = -30
        self.__superior = superior

    def actualizar(self, deltaTime: float):
        super().actualizar(deltaTime)

    def posicionarTuberia(self, tuberiaAnteriorX: int, altoVentana: int, random: int):
        alto = self._sprite.get_size()[1]

        if(self.__superior):
            self.mover(tuberiaAnteriorX + Tuberia.__espacioX, altoVentana /
                       2 + Tuberia.__espacioY + random)
        else:
            self.mover(tuberiaAnteriorX + Tuberia.__espacioX, altoVentana / 2 -
                       Tuberia.__espacioY - alto + random)
