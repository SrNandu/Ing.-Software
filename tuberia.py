from gameObject import gameObject

class tuberia(gameObject):

    def posicionar(self, anchoVentana : int, altoVentana : int , i : int, arriba : bool):
        espacio = 30

        alto = self._sprite.get_size()[1]
        
        if arriba:
            self.mover(anchoVentana / 2 + 100 * i, altoVentana / 2 + espacio)
        else:
            self.mover(anchoVentana / 2 + 100 * i, altoVentana / 2 - espacio - alto)