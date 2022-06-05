from pygame import Surface


class GameObject(object):

    __posicionX: int = 0
    __posicionY: int = 0
    __velocidadX: int = 0
    __velocidadY: int = 0

    __sprite: Surface

    def __init__(self, sprite : Surface):
        self.__sprite = sprite

    def mover(self, x : int, y : int):
        """
        Mover a las coordenadas indicadas

        :param x: Coordenada en el eje x
        :param y: Coordenada en el eje y
        """
        self.__posicionX = x
        self.__posicionY = y

    def actualizar(self, deltaTime : float):
        """
        Actualizar poscion segun velocidad

        :param deltaTime: Tiempo transcurrido desde el ultimo frame
        """
        self.__posicionX += self.__velocidadX * deltaTime
        self.__posicionY += self.__velocidadY * deltaTime

    def setVelocidad(self, velx : int, vely : int):
        """
        Setear velocidad del objeto

        :param x: Velocidad en el eje x
        :param y: Velocidad en el eje y
        """
        self.__velocidadX = velx
        self.__velocidadY = vely

    def getPosicion(self) -> tuple:
        """
        Devuelve la posicion

        :return: Tupla con cordenadas (x,y)
        """
        return (self.__posicionX, self.__posicionY)

    def getSprite(self) -> Surface:
        """
        Devuelve sprite del objeto

        :return: Una surface que representa el sprite
        """
        return self.__sprite
