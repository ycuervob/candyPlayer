from ScreenCapture import ScreenCapture
import numpy as np
#Clase que convierte la imagen al un arreglo de 9x9 de numpy
class Convertion:
    
    def __init__(self, screenCapture: ScreenCapture):
        self.screenCapture = screenCapture

    def convert(self, division = 9):
        #Obtenemos la imagen
        image = self.screenCapture.getScreen()
        #Convertimos la imagen a un arreglo de numpy
        image = np.array(image)

        #Convertimos la imagen a un arreglo de 9x9
        (imageLength, imagewidth, depth) = image.shape
        
        print(imageLength)
        
    
if __name__ == "__main__":
    sc = ScreenCapture()
    c = Convertion(sc)
    c.convert()