class Player:
    """clase para realizar las interacciones con el juego.
    
    Metodos:
        
        -movimiento"""
    def __init__(self,pointer):
        self.pointer = pointer

    def movimiento(self,tuplas):
        """metodo para mover el mouse de acuerdo a un movimiento en matriz dado por el agente
        
        recibe: tuplas
            -tupla de la forma {(xi,yi),(xf,yf),valor}"""
        
        inicial = tuplas[0]
        final = tuplas[1]

        #valores quemados        
        x = 100
        y = 10
        width = 650
        height = 580
        scuareWidth = width/9
        scuareHeight = height/9

        xPixelI, yPixelI = inicial[0] * scuareWidth + x + scuareWidth/2 , inicial[1] * scuareHeight + y + scuareHeight/2
        xPixelF, yPixelF = final[0] * scuareWidth + x + scuareWidth/2 , final[1] * (height/9) + y + scuareHeight/2

        self.pointer.twoClickMove(xPixelI, yPixelI, xPixelF, yPixelF)