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
    await asyncio.sleep(2)
    pointer = Pointer()
    pointer.moveAndClick(750, 350)
    sc = ScreenCapture()
    c = Convertion(sc, umbral=0.90)
    a = Agent(np.array([], dtype=np.int8))
    p = Player(pointer)
    prevMatrix = np.array([], dtype=np.int8)
    currMatrix = np.array([], dtype=np.int8)

    return c,a,p,sc,currMatrix

async def play():
    c,a,p,sc,currMatrix = await init()

    i = 0
    mejoresAcciones = []
    mejorMovimiento = ((0,0),(0,0),0)
    mejorMovimientoPrevio = ((0,0),(0,0),0)
    while i < 1000:
        #conseguir acciones desde la pantalla
        sc.setScreen()
        currMatrix = c.convert()

        acciones = a.actions(currMatrix)
        acciones = np.array(acciones, dtype=object)
        
        #si no hay acciones  se vuelve a probar a calcular las acciones
        if len(acciones) == 0:
            continue

        num_agentes = min(len(acciones), 5)

        #top 5 acciones en O(n + k log k)
        top_indices = np.argpartition(acciones[:, -1], -num_agentes)[-5:]

        mejoresAcciones = acciones[top_indices]

        #euristica
        matrices = [a.matrixValue(currMatrix,mejoresAcciones[i][0],mejoresAcciones[i][1])[1] for i in range(num_agentes)]
        euristica = [a.compute("s",matrices[i])[2] for i in range(num_agentes)]
        
        # mejor movimiento de acuerdo a la euristica
        arr1 = np.array([mejoresAcciones[i][2] for i in range(num_agentes)])
        arr2 = np.array(euristica)
        arr3 = [[mejoresAcciones[i][1][0] for i in range(num_agentes)]]
        resultado = arr1 + arr2 + arr3

        mejorMovimiento = np.argmax(resultado)
        if mejorMovimientoPrevio[0] == mejoresAcciones[mejorMovimiento][0] and mejorMovimientoPrevio[1] == mejoresAcciones[mejorMovimiento][1]:
            newmejorMovimiento = np.delete(resultado,  mejorMovimiento)
            otroMejor = np.argmax(newmejorMovimiento)
            p.movimiento(mejoresAcciones[otroMejor])
        else:
            p.movimiento(mejoresAcciones[mejorMovimiento])

        mejorMovimientoPrevio = mejoresAcciones[mejorMovimiento]
        i+=1

async def main():
    await play()

if __name__ == "__main__":
    asyncio.run(main())