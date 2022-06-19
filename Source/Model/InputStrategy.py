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
    OJO_FRAMES = 3

    BOCA_UMBRAL = 0.7
    BOCA_FRAMES = 3

    # Landmarks Ojos
    (oIStart, oIEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (oDStart, oDEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    __ojoICerrado: bool = False
    __ojoDCerrado: bool = False
    __bocaAbierta: bool = False

    __poscicion: float
    __gesto: str

    __detectorCara: None

    def __init__(self):
        super().__init__()

        self.__detectorCara = dlib.get_frontal_face_detector()
        path = padre + '\\shape_predictor_68_face_landmarks.dat'
        self.__detectorPuntosCara = dlib.shape_predictor(path)

    def reconocer(self, frame):
        pass

    def __detectarGuiño(self, puntosCara):
        ojoIzq = puntosCara[self.oIStart:self.oIEnd]
        ojoDer = puntosCara[self.oDStart:self.oDEnd]

        aperturaOjoIzq = self.__calcularAperturaOjo(ojoIzq)
        aperturaOjoDer = self.__calcularAperturaOjo(ojoDer)

        if aperturaOjoIzq < self.OJO_UMBRAL:
            self.__ojoICerrado = True
        else:
            self.__ojoICerrado = False
            if self.__ojoICerrado == True:
                self.__gesto = "GiñoI"

        if aperturaOjoDer < self.OJO_UMBRAL:
            self.__ojoDCerrado = True
        else:
            self.__ojoDCerrado = False
            if self.__ojoDCerrado == True:
                self.__gesto = "GiñoD"

    def __detectarAperturaBoca(self, puntosCara):
        aperturaBoca = self.__calcularAperturaBoca(puntosCara[60, 67])

        if aperturaBoca > self.BOCA_UMBRAL:
            self.__bocaAbierta = True
        else:
            self.__bocaAbierta = False
            if self.__bocaAbierta == True:
                self.__gesto = "Boca"

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
