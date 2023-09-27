import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
import cv2

# Clase de captura de pantalla
class ScreenCapture:
    def __init__(self, posx = 100, posy = 10, width = 650, height = 580):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        rgbscreen = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(self.posx, self.posy, self.posx+self.width, self.posy+self.height))), cv2.COLOR_RGB2BGR)    
        self.screen = np.array(cv2.cvtColor(rgbscreen, cv2.COLOR_BGR2HSV))

    def setScreen(self):
        rgbscreen = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(self.posx, self.posy, self.posx+self.width, self.posy+self.height))), cv2.COLOR_RGB2BGR)    
        self.screen = np.array(cv2.cvtColor(rgbscreen, cv2.COLOR_BGR2HSV))

    def showScreen(self):
        # Convierte la captura de pantalla a un arreglo NumPy
        screenshot_np = np.array(self.screen)
        # Muestra la imagen utilizando Matplotlib
        plt.imshow(screenshot_np)
        plt.axis('off')  # Desactiva los ejes (opcional)
        plt.show()

    def getScreen(self):
        return self.screen

# Test de class
if __name__ == "__main__":
    #Posiciones absolutas candy
    x = 100
    y = 10
    width = 650
    height = 580
    sc = ScreenCapture(x, 1080-768 + y, width, height)
    sc2 = ScreenCapture()
    sc.showScreen()
    sc2.showScreen()

