from Model.InputStrategy import InputStrategy
from imutils import face_utils


class InputCabezaStrategy(InputStrategy):
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

            self._notifySignal.emit()
            return shape

        return []