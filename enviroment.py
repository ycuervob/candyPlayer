from Mondongo.Convertion import Convertion
from Mondongo.Player import Player
from Mondongo.ScreenCapture import ScreenCapture
from Mondongo.Pointer import Pointer
from Agent.Agent import Agent

import webbrowser
import asyncio
import numpy as np

async def init():
    await asyncio.create_subprocess_exec("http-server", "Game", "-p", "3006")
    webbrowser.open("http://127.0.0.1:3006")
    await asyncio.sleep(5)
    pointer = Pointer()
    pointer.moveAndClick(750, 350)
    await asyncio.sleep(25)
    sc = ScreenCapture()
    c = Convertion(sc, umbral=0.9)
    a = Agent(np.array([], dtype=np.int8))
    p = Player(pointer)

    return c,a,p, sc

async def play():
    c,a,p,sc = await init()

    i = 0
    while i < 20:
        #conseguir acciones desde la pantalla
        matriz = c.convert()
        acciones = a.actions(matriz)
        acciones = np.array(acciones, dtype=object)

        #top 5 acciones en O(n + k log k)
        top_indices = np.argpartition(acciones[:, -1], -5)[-5:]

        mejoresAcciones = acciones[top_indices]

        #euristica

        #TODO paralelizarlo
        a1 = Agent(np.array([], dtype=np.int8))
        a2 = Agent(np.array([], dtype=np.int8))
        a3 = Agent(np.array([], dtype=np.int8))
        a4 = Agent(np.array([], dtype=np.int8))
        a5 = Agent(np.array([], dtype=np.int8))

        matriz1 = a1.matrixValue(matriz,mejoresAcciones[0][0],mejoresAcciones[0][1])[1]
        matriz2 = a2.matrixValue(matriz,mejoresAcciones[1][0],mejoresAcciones[1][1])[1]
        matriz3 = a3.matrixValue(matriz,mejoresAcciones[2][0],mejoresAcciones[2][1])[1]
        matriz4 = a4.matrixValue(matriz,mejoresAcciones[3][0],mejoresAcciones[3][1])[1]
        matriz5 = a5.matrixValue(matriz,mejoresAcciones[4][0],mejoresAcciones[4][1])[1]

        euristica = [
            a1.compute("s",matriz1)[2],
            a2.compute("s",matriz2)[2],
            a3.compute("s",matriz3)[2],
            a4.compute("s",matriz4)[2],
            a5.compute("s",matriz5)[2],
            ]
        
        # mejor movimiento de acuerdo a la euristica
        arr1 = np.array([
            mejoresAcciones[0][2],
            mejoresAcciones[1][2],
            mejoresAcciones[2][2],
            mejoresAcciones[3][2],
            mejoresAcciones[4][2],
        ])

        arr2 = np.array(euristica)
        resultado = arr1 + arr2

        mejorMovimiento = np.argmax(resultado)
        print("mejorMovimiento:", mejoresAcciones[mejorMovimiento])
        p.movimiento(mejoresAcciones[mejorMovimiento])
        i+=1

        sc.setScreen()

async def main():
    await play()

if __name__ == "__main__":
    asyncio.run(main())