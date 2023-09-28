import numpy as np
import webbrowser
import asyncio
import matplotlib.pyplot as plt

def mostrar_color_rgb(color_rgb):
    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=color_rgb))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', 'box')
    plt.axis('off')
    plt.show()


#Clase que convierte la imagen al un arreglo de 9x9 de numpy
class Convertion:

    def __init__(self, screenCapture, baseRoute =  "Mondongo/imgCandy/", umbral = 0.95):
        self.screenCapture = screenCapture
        self.manualColors = {}
        self.colors = {
            0x01: 30,   #amarillo
            0x02: 15,   #naranja
            0x03: 120,  #azul
            0x04: 60,   #verde
            0x05: 150,  #morado
            0x06: 0     #rojo
        }

        self.colorsArray = {
            0x05: np.array([[103,  87, 111],[106,  87, 109],[111,  87, 110],[118,  84, 112],[124,  96, 113],[ 67,  70, 101],[ 75,  35, 127],[ 76, 109, 127],[ 75, 109, 127],[ 75,   1, 127],[ 75,   0, 127],[ 75,   2, 127],[  6,  78, 127],[  5, 108, 127],[  5,  43, 127],[  5,  45, 127],[  5,  45, 127],[  5,  46, 127],[  6,  43, 127],[ 76,  36, 127],[ 76, 109, 127],[  6,  41, 127],[  6,  41, 127],[ 76,   0, 127],[ 76,  36, 127],[ 76,   0, 127],[ 76,   0, 127],[ 75,   1, 127],[ 75,  41, 127],[  6,  45, 127],[  5,  47, 127],[  4,  47, 127],[  3,  44, 127],[  3,  36, 127],[  2,  34, 127],[  2,  36, 127],[  3,  47, 127],[  6,  46, 127],[  6,   1, 127],[  4,  50, 127],[  3,  48, 127],[  3,  45, 127],[  3,  44, 127],[  3,  42, 127],[  3,   3, 127],[  3,   1, 127],[  4,   0, 127],[  4,   0, 127],[  4,   0, 127],[  4,  41, 127],[  4,  36, 127],[102, 121,   5],[  1,   5, 123],[118,  81, 122],[ 67,  70, 121],[121, 111, 121],[124,  93, 117],[117,  81, 116],[111,  81, 115],[106,  86, 110],[103,  99, 100],[101, 101,  99],[100,  17, 115]],dtype=np.int8), 
            0x03: np.array([[100,  95, 111],[100, 105, 111],[100, 113, 113],[101,  92, 113],[110,   9, 126],[110,  42,  31],[109,  18,  31],[108,  23,  31],[108, 125,  31],[107,  25,  31],[107,  24,  31],[106,  22,  31],[106,  21,  31],[106,  20,  31],[105,  19,  31],[105,   0,  31],[105,  54,  31],[105,  53,  31],[104,  53,  31],[104,  51,  31],[104,  50,  31],[104,  47,  31],[104,  44,  31],[104,  42,  31],[104,   3,  31],[104,   1,  31],[103, 109,  31],[103,  40,  31],[104, 126,  31],[104, 124,  31],[104, 123,  31],[104, 127,  31],[105,   0,  31],[104, 127,  31],[104,   2,  31],[104, 119,  31],[105, 114,  31],[106, 114,  31],[107, 121,  31],[108,  42,  31],[110,   0,  42],[111,  42,  15],[110, 109,  25],[109, 121,  31],[110,  40,  31],[110,   0, 124],[110,  43,  48],[110, 127, 106],[110,  53,  12],[111,  45,   8],[112, 123,  11],[113,   9, 117],[110, 126,  84],[103,  14, 119],[103, 125, 117],[102,  77, 114],[101,   2, 112],[100, 115, 110],[ 99, 102, 110],[ 98, 100, 100],[ 99, 119,  83],[ 99, 123,  86],[ 96,  95, 105]],dtype=np.int8), 
            0x06: np.array([[ 99,  83, 117],[100,  86, 116],[100,  85, 114],[100,  83, 115],[100,  79, 113],[101,  71, 112],[101,  63, 108],[103,  53, 105],[107,  40, 101],[116,  25,  97],[  0,  23,  93],[ 85,  40,  94],[ 91,  59,  97],[ 94,  80, 101],[ 95,  99,  97],[ 93,  25,  99],[  0,   0,  89],[  0,   0,  29],[  0, 127,  38],[  0, 127, 108],[  0, 127,  41],[  0,   0,  52],[  0,   0,   3],[  0,   0,  26],[  0,   0,  61],[  0,   0,  62],[  0, 127,   0],[  0, 127,   0],[  0,   0,   0],[  0,   0,   0],[  0,   0,   0],[  0,   0,   0],[  0,   0,   0],[  0, 127,   0],[  0,   0,   0],[  0,   0, 127],[  0,   0,  28],[  0,   0,   7],[  0,   0,  28],[  1, 127,  28],[  0,   0, 120],[  1,   0,  53],[  0, 127,   4],[  0, 127,  39],[  0,   0,  25],[  0,   0, 100],[  1, 127,  87],[  0,  62,  81],[  0,  62, 101],[ 93,  14,  88],[ 92, 125, 112],[ 90, 106, 107],[ 87,  78, 102],[ 13,  48,  97],[103,  31,  99],[113,  39, 107],[104,  56, 110],[103,  67, 117],[102,  80, 121],[102,  85,   0],[101,  91, 126],[100,  96, 114],[102,  15, 126]],dtype=np.int8), 
            0x02: np.array([[ 96,  28, 101],[ 72,  10,  95],[  9,  85, 124],[ 14,  11,   1],[ 14,   9,   1],[ 14,  13,   1],[ 15,  15,   1],[ 15,  18,   1],[ 15,  25,   1],[ 15,  25,   1],[ 15,   0,   1],[ 15,  25,   1],[ 15,  22,   1],[ 15,  16,   1],[ 15,  14,   1],[ 14,  15,   1],[ 13,  16,   1],[ 14,  14,   1],[ 14,  16,   1],[ 15,  14,   1],[ 16,  11,   1],[ 16,  14,   1],[ 16,  16,   1],[ 16,  16,   1],[ 16,  16,   1],[ 16,   0,   1],[ 16,  17,   1],[ 16,  17,   1],[ 16,  17,   1],[ 16,  16,   1],[ 16,  16,   1],[ 16,  17,   1],[ 16,  16,   1],[ 16,  16,   1],[ 16,  15,   1],[ 16,  15,   1],[ 17,  15,   1],[ 17,  12,   1],[ 17,  11,   1],[ 17,   9,   1],[ 17,  10,   1],[ 17,  16,   1],[ 16,  19,   1],[ 16,  21,   1],[ 15,  23,   1],[ 15,  21,   1],[ 14,  25,   1],[ 13,  25,   1],[ 12,  24,   1],[ 11,  21,   1],[ 11,  17,   1],[ 10,   0,   1],[ 11,   4,  28],[  9,  12, 107],[  7,   5,  14],[ 10, 127, 119],[ 10, 105, 113],[  9,  69, 110],[  4,  31, 103],[109,  12, 103],[101,  34, 113],[102,  59, 110],[104,  18, 121]],dtype=np.int8), 
            0x04: np.array([[ 83,  82, 110],[ 77,  92, 110],[ 57, 124, 100],[ 51, 110,  31],[ 52,   9,  36],[ 52,  15,  32],[ 52,  12,  42],[ 52,  13, 125],[ 52,  12, 110],[ 52,  11, 112],[ 52,  13, 112],[ 52,  13, 113],[ 52,  13, 113],[ 52,  13,   4],[ 52, 127, 110],[ 52,  54, 125],[ 52,  56, 107],[ 52,  56,  40],[ 52,  57,  40],[ 52,  57,  42],[ 51,  56,  42],[ 51,  56,  42],[ 51,  25,  36],[ 51,   0,  29],[ 51,  14,  22],[ 51,  14, 105],[ 51,  14, 102],[ 52,  14,  99],[ 51,  14,  98],[ 51,   0,  97],[ 51,  14,  92],[ 51,  14,  90],[ 52,  14,  85],[ 51,   0,  91],[ 50,   0,  90],[ 50,   0,  87],[ 51,   1,   1],[ 51,   1,  17],[ 51,   1,  13],[ 51,   1, 121],[ 50,   0, 119],[ 50,   0, 114],[ 50,   1,  74],[ 51,   1, 119],[ 51,   1,  96],[ 51,   1, 122],[ 51,   1, 118],[ 51,   1, 111],[ 52,   0, 100],[ 51,   0,  93],[ 52,  63,  83],[ 52,  63,  75],[ 50,  28,  71],[ 49,  28,  58],[ 49, 123,  55],[ 59, 103, 119],[ 62, 121, 117],[ 68, 113, 118],[ 73, 103, 115],[ 78,  92, 117],[ 85,  84, 116],[ 92,  88, 111],[100, 113, 120]],dtype=np.int8), 
            0x01: np.array([[ 66,  34,  99],[ 48,  45, 103],[ 24,   8, 124],[ 28,   1,   3],[ 27,   1,   3],[ 27,   1,   3],[ 28,   3,   3],[ 28,   3,   3],[ 28,   3,   3],[ 28,   3,   3],[ 28,   3,   3],[ 28,   3,   3],[ 28,   3,   3],[ 28,   3,   3],[ 28,   3,   3],[ 28,   3,   3],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   2],[ 28,   3,   1],[ 28,   3,   1],[ 28,   3,   1],[ 27,   2,   1],[ 27,   0,   1],[ 27, 127,   0],[ 26, 127,   0],[ 26,   1,   0],[ 25,   3, 127],[ 25,   3, 127],[ 24,   3, 127],[ 23,   3, 127],[ 23,   3, 126],[ 22,   3, 126],[ 22,   3, 126],[ 21,   3, 125],[ 21,   3, 125],[ 20,   3,  59],[ 20,   3,  19],[ 19,   3,   6],[ 18,   3,  39],[ 17,   2, 105],[ 15,   3,  91],[ 17,   3,  93],[ 21,   3,  59],[ 22,   3,   3],[ 21,  52,  14],[ 24,  80,   4],[ 26, 103, 123],[ 28, 104, 115],[ 33,  75, 108],[ 43,  52,  97],[ 64,  47,  78],[ 84,  52,  87],[ 91,  53,  97]],dtype=np.int8)
        }

        self.umbral = umbral

    def clasificarColorBasic(self, pixels):
        #Creamos un arreglo para obtener los 10x10 tipos de colores de pixeles
        #Obtenemos el color de cada pixel con la distancia mas corta a los colores
        squaresize = pixels.shape
        closestColors = np.zeros((squaresize[0],squaresize[1]), dtype=np.int8)

        for i in range(squaresize[0]):
            for j in range(squaresize[1]):
                closestColors[i][j] = self.clasifyOnePixel(pixels[i][j])

        #Obtenemos el color que mas se repite
        (unique, counts) = np.unique(closestColors, return_counts=True)

        #Obtenemos el color que mas se repite
        #(unique, counts) = np.unique(representationPixels, return_counts=True)
        index = np.argmax(counts)
        return unique[index]

    def clasifyManual(self, pixels):
        #Creamos un arreglo para obtener los 10x10 tipos de colores de pixeles
        #Obtenemos el color de cada pixel con la distancia mas corta a los colores
        vectors = pixels[pixels.shape[0]//2:5+pixels.shape[0]//2][0]
        vector = np.sum(vectors, axis=0) // len(vectors)      
        color = self.clasifyOnePixel(vector)
        if color in self.manualColors:
            self.manualColors[color] = (self.manualColors[color] + pixels) // 2
        else:
            self.manualColors[color] = pixels

        return "Done"
        
    
    def printManualColors(self):
        print(self.manualColors)

    def clasifyArray(self, arrayPixels):
        distancia_minima = float('inf')
        color_clasificado = None
        peso_maximo = 1.0  # Peso máximo para el valor central
        n = arrayPixels.shape[0]
        desviacion = n / 7.0 
        ponderation = np.array([peso_maximo * np.exp(-((i - n/2)**2) / (2 * desviacion**2)) for i in range(len(arrayPixels))])
        
        for nombre_color, arrayColor in self.colorsArray.items():
            # Calcular la distancia entre el pixel y el valor H del color
            distancia = np.linalg.norm(ponderation*(arrayPixels[:,0,0] - arrayColor[:,0]))
            
            # Actualizar el color clasificado si la distancia actual es menor
            if distancia < distancia_minima:
                distancia_minima = distancia
                color_clasificado = nombre_color
        
        return color_clasificado

    def clasifyOnePixel(self, pixel):
        distancia_minima = float('inf')
        color_clasificado = None
        for nombre_color, valor_color in self.colors.items():
            # Calcular la distancia entre el pixel y el valor H del color
            distancia = min(abs(pixel[0] - valor_color), 360 - abs(pixel[0] - valor_color))
            
            # Actualizar el color clasificado si la distancia actual es menor
            if distancia < distancia_minima:
                distancia_minima = distancia
                color_clasificado = nombre_color

        return color_clasificado

    def setScreenCapture(self, screenCapture):
        self.screenCapture = screenCapture

    def convert(self, division = 9):
        #Obtenemos la imagen
        completeImage = self.screenCapture.getScreen()
        #Convertimos la imagen a un arreglo de numpy
        image = np.array(completeImage)

        #Convertimos la imagen a un arreglo de 9x9
        (imageLength, imagewidth, depth) = image.shape
        #Obtenemos el tamaño de cada cuadro
        divisionWidth = imageLength // division
        divisionLength = imagewidth // division
        #Creamos el arreglo de 9x9 que tendra la representación
        representationArray = np.zeros((division, division), dtype=np.int8)

        #Recorremos la imagen en los puntos medios de cada cuadro
        #Esta bien pero falta corregir un error de un candy que queda medio tapado por 
        #Un letrero
        plt.imshow(completeImage)
        plt.show()

        for i in range(9):
            for j in range(9):
                representationPixels = image[i*divisionWidth:(i+1)*divisionWidth, j*divisionLength+divisionLength//2:j*divisionLength+divisionLength//2+1]
                # plt.imshow(representationPixels)
                # plt.show()
                representationArray[i][j] +=  self.clasifyArray(representationPixels)
        return representationArray
    


if __name__ == "__main__":
    from ScreenCapture import ScreenCapture
    from Pointer import Pointer
    import tracemalloc
    tracemalloc.start()
    async def tarea1():
        await asyncio.create_subprocess_exec("xdg-open", "Game/OLHag1ofTsZg59.swf")
        await asyncio.sleep(1)
        pointer = Pointer()
        pointer.press("ctrl", "f")
        await asyncio.sleep(6)
        sc = ScreenCapture()
        c = Convertion(sc, umbral=0.9)
        array = c.convert()
        print(array)
        print(array.shape)
        for i in array:
            for j in i:
                if j == 1:
                    print("Amarillo", end=" ")
                elif j == 2:
                    print("Naranja", end=" ")
                elif j == 3:
                    print("Azul", end=" ")
                elif j == 4:
                    print("Verde", end=" ")
                elif j == 5:
                    print("Morado", end=" ")
                elif j == 6:
                    print("Rojo", end=" ")
            print()

    asyncio.run(tarea1())