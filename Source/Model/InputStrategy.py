from Subject import Subject
from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import sys
import os

# Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))

# Nombre del directorio padre
padre = os.path.dirname(actual)


class InputStrategy(Subject):
    OJO_UMBRAL = 0.3
    OJO_FRAMES = 5

    BOCA_UMBRAL = 0.45
    BOCA_FRAMES = 10

    # Landmarks Ojos
    (oIStart, oIEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]

    __ojoIFrames: int = 0
    __ojoDFrames: int = 0
    __bocaAbiertaFrames: int = 0

    __ojoICerrado: bool = False
    __ojoDCerrado: bool = False
    __bocaAbierta: bool = False

    _posicion: float = 0
    __gesto: str

    _detectorCara: None
    _detectorPuntosCara: None

    def __init__(self):
        super().__init__()

        self._detectorCara = dlib.get_frontal_face_detector()
        path = padre + '\\shape_predictor_68_face_landmarks.dat'
        self._detectorPuntosCara = dlib.shape_predictor(path)

    def reconocer(self, frame):
        pass

    def _detectarGuiño(self, puntosCara):
        ojoIzq = puntosCara[self.oIStart:self.oIEnd]
        ojoDer = puntosCara[self.oDStart:self.oDEnd]

        aperturaOjoIzq = self.__calcularAperturaOjo(ojoIzq)
        aperturaOjoDer = self.__calcularAperturaOjo(ojoDer)

        if aperturaOjoIzq < self.OJO_UMBRAL:
            self.__ojoIFrames = self.__ojoIFrames + 1
            if self.__ojoIFrames > self.OJO_FRAMES and (not self.__ojoDCerrado and not self.__ojoICerrado):
                self.__ojoICerrado = True
                self.__gesto = "GiñoI"
                print(self.__gesto)
        else:
            self.__ojoICerrado = False
            self.__ojoIFrames = 0

        if aperturaOjoDer < self.OJO_UMBRAL:
            self.__ojoDFrames = self.__ojoDFrames + 1
            if self.__ojoDFrames > self.OJO_FRAMES and (not self.__ojoDCerrado and not self.__ojoICerrado):
                self.__ojoDCerrado = True
                self.__gesto = "GiñoD"
                print(self.__gesto)
        else:
            self.__ojoDCerrado = False
            self.__ojoDFrames = 0

    def _detectarAperturaBoca(self, puntosCara):
        aperturaBoca = self.__calcularAperturaBoca(puntosCara[60:68])

        if aperturaBoca > self.OJO_UMBRAL:
            self.__bocaAbiertaFrames = self.__bocaAbiertaFrames + 1
            if self.__bocaAbiertaFrames > self.BOCA_UMBRAL and not self.__bocaAbierta:
                self.__bocaAbierta = True
                self.__gesto = "Boca"
                print(self.__gesto)
        else:
            self.__bocaAbierta = False
            self.__bocaAbiertaFrames = 0

    def __calcularAperturaBoca(self, boca):
        # Calcula distancia eucleciana de las landmarks verticales
        V = dist.euclidean(boca[2], boca[6])
        # Calcula distancia eucleciana de las landmarks verticales horizontales
        H = dist.euclidean(boca[0], boca[4])

        return V / H

    def __calcularAperturaOjo(self, ojo):
        # Calcula distancia eucleciana de las landmarks verticales
        A = dist.euclidean(ojo[1], ojo[5])
        B = dist.euclidean(ojo[2], ojo[4])
        # Calcula distancia eucleciana de las landmarks verticales horizontales
        C = dist.euclidean(ojo[0], ojo[3])

        return (A + B) / (2.0 * C)
