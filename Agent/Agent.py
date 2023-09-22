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
        valueInit = value
        # Cambia los valores de la matriz a ver que mondá

        if value == 0:
            pivot = matrixCandy[punto1[0]][punto1[1]]
            matrixCandy[punto1[0]][punto1[1]] = matrixCandy[punto2[0]][punto2[1]]
            matrixCandy[punto2[0]][punto2[1]] = pivot
        
        # Se les resta uno para ir calculando si hay 3 o más dulces iguales, la matriz es cuadrada
        length = len(matrixCandy[0])

        for i in range(0,length):
            countH = set()
            countV = set()
            for j in range(1,length):
                if matrixCandy[i][j] == matrixCandy[i][j-1] and matrixCandy[i][j] == matrixCandy[i][j-2] and matrixCandy[i][j] != 0x00:
                    countH.add(j)
                    countH.add(j-1)
                    countH.add(j-2)
                    
                if matrixCandy[j][i] == matrixCandy[j-1][i] and matrixCandy[j][i] == matrixCandy[j-2][i] and matrixCandy[j][i] != 0x00:
                    countV.add(j)
                    countV.add(j-1)
                    countV.add(j-2)
            
            for k in countH:
                matrixCandy[i][k] = 0
                value += 1
        
            for k in countV:
                matrixCandy[k][i] = 0
                value += 1

        # Este simula el caso en el que caen 3 dulces en horizontal
        self.applyGravity(matrixCandy)
        # Se llama recursivamente para ver si hay más dulces de 3 o mas juntos
        print(matrixCandy)
        print(valueInit//3)
        print(value//3)

        if value > valueInit:
            self.matrixValue(matrixCandy, (0,0), (0,0), value)

        
        
        return value//3, matrixCandy

    # Esta función recibe una matriz de dulces con ceros y hace caer por gravedad los dulces
    def applyGravity(self, matrixCandy : np.ndarray):
        row = len(matrixCandy)
        column = row

        for col in range(column):
            # Crear una lista temporal para almacenar los valores no nulos de la columna actual
            notNullValues = np.array([], dtype=np.int8)
            
            for r in range(row):
                if matrixCandy[r][col] != 0x00:
                    notNullValues = np.append(notNullValues, matrixCandy[r][col])

            # Llenar la columna con ceros
            for k in range(row):
                if k < len(notNullValues):
                    matrixCandy[row-k-1][col] = notNullValues[k]
                else:
                    matrixCandy[row-k-1][col] = 0x00


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
    agenteTest = Agent(np.array([], dtype=np.uint8)) # Esto es solo un ejemplo esta no es la matriz real
    # Ejemplo de matrix de 9x9 con una secuencia de 5 consecutivas
    matrix_ejemplo = np.array([
        [1, 3, 1, 2, 2, 2, 2, 2, 2],
        [4, 4, 4, 5, 5, 5, 4, 5, 5],
        [7, 7, 7, 8, 8, 8, 8, 8, 8],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 1, 1, 2, 2, 2, 3, 3, 3],
        [4, 4, 4, 5, 5, 5, 6, 6, 6],
        [7, 7, 7, 8, 8, 8, 9, 9, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ], dtype=np.uint8)

    print(matrix_ejemplo)
    agenteTest.matrixValue(matrix_ejemplo, (0,0), (0,0))

    print("Solution:", agenteTest)
