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

        num_agentes = min(len(acciones), 5)

        #top 5 acciones en O(n + k log k)
        top_indices = np.argpartition(acciones[:, -1], -5)[-num_agentes:]

        mejoresAcciones = acciones[top_indices]

        #euristica

        #TODO paralelizarlo
        agentes = [Agent(np.array([], dtype=np.int8)) for x in range(num_agentes)]

        matrices = [agentes[i].matrixValue(matriz,mejoresAcciones[i][0],mejoresAcciones[i][1])[1] for i in range(len(agentes))]

        euristica = [agentes[i].compute("s",matrices[i])[2] for i in range(len(agentes))]
        
        # mejor movimiento de acuerdo a la euristica
        arr1 = np.array([mejoresAcciones[i][2] for i in range(len(agentes))])

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