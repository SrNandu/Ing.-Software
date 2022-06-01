from pygame import Surface


class gameObject:

    _posicionX = 0
    _posicionY = 0
    _velocidadX = 0
    _velocidadY = 0

    _sprite = None

    def __init__(self, sprite):
        self._sprite = sprite

    def mover(self, x, y):
        self._posicionX = x
        self._posicionY = y

    def actualizar(self, deltaTime):
        self._posicionX += self._velocidadX * deltaTime
        self._posicionY += self._velocidadY * deltaTime

    def setVelocidad(self, velx, vely):
        self._velocidadX = velx
        self._velocidadY = vely

    def getSprite(self) -> Surface:
        return self._sprite

    def getPosicion(self) -> tuple:
        return (self._posicionX, self._posicionY)
