import numpy as np
from Functions.astar_search import astar_search

# Classe agente
class Agent:

    multiplier = 60

    # Construtor No tiene estado objetivo porque no existe
    # un estado objetivo en el problema realmente
    def __init__(self, initial_state : np.ndarray):
        self.initial_state = initial_state

    # Define las acciones posibles dado una matriz de dulces
    # Devuelve una lista de tuplas con: (punto inicial, punto final, costo)
    def actions(self, matrixCandy : np.ndarray) -> list[((np.int8, np.int8), (np.int8, np.int8), np.int8)]:
        pass

    # Esta función recibe una matriz de dulces
    # Devuelve solo el costo de la matriz y la matriz resultante con gravedad porque ya se sabe que puntos se mueven
    def matrixValue(self, originalMatrix : np.ndarray, punto1 : (np.int8, np.int8), punto2 : (np.int8, np.int8), value : np.uint8 = 0) -> (np.int8, np.ndarray):
        matrixCandy = np.copy(originalMatrix)
        # Cambia los valores de la matriz a ver que mondá

        if value == 0:
            pivot = matrixCandy[punto1[0]][punto1[1]]
            matrixCandy[punto1[0]][punto1[1]] = matrixCandy[punto2[0]][punto2[1]]
            matrixCandy[punto2[0]][punto2[1]] = pivot
        
        # Se les resta uno para ir calculando si hay 3 o más dulces iguales, la matriz es cuadrada
        length = len(matrixCandy[0]) - 1 

        # Direcciones a buscar
        # Direcciones en las que buscar coincidencias
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),(-2, 0),(2, 0),(0, -2),(0, 2)]

        for i in range(1,length):
            for j in range(1,length):
                candy = matrixCandy[i][j]
                count = 0
                for di,dj in directions:
                    if i+di < 0 and i+di > length and j+dj < 0 and j+dj > length:
                        if candy == matrixCandy[i+di][j+dj]:
                            matrixCandy[i+di][j+dj] = 0x00
                            count += 1

                if count >= 3:
                    value += self.multiplier + (3-count)*self.multiplier
                    # Este simula el caso en el que caen 3 dulces en horizontal
                    self.aplicar_gravedad(matrixCandy)
                    # Se llama recursivamente para ver si hay más dulces de 3 o mas juntos
                    self.matrixValue(matrixCandy, 0, 0, value)
                    break
            else:
                continue
            break
        
        return value, matrixCandy
        

    # Esta función recibe una matriz de dulces con ceros y hace caer por gravedad los dulces
    def aplicar_gravedad(matrixCandy : np.ndarray):
        filas = len(matrixCandy)
        columnas = filas

        for col in range(columnas):
            # Crear una lista temporal para almacenar los valores no nulos de la columna actual
            valores_no_nulos = np.array([], dtype=np.int8)
            
            for fila in range(filas):
                if matrixCandy[fila][col] != 0x00:
                    valores_no_nulos = np.append(valores_no_nulos, matrixCandy[fila][col])

            # Llenar la columna con ceros
            for fila in range(filas):
                if fila < len(valores_no_nulos):
                    matrixCandy[fila][col] = valores_no_nulos[fila]
                else:
                    matrixCandy[fila][col] = 0


    # Devuelve una tupla de tuplas con: (punto inicial, punto final, costo)
    def compute(self, perception : str, matrixCandy : np.ndarray = None, punto1 : (np.int8, np.int8) = None, punto2 : (np.int8, np.int8) = None) -> ((np.int8, np.int8), (np.int8, np.int8), np.int8):
        if(perception == "a"):
            return self.actions(matrixCandy)
        elif(perception == "v"):
            return self.matrixValue(matrixCandy, punto1, punto2)
        elif(perception == "s"):
            actions = self.actions(matrixCandy)
            return max(actions, key=lambda x: x[2])
        else:
            return None


# Example usage
if(__name__ == "__main__"):
    agenteTest = Agent(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])) # Esto es solo un ejemplo esta no es la matriz real
    print("Solution:", agenteTest)
