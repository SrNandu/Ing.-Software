from pygame import Surface


class GameObject(object):

    _posicionX: int = 0
    _posicionY: int = 0
    _velocidadX: int = 0
    _velocidadY: int = 0

    _sprite: Surface

    def __init__(self, sprite : Surface):
        self._sprite = sprite

    def mover(self, x : int, y : int):
        self._posicionX = x
        self._posicionY = y

    def actualizar(self, deltaTime : float):
        self._posicionX += self._velocidadX * deltaTime
        self._posicionY += self._velocidadY * deltaTime

    def setVelocidad(self, velx : int, vely : int):
        self._velocidadX = velx
        self._velocidadY = vely

    def getPosicion(self) -> tuple:
        return (self._posicionX, self._posicionY)

    def getSprite(self) -> Surface:
        return self._sprite
