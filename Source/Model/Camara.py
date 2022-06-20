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

            self.__frame = self.__inputStrategy.reconocer(self.__frame)

            self._notify(self)

    def getFrame(self):
        return self.__frame
