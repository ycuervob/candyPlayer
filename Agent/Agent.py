import numpy as np
from Functions.astar_search import astar_search

# Classe agente
class Agent:

    # Construtor No tiene estado objetivo porque no existe
    # un estado objetivo en el problema realmente
    def __init__(self, initial_state : np.ndarray):
        self.initial_state = initial_state

    # Define las acciones posibles dado una matriz de dulces
    # Devuelve una lista de tuplas con: (punto inicial, punto final, costo, matriz resultante)
    def actions(self, matrixCandy : np.ndarray) -> list[((np.int8, np.int8), (np.int8, np.int8), np.int8, np.ndarray)]:
        pass

    # Esta función recibe una matriz de dulces
    # Devuelve una lista de tuplas con: (punto inicial, punto final, costo)
    def matrixValue(self, matrixCandy : np.ndarray, punto1 : (np.int8, np.int8), punto2 : (np.int8, np.int8)) -> [(np.int8, np.int8), (np.int8, np.int8), np.int8]:
        pass

    # Devuelve una tupla de tuplas con: (punto inicial, punto final, costo)
    def compute(self, perception : str, matrixCandy : np.ndarray = None) -> ((np.int8, np.int8), (np.int8, np.int8), np.int8):
        if(perception == "a"):
            return self.actions(matrixCandy)
        elif(perception == "v"):
            return self.matrixValue(matrixCandy)
        elif(perception == "s"):
            actions = self.actions(matrixCandy)
            return max(actions, key=lambda x: x[2])
        else:
            return None


# Example usage
if(__name__ == "__main__"):
    agenteTest = Agent(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])) # Esto es solo un ejemplo esta no es la matriz real
    print("Solution:", agenteTest)
