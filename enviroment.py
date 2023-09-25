from Agent.Agent import Agent
from Mondongo.Convertion import Convertion
from Mondongo.Player import Player
from Mondongo.Pointer import Pointer
from Mondongo.ScreenCapture import ScreenCapture

import webbrowser
import asyncio
import numpy as np

c = None
a = None
p = None

async def init():
    global c, a, p
    await asyncio.create_subprocess_exec("http-server", "Game", "-p", "3006")
    webbrowser.open("http://127.0.0.1:3006")
    await asyncio.sleep(2)
    pointer = Pointer()
    pointer.moveAndClick(750, 350)
    await asyncio.sleep(26)
    sc = ScreenCapture()
    c = Convertion(sc, umbral=0.9)
    a = Agent(np.array([], dtype=np.int8))
    p = Player(pointer)

async def play():
    await init()
    global c, a, p

    while True:
        #conseguir acciones desde la pantalla
        acciones = a.actions(c.convert())
        print(acciones)

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

        euristica = [
            a1.compute("s",mejoresAcciones[0])[2],
            a2.compute("s",mejoresAcciones[1])[2],
            a3.compute("s",mejoresAcciones[2])[2],
            a4.compute("s",mejoresAcciones[3])[2],
            a5.compute("s",mejoresAcciones[4])[2],
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

        p.movimiento(mejoresAcciones[mejorMovimiento])

asyncio.run(play())