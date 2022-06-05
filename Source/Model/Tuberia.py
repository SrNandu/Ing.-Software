from pygame import Surface
from Model.GameObject import GameObject


class Tuberia(GameObject):
    __superior: bool
    __espacioX: int = 150
    __espacioY: int = 60

    def __init__(self, sprite: Surface, superior: bool):
        super().__init__(sprite)
        self.setVelocidad(-30, 0)
        self.__superior = superior

    def posicionarTuberia(self, tuberiaAnteriorX: int, altoVentana: int, random: int):
        """
        Posicionar tuberia detras de la tuberiaAnterior y segun el alto de la ventana

        :param tuberiaAnteriorX: Posicion en el eje x de la tuberiaAnterior
        :param altoVentana: Alto ventana
        :param random: Valor aleatorio para aleteorizar la posicion Y de la tuberia
        """
        alto = self.getSprite().get_size()[1]

        if(self.__superior):
            self.mover(tuberiaAnteriorX + Tuberia.__espacioX, altoVentana /
                       2 + Tuberia.__espacioY + random)
        else:
            self.mover(tuberiaAnteriorX + Tuberia.__espacioX, altoVentana / 2 -
                       Tuberia.__espacioY - alto + random)
