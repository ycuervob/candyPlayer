# Agent

Contiene los archivos del agente que soluciona el problema de forma conceptual, tiene estados y usa algún algoritmo para encontrar la solucion a un problema con matrices.

# Game

Archivos del juego, solo hace falta servir su contenido estático para poder ver el juego en un navegador.

# Mondongo

Tiene los archivos necesarios para pasar al agente la información leída de la página web mapeada a una matriz que el agente pueda entender, también debe encargarse de ejecutar las acciones.

Para instalar requerimientos de python ejecutar:

```Shell
    sudo apt-get install scrot
    sudo apt-get install python3-tk python3-dev
    sudo apt install python3.10-venv
    python3 -m venv candyenv
    source candyenv/bin/activate
    pip install -r requirements.txt
    deactivate 
```

Para activar el ambiente donde se instalaron los requerimientos usar:

```Shell
    source candyenv/bin/activate
```

y para desactivarlo usar:

```Shell
    deactivate 
```