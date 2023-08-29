# Agent

Contiene los archivos del agente que soluciona el problema de forma conceptual, tiene estados y usa algún algoritmo como A* para encontrar la solucion a un problema con matrices.

# Game

Archivos del juego, solo hace falta servir su contenido estático para poder ver el juego en un navegador.

# Mondongo

Tiene los archivos necesarios para pasar al agente la información leída de la página web mapeada a una matriz que el agente pueda entender, también debe encargarse de ejecutar las acciones.

Para instalar requerimientos de python ejecutar:

```Shell
    apt install python3.10-venv
    python3 -m venv Mondongo/candyenv
    source Mondongo/candyenv/bin/activate
    pip install -r Mondongo/python/requirements.txt
    deactivate 
```