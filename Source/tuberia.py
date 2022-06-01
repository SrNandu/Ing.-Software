import random
from pygame import Surface
from gameObject import gameObject


class tuberia(gameObject):

    def __init__(self, sprite: Surface):
        self._velocidadX = -30
        super().__init__(sprite)

    def posicionar(self, anchoVentana: int, altoVentana: int, i: int, arriba: bool):
        espacio = 50
        rand = random.randint(-50, 50)

        alto = self._sprite.get_size()[1]

        if arriba:
            self.mover(anchoVentana / 2 + 150 * i, altoVentana / 2 + espacio + rand)
        else:
            self.mover(anchoVentana / 2 + 150 * i,
                       altoVentana / 2 - espacio - alto + rand)
