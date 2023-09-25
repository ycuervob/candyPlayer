from Agent.Agent import Agent
from Mondongo.Convertion import Convertion
from Mondongo.Player import Player
from Mondongo.Pointer import Pointer
from Mondongo.ScreenCapture import ScreenCapture
import keyboard

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

    #conseguir acciones desde la pantalla
    sol = a.compute("s", c.convert())
    print(sol)
    #ejecutar acciones
    p.movimiento(sol)

asyncio.run(play())