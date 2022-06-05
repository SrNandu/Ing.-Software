from Model.GameObject import GameObject
from Model.Tuberia import Tuberia


class Colisiones:

    def colisiona(tuberia: Tuberia, pajaro: GameObject) -> bool:
        posicionPajaro = pajaro.getPosicion()
        sizePajaro = pajaro.getSprite().get_size()

        posicionTuberia = tuberia.getPosicion()
        sizeTuberia = tuberia.getSprite().get_size()

        #Si intersectan los triangulos es porque colisiono
        if(Colisiones.__intersectanRectangulos(posicionPajaro, sizePajaro, posicionTuberia, sizeTuberia)):
            return True

        return False

    def parTuberiasAfuera(parTuberias: tuple[Tuberia]) -> bool:
        x = parTuberias[0].getPosicion()[0]
        ancho = parTuberias[0].getSprite().get_size()[0]

        return x + ancho < 0

    def __intersectanRectangulos(p1: tuple, size1: tuple, p2: tuple, size2: tuple) -> bool:

        x1 = p1[0]
        y1 = p1[1]
        ancho1 = size1[0]
        alto1 = size1[1]

        x2 = p2[0]
        y2 = p2[1]
        ancho2 = size2[0]
        alto2 = size2[1]

        # Si un rectangulo esta del lado izquierdo del otro
        if(x1 > x2 + ancho2 or x2 > x1 + ancho1):
            return False

        # Si un rectangulo esta arriba del otro
        if(y1 + alto1 < y2 or y2 + alto2 < y1):
            return False

        return True
