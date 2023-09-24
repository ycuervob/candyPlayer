from ScreenCapture import ScreenCapture
from Pointer import Pointer
import numpy as np
import webbrowser
import asyncio
import matplotlib.pyplot as plt
import cv2

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

    def __init__(self, screenCapture: ScreenCapture, baseRoute =  "Mondongo/imgCandy/", umbral = 0.95):
        self.screenCapture = screenCapture
        self.colors = {
            0x01: (255, 255, 0),    #amarillo
            0x02: (255, 150, 0),    #naranja
            0x03: (0, 0, 255),      #azul
            0x04: (0, 255, 0),      #verde
            0x05: (255, 0, 255),    #morado
            0x06: (255, 0, 0)       #rojo
        }
        self.umbral = umbral
        self.arraytypes = np.array(["", "E", "E1", "E2"])
        self.arrayAmarillos = [cv2.cvtColor(cv2.imread(baseRoute + "amarillo/amarillo"+ types +".png") , cv2.COLOR_BGR2GRAY) for types in self.arraytypes]
        self.arrayNaranjas = [cv2.cvtColor(cv2.imread(baseRoute + "naranja/naranja"+ types +".png"), cv2.COLOR_BGR2GRAY) for types in self.arraytypes]
        self.arrayAzules = [cv2.cvtColor(cv2.imread(baseRoute + "azul/azul"+ types +".png"), cv2.COLOR_BGR2GRAY) for types in self.arraytypes]
        self.arrayVerdes = [cv2.cvtColor(cv2.imread(baseRoute + "verde/verde"+ types +".png"), cv2.COLOR_BGR2GRAY) for types in self.arraytypes]
        self.arrayMorados = [cv2.cvtColor(cv2.imread(baseRoute + "morado/morado"+ types +".png"), cv2.COLOR_BGR2GRAY) for types in self.arraytypes]
        self.arrayRojos = [cv2.cvtColor(cv2.imread(baseRoute + "rojo/rojo"+ types +".png"), cv2.COLOR_BGR2GRAY) for types in self.arraytypes]
        self.arrayCandy = [self.arrayAmarillos, self.arrayNaranjas, self.arrayAzules, self.arrayVerdes, self.arrayMorados, self.arrayRojos]

    def clasificarColorBasic(self, pixel):
        distancia_minima = float('inf')
        color_clasificado = None

        for nombre_color, valor_color in self.colors.items():
            # Calcular la distancia euclidiana entre el pixel y el valor RGB del color
            distancia = np.sqrt(sum(np.power(np.array(pixel) - np.array(valor_color),2)))
            
            # Actualizar el color clasificado si la distancia actual es menor
            if distancia < distancia_minima:
                distancia_minima = distancia
                color_clasificado = nombre_color

        return color_clasificado

    def setScreenCapture(self, screenCapture: ScreenCapture):
        self.screenCapture = screenCapture

    def convert(self, division = 9):
        #Obtenemos la imagen
        image = self.screenCapture.getScreen()
        #Convertimos la imagen a un arreglo de numpy
        image = np.array(image)

        #Convertimos la imagen a un arreglo de 9x9
        (imageLength, imagewidth, depth) = image.shape
        #Obtenemos el tamaño de cada cuadro
        divisionLength = imageLength // division
        divisionWidth = imagewidth // division
        #Creamos el arreglo de 9x9 que tendra la representación
        representationArray = np.zeros((division, division), dtype=np.int8)
        #Creamos un arreglo 9x9 que tendrá los colors de cada dulce en la matriz
        representativeColor = np.zeros((9,9,3), dtype=np.uint8)

        #Recorremos la imagen en los puntos medios de cada cuadro
        #Esta bien pero falta corregir un error de un candy que queda medio tapado por 
        #Un letrero
        for i in range(9):
            for j in range(9):
                representationPixel = image[i * divisionLength + divisionLength // 2][j * divisionWidth + divisionWidth // 2]
                for k in range(3):
                    representativeColor[i][j][k] += representationPixel[k]
        #Correccion de dulce por tapado 
        for k in range(3):
            representativeColor[0][3][k] = image[divisionLength // 2][(3 * divisionWidth + divisionWidth // 2)-10][k]

        #Clasificamos los colores basicamente
        for i in range(9):
            for j in range(9):
                representationArray[i][j] = self.clasificarColorBasic(representativeColor[i][j])

        #Clasificamos los colores de los dulces mas especificamente usando openCV
        for i in range(9):
            for j in range(9):
                candysOfSameColor = self.arrayCandy[representationArray[i][j]-1]
                for candy in candysOfSameColor:
                    histCandy = cv2.calcHist([candy], [0], None, [256], [0, 256])
                    histImage = cv2.calcHist([image[i * divisionLength: (i + 1) * divisionLength, j * divisionWidth: (j + 1) * divisionWidth]], [0], None, [256], [0, 256])
                    simliarity = cv2.compareHist(histCandy, histImage, cv2.HISTCMP_CORREL)
                    if simliarity > self.umbral and candysOfSameColor.index(candy) > 0:
                        representationArray[i][j] += 9
                        break
                    

        return representationArray
    
async def tarea1():
    asyncio.create_subprocess_exec("make", "start")
    await asyncio.sleep(5)
    webbrowser.open("http://127.0.0.1:3006")
    await asyncio.sleep(5)
    pointer = Pointer()
    pointer.moveAndClick(750, 350)
    await asyncio.sleep(30)
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

if __name__ == "__main__":
    asyncio.run(tarea1())