import numpy as np

# Classe agente
class Agent:

    multiplier = 60

    # Construtor No tiene estado objetivo porque no existe
    # un estado objetivo en el problema realmente
    def __init__(self, initial_state : np.ndarray):
        self.initial_state = initial_state
        self.espetialsCandys = set()

    # Define las acciones posibles dado una matriz de dulces
    # Devuelve una lista de tuplas con: (punto inicial, punto final, costo)
    def actions(self, matrixCandy : np.ndarray) -> list[((np.int8, np.int8), (np.int8, np.int8), np.int8)]:
        length = len(matrixCandy) #La matriz es cuadrada
        movements = []

        for i in range(1,length):  
            vectorH = matrixCandy[i-1]
            vectorH1 = matrixCandy[i]
            vectorV = matrixCandy[:,i-1]
            vectorV1 = matrixCandy[:,i]
            for j in range(length-2):
                caso1H, _ = self.sameCandy(vectorH1[j], vectorH[j+1], vectorH[j+2]) #Caso 1
                caso2H, _ = self.sameCandy(vectorH[j], vectorH1[j+1], vectorH[j+2]) #Caso 2
                caso3H, _ = self.sameCandy(vectorH[j], vectorH[j+1], vectorH1[j+2]) #Caso 3
                caso4H, _ = self.sameCandy(vectorH1[j], vectorH[j+1], vectorH1[j+2]) #Caso 4
                caso5H, _ = self.sameCandy(vectorH[j], vectorH1[j+1], vectorH1[j+2]) #Caso 5
                caso6H, _ = self.sameCandy(vectorH1[j], vectorH1[j+1], vectorH[j+2]) #Caso 6
                caso7H, _ = self.sameCandy(vectorH[j], vectorH1[j]) #Caso 7 y 8

                if caso1H:
                    movements.append(((i-1,j), (i,j), self.matrixValue(matrixCandy, (i-1,j), (i,j))[0]))
                if caso2H:
                    movements.append(((i-1,j+1), (i,j+1), self.matrixValue(matrixCandy, (i-1,j+1), (i,j+1))[0]))
                if caso3H:
                    movements.append(((i-1,j+2), (i,j+2), self.matrixValue(matrixCandy, (i-1,j+2), (i,j+2))[0]))
                if caso4H:
                    movements.append(((i-1,j+1), (i,j+1), self.matrixValue(matrixCandy, (i-1,j+1), (i,j+1))[0]))
                if caso5H:
                    movements.append(((i-1,j), (i,j), self.matrixValue(matrixCandy, (i-1,j), (i,j))[0]))
                if caso6H:
                    movements.append(((i-1,j+2), (i,j+2), self.matrixValue(matrixCandy, (i-1,j+2), (i,j+2))[0]))
                if caso7H:
                    if (i+2) < length:
                        if self.sameCandy(vectorH[j], matrixCandy[i+2][j])[0]:
                            movements.append(((i+1,j), (i+2,j), self.matrixValue(matrixCandy, (i+1,j), (i+2,j))[0]))
                    if (i-3) >= 0:
                        if self.sameCandy(vectorH[j], matrixCandy[i-3][j])[0]:
                            movements.append(((i-2,j), (i-3,j), self.matrixValue(matrixCandy, (i-2,j), (i-3,j))[0]))

                caso1V, _ = self.sameCandy(vectorV1[j], vectorV[j+1], vectorV[j+2]) #Caso 1
                caso2V, _ = self.sameCandy(vectorV[j], vectorV1[j+1], vectorV[j+2]) #Caso 2
                caso3V, _ = self.sameCandy(vectorV[j], vectorV[j+1], vectorV1[j+2]) #Caso 3
                caso4V, _ = self.sameCandy(vectorV1[j], vectorV[j+1], vectorV1[j+2]) #Caso 4
                caso5V, _ = self.sameCandy(vectorV[j], vectorV1[j+1], vectorV1[j+2]) #Caso 5
                caso6V, _ = self.sameCandy(vectorV1[j], vectorV1[j+1], vectorV[j+2]) #Caso 6
                caso7V, _ = self.sameCandy(vectorV[j], vectorV1[j]) #Caso 7 y 8

                if caso1V:
                    movements.append(((j,i-1), (j,i), self.matrixValue(matrixCandy, (j,i-1), (j,i))[0]))
                if caso2V:
                    movements.append(((j+1,i-1), (j+1,i), self.matrixValue(matrixCandy, (j+1,i-1), (j+1,i))[0]))
                if caso3V:
                    movements.append(((j+2,i-1), (j+2,i), self.matrixValue(matrixCandy, (j+2,i-1), (j+2,i))[0]))
                if caso4V:
                    movements.append(((j+1,i-1), (j+1,i), self.matrixValue(matrixCandy, (j+1,i-1), (j+1,i))[0]))
                if caso5V:
                    movements.append(((j,i-1), (j,i), self.matrixValue(matrixCandy, (j,i-1), (j,i))[0]))
                if caso6V:
                    movements.append(((j+2,i-1), (j+2,i), self.matrixValue(matrixCandy, (j+2,i-1), (j+2,i))[0]))
                if caso7V:
                    if (i+2) < length:
                        if self.sameCandy(vectorV[j], matrixCandy[j][i+2])[0]:
                            movements.append(((j,i+1), (j,i+2), self.matrixValue(matrixCandy, (j,i+1), (j,i+2))[0]))
                    if (i-3) >= 0:
                        if self.sameCandy(vectorV[j], matrixCandy[j][i-3])[0]:
                            movements.append(((j,i-2), (j,i-3), self.matrixValue(matrixCandy, (j,i-2), (j,i-3))[0]))

        return movements
        
    # Esta función recibe una matriz de dulces
    # Devuelve solo el costo de la matriz y la matriz resultante con gravedad porque ya se sabe que puntos se mueven
    def matrixValue(self, originalMatrix : np.ndarray, punto1 : (np.int8, np.int8), punto2 : (np.int8, np.int8), value : np.uint8 = 0) -> (np.int8, np.ndarray):
        matrixCandy = np.copy(originalMatrix)
        valueInit = value
        # Cambia los valores de la matriz a ver que mondá
        pointToChange = set()
        for point, color in self.espetialsCandys:
            if abs(matrixCandy[point[0]][point[1]]-color) != 0x09:
                pointToChange.add((point, color))
        self.espetialsCandys = self.espetialsCandys-pointToChange


        if value == 0:
            pivot = matrixCandy[punto1[0]][punto1[1]]
            matrixCandy[punto1[0]][punto1[1]] = matrixCandy[punto2[0]][punto2[1]]
            matrixCandy[punto2[0]][punto2[1]] = pivot
        
        # Se les resta uno para ir calculando si hay 3 o más dulces iguales, la matriz es cuadrada
        length = len(matrixCandy[0])

        for i in range(0,length):
            countH = set()
            countV = set()
            for j in range(2,length):    
                horizontalCandys = [matrixCandy[i][j-x] for x in range(4)]
                horizontalCandysPos = [(i,j-x) for x in range(4)]

                samecandyH, espetialCandyH = self.sameCandy(*horizontalCandys[0:3])     
                if samecandyH and matrixCandy[i][j] != 0x00:
                    countH.add(j)
                    countH.add(j-1)
                    countH.add(j-2)
                    if (j-3) >= 0:
                        if self.sameCandy(*horizontalCandys[2:4])[0]:
                            puntoEspetialCandy = punto1 if punto1 in horizontalCandysPos else punto2
                            self.espetialsCandys.add((puntoEspetialCandy, matrixCandy[puntoEspetialCandy[0]][puntoEspetialCandy[1]]+9))

                
                if samecandyH and espetialCandyH:
                    for k in range(length):
                        countH.add(k)
                
                verticalCandys = [matrixCandy[j-x][i] for x in range(4)]
                verticalCandysPos = [(j-x,i) for x in range(4)]

                samecandyV, espetialCandyV = self.sameCandy(*verticalCandys[0:3])
                if samecandyV and matrixCandy[j][i] != 0x00:
                    countV.add(j)
                    countV.add(j-1)
                    countV.add(j-2)
                    if (j-3) >= 0:
                        if self.sameCandy(*verticalCandys[2:4])[0]:
                            puntoEspetialCandy = punto1 if punto1 in verticalCandysPos else punto2
                            self.espetialsCandys.add((puntoEspetialCandy, matrixCandy[puntoEspetialCandy[0]][puntoEspetialCandy[1]]+9))

                if samecandyV and espetialCandyV:
                    for k in range(length):
                        countV.add(k)
            
            for k in countH:
                matrixCandy[i][k] = 0
                value += 1
        
            for k in countV:
                matrixCandy[k][i] = 0
                value += 1
                
        # Este simula el caso en el que caen 3 dulces en horizontal
        self.applyGravity(matrixCandy)
        # Se llama recursivamente para ver si hay más dulces de 3 o mas juntos
        if value > valueInit:
            value, matrixCandy = self.matrixValue(matrixCandy, (0,0), (0,0), value)

        return value, matrixCandy
    
    def sameCandy(self,*candies : np.int8):

        if 0x00 in candies:
            return False, False

        same = True
        primeCandy = False
        for candy in candies:
            if candy != candies[0] and abs(candy - candies[0]) != 0x09:
                same = False
            if abs(candy - candies[0]) == 0x09:
                primeCandy = True
        return same, primeCandy

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
            if len(actions) > 0:
                return max(actions, key=lambda x: x[2])
            return ((0,0), (0,0), 0)
        else:
            return None


# Example usage
if(__name__ == "__main__"):
    agenteTest = Agent(np.array([], dtype=np.int8)) # Esto es solo un ejemplo esta no es la matriz real
    # Ejemplo de matrix de 9x9 con una secuencia de 5 consecutivas
    matrix_ejemplo = np.zeros((9,9), dtype=np.int8)
    matrix_ejemplo[5][1] = 0x01
    matrix_ejemplo[2][1] = 0x01
    matrix_ejemplo[3][1] = 0x01

    matrix_ejemplo += [
    [3, 6, 5, 5, 3, 5, 6, 1, 1],
    [1, 6, 3, 6, 5, 1, 3, 5, 4],
    [2, 4, 1, 2, 4, 1, 5, 6, 3],
    [6, 1, 4, 3, 5, 3, 4, 6, 3],
    [5, 5, 3, 1, 6, 1, 3, 2, 4],
    [3, 1, 3, 5, 2, 2, 6, 6, 1],
    [3, 5, 6, 5, 1, 3, 6, 2, 4],
    [4, 6, 5, 2, 1, 5, 1, 5, 5],
    [4, 6, 5, 1, 6, 3, 1, 3, 6]]

    print(matrix_ejemplo)
    print(agenteTest.actions(matrix_ejemplo))

