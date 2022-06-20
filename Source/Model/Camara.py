from threading import Thread
from Model.InputStrategy import InputStrategy
from Subject import Subject
from imutils.video import VideoStream
import imutils
import cv2


class Camara(Subject):
    __inputStrategy: InputStrategy

    # SINGLETON
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Camara, cls).__new__(cls)
        return cls.instance

    def start(self):
        thread = Thread(target=self.__startReconocimiento)
        thread.start()

    def setInputStrategy(self, inputStrategy: InputStrategy):
        self.__inputStrategy = inputStrategy

    def __startReconocimiento(self):
        vs = VideoStream(src=0).start()

        while True:
            self.__frame = vs.read()
            #self.__frame = imutils.resize(self.__frame, width=450)
            frameGray = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY)

            shape = self.__inputStrategy.reconocer(frameGray)

            if len(shape) > 0:
                boca = cv2.convexHull(shape[60:68])
                cv2.drawContours(self.__frame, [boca], -1, (0, 255, 0), 1)

            self._notify(self)


    def getFrame(self):
        return self.__frame
