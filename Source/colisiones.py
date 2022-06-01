from Source.gameObject import gameObject


class colisiones:

    def __colisiona(tuberiasArriba: list[gameObject], tuberiasAbajo: list[gameObject], pajaro: gameObject):
        return False

    def intersectanRectangulos(x1, y1, ancho1, alto1, x2, y2, ancho2, alto2):
        # Si un rectangulo esta del lado izquierdo del otro
        if(x1 > x2 + ancho2 or x2 > x1 + ancho1):
            return False

        # Si un rectangulo esta arriba del otro
        if(y1 + alto1 > y2 or y2 + alto2 > y1):
            return False

        return True
