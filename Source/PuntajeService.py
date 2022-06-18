import os
class puntajeService: 
    
    __instance: None
    __puntajeMax: int

    def __init__(self):

        if os.path.isfile('Textos/puntaje.txt'):
            with open("Textos/puntaje.txt","r") as archivo:
                for linea in archivo:
                    print(linea)
        else: 
            file = open("Textos/puntaje.txt", "w")            
            file.write("Puntaje maximo:")