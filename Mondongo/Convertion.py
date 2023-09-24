from ScreenCapture import ScreenCapture
from Pointer import Pointer
import numpy as np
import webbrowser
import asyncio
import matplotlib.pyplot as plt

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
    
    def __init__(self, screenCapture: ScreenCapture):
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
        #Creamos un arreglo 9x9 que tendrá los colores de cada dulce en la matriz
        representativeColor = np.zeros((9,9,3), dtype=np.uint8)

        #Recorremos la imagen en los puntos medios de cada cuadro
        #Esta bien pero falta corregir un error de un candy que queda medio tapado por 
        #Un letrero
        for i in range(9):
            for j in range(9):
                representationPixel = image[i * divisionLength + divisionLength // 2][j * divisionWidth + divisionWidth // 2]
                print(representationPixel)
                for k in range(3):
                    representativeColor[i][j][k] += representationPixel[k]
            #Correccion de dulce por tapado 
        for k in range(3):
            representativeColor[0][3][k] = image[divisionLength // 2][(3 * divisionWidth + divisionWidth // 2)-10][k]

        return representativeColor
    
async def tarea1():
    asyncio.create_subprocess_exec("make", "start")
    await asyncio.sleep(2)
    webbrowser.open("http://127.0.0.1:3006")
    await asyncio.sleep(2)
    pointer = Pointer()
    pointer.moveAndClick(750, 350)
    await asyncio.sleep(30)
    sc = ScreenCapture()
    c = Convertion(sc)
    array = c.convert()
    print(array)
    print(array.shape)
    for i in range(9):
        for j in range(9):
            mostrar_color_rgb(tuple(x/255 for x in array[i][j]))

if __name__ == "__main__":
    asyncio.run(tarea1())