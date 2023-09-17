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
    def actions(self, matrixCandy : np.ndarray) -> list[((int, int), (int, int), int, np.ndarray)]:
        pass

    # Esta función recibe una matriz de dulces
    # Devuelve una lista de tuplas con: (punto inicial, punto final, costo)
    def matrixValue(self, matrixCandy : np.ndarray) -> [(int, int), (int, int), int]:
        pass

    # Devuelve una tupla de tuplas con: (punto inicial, punto final, costo)
    def compute(self, perception : str, matrixCandy : np.ndarray = None) -> ((int, int), (int, int), int):
        return astar_search(self.initial_state, self.goal_state, self.actions, self.heuristic)

# Example usage

if(__name__ == "__main__"):
    agenteTest = Agent(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])) # Esto es solo un ejemplo esta no es la matriz real
    print("Solution:", agenteTest)
