from Window import Window
import cv2
from Model.InputStrategy import InputStrategy
from imutils import face_utils
import mediapipe as mp


class InputManoStrategy(InputStrategy):
    __detectorManos = mp.solutions.hands.Hands(static_image_mode=False,
                                               max_num_hands=1,
                                               min_detection_confidence=0.5,
                                               min_tracking_confidence=0.5)
    __mpDraw = mp.solutions.drawing_utils

    def __init__(self):
        super().__init__()

    def reconocer(self, frame):
        frameHand = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mano = self.__detectorManos.process(frameHand)
        # print(results.multi_hand_landmarks)
        if mano.multi_hand_landmarks:
            for handLms in mano.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y*h)
                    cv2.circle(frame, (cx, cy), 3, (255, 0, 255), cv2.FILLED)

                    if id == 9:
                        self._posicion = lm.y * Window.getHeight()

            self.__mpDraw.draw_landmarks(
                frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)

        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        caras = self._detectorCara(frameGray, 0)
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

        return frame
