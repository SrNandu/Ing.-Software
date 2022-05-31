from abc import abstractmethod


class Object :
    
    _posicionX = 0
    _posicionY = 0
    _velocidadX = 0
    _velocidadY = 0
    
    _sprite = None
    
    def __init__(self,sprite):
        self._sprite = sprite
    
    def mover(self,x,y):
        self._posicionX = x
        self._posicionY = y

    
    def actualizar(self, deltaTime):
        self._posicionX += self._velocidadX * deltaTime
        self._posicionY += self._velocidadY * deltaTime
        
