import pyautogui

#Clase pointer para mover el mouse
class pointer:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        
    def move(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        pyautogui.moveTo(self.pos)
        
    def click(self):
        pyautogui.click(self.pos)
    
    def twoClickMove(self, x, y, x2, y2):
        self.move(x, y)
        self.click()
        self.move(x2, y2)
        self.click()

    def getPos(self):
        return self.pos
    

#Test de class
if __name__ == "__main__":
    p = pointer()
    p.move(100, 100)
    p.click()
    p.move(200, 200)
    p.click()
    p.twoClickMove(300, 300, 400, 400)
    print(p.getPos())
