import numpy as np
from Functions.astar_search import astar_search

# Classe agente
class Agent:

    # Construtor No tiene estado objetivo porque no existe
    # un estado objetivo en el problema realmente
    def __init__(self, initial_state : np.ndarray):
        self.initial_state = initial_state

    # Define las acciones posibles dado una matriz de dulces
    def actions(self, state : np.ndarray, matrixCandy : np.ndarray):
        pass

    # Define una heuristica o funcion que maximize el resultado
    # Esta función recibe una matriz de dulces y devuelve un valor con el consto y las posiciones de los dulces a mover para el máximo
    # de esa sola matriz
    def matrixValue(self, matrixCandy : np.ndarray):
        pass

    # Devuelve el movimiento que debe realizar el agente pos x e y
    def compute(self, perception : np.ndarray):
        return astar_search(self.initial_state, self.goal_state, self.actions, self.heuristic)

# Example usage

if(__name__ == "__main__"):
    agenteTest = Agent(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
    print("Solution:", agenteTest)
