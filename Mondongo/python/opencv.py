import cv2
import numpy as np
import pyautogui
import matplotlib.pyplot as plt

# Clase de captura de pantalla
class screenCapture:
    def __init__(self, posx, posy, width, height):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.screen = pyautogui.screenshot(region=(self.posx, self.posy, self.width, self.height))

    def showScreen(self):
        # Convierte la captura de pantalla a un arreglo NumPy
        screenshot_np = np.array(self.screen)
        # Muestra la imagen utilizando Matplotlib
        plt.imshow(screenshot_np)
        plt.axis('off')  # Desactiva los ejes (opcional)
        plt.show()

    def getScreen(self):
        return self.screen

    def saveScreen(self, filename):
        self.screen.save(filename)

# Test de class
if __name__ == "__main__":
    sc = screenCapture(0, 0, 800, 800)
    sc.showScreen()

