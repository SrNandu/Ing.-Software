import sys, time, random, pygame

from pytest import Instance
from collections import deque
import cv2 as cv, mediapipe as mp

class Camara(View):
    __streamVideo: None
    __input: None
    __instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            instance = super().__new__(*args, **kwargs)
            cls.__instance[cls] = instance
        return cls.__instance[cls]

    def __init__(self):
        # Configuración de mediapipe:
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_face_mesh = mp.solutions.face_mesh
        drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
        
        
    def startCaptura(self):
        # Se debe captar una vez por webcam -> 0
        capture = cv.VideoCapture(0)
        window_size = (capture.get(cv.CAP_PROP_FRAME_WIDTH), capture.get(cv.CAP_PROP_FRAME_HEIGHT)) # width by height
        screen = pygame.display.set_mode(window_size)
        

    def getFrame(self):
        success, frame = capture.read()
       

#    def setInputStrategy(self, inputStrategy):
 
#    def procesarFrames(self):
