import pyautogui

# Mover el mouse a las coordenadas (x, y)
pyautogui.moveTo(1920, 0)

# Hacer clic en las coordenadas actuales del mouse
pyautogui.click()

# Obtener las coordenadas actuales del mouse
x, y = pyautogui.position()
print(f"Coordenadas actuales del mouse: ({x}, {y})")
