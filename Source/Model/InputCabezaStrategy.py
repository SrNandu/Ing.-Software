import cv2
from Model.InputStrategy import InputStrategy
from imutils import face_utils
import mediapipe as mp


class InputCabezaStrategy(InputStrategy):
    __detectorManos = mp.solutions.hands.Hands(static_image_mode=False,
                                               max_num_hands=1,
                                               min_detection_confidence=0.5,
                                               min_tracking_confidence=0.5)
    __mpDraw = mp.solutions.drawing_utils

    def __init__(self):
        super().__init__()

    def reconocer(self, frame):
        mano = self.__detectorManos.process(frame)
        #print(results.multi_hand_landmarks)
        if mano.multi_hand_landmarks:
            for handLms in mano.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    #print(id,lm)
                    h, w, c = frame.shape
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    #if id ==0:
                    cv2.circle(frame, (cx,cy), 3, (255,0,255), cv2.FILLED)

                self.__mpDraw.draw_landmarks(frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)

        caras = self._detectorCara(frame, 0)
        for cara in caras:
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = self._detectorPuntosCara(frame, cara)
            shape = face_utils.shape_to_np(shape)

            self._gesto = ""
            self._detectarAperturaBoca(shape)

            # Dibujar contorno boca
            boca = cv2.convexHull(shape[60:68])
            cv2.drawContours(frame, [boca], -1, (0, 255, 0), 1)

        self._notifySignal.emit()

        return []
