from Subject import Subject
from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import sys
import os
from PyQt5.QtCore import pyqtSignal

# Nombre del directorio
actual = os.path.dirname(os.path.realpath(__file__))

# Nombre del directorio padre
padre = os.path.dirname(actual)


class InputStrategy(Subject):
    CEJA_UMBRAL = 0.3
    CEJA_FRAMES = 5

    BOCA_UMBRAL = 0.45
    BOCA_FRAMES = 5

    # Landmarks Ojos
    (cejaStart, cejaEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eyebrow"]

    __bocaAbiertaFrames: int = 0

    __bocaAbierta: bool = False

    _posicion: float = 0
    _gesto: str

    _detectorCara: None
    _detectorPuntosCara: None

    _notifySignal: pyqtSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self._detectorCara = dlib.get_frontal_face_detector()
        path = padre + '\\shape_predictor_68_face_landmarks.dat'
        self._detectorPuntosCara = dlib.shape_predictor(path)
        
        self._notifySignal.connect(self.__onMovimiento)

    def reconocer(self, frame):
        pass

    def getGesto(self):
        return self._gesto

    def _detectarAperturaBoca(self, puntosCara):
        aperturaBoca = self.__calcularAperturaBoca(puntosCara[60:68])

        if aperturaBoca > self.BOCA_UMBRAL:
            self.__bocaAbiertaFrames = self.__bocaAbiertaFrames + 1
            if self.__bocaAbiertaFrames > self.BOCA_FRAMES:
                self.__bocaAbierta = True
        else:
            if self.__bocaAbierta:
                if self.__bocaAbiertaFrames > self.BOCA_FRAMES * 3:
                    self._gesto = "BocaLargo"
                else:
                    self._gesto = "Boca"
                print(self._gesto)

            self.__bocaAbierta = False
            self.__bocaAbiertaFrames = 0

    def __calcularAperturaBoca(self, boca):
        # Calcula distancia eucleciana de las landmarks verticales
        V = dist.euclidean(boca[2], boca[6])
        # Calcula distancia eucleciana de las landmarks verticales horizontales
        H = dist.euclidean(boca[0], boca[4])

        return V / H

    def __onMovimiento(self):
        self._notify(self)
