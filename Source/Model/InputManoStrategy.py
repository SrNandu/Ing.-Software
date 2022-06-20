import cv2
from Model.InputStrategy import InputStrategy
from imutils import face_utils

class InputManoStrategy(InputStrategy):
    def __init__(self):
        super().__init__()

    def reconocer(self, frame):
        caras = self._detectorCara(frame, 0)

        for cara in caras:
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = self._detectorPuntosCara(frame, cara)
            shape = face_utils.shape_to_np(shape)

            self._gesto = ""
            self._detectarAperturaBoca(shape)

            #Nariz
            self._posicion = shape[29][1]

            #Dibujar contorno boca
            boca = cv2.convexHull(shape[60:68])
            cv2.drawContours(frame, [boca], -1, (0, 255, 0), 1)


        self._notifySignal.emit()

        return []