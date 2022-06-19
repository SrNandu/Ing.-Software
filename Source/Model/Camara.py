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

    def __init__(self):
        thread = Thread(target=self.__startReconocimiento)
        thread.start()

    def setInputStrategy(self, inputStrategy: InputStrategy):
        self.__inputStrategy = inputStrategy

    def __startReconocimiento(self):
        vs = VideoStream(src=0).start()

        while True:
            frame = vs.read()
            frame = imutils.resize(frame, width=450, height=250)
            frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            self.__inputStrategy.reconocer(frameGray)
            self._notify(self)
