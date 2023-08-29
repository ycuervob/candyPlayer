import cv2
import numpy as np
import pyautogui

# Capturar la pantalla
screen = np.array(pyautogui.screenshot())

# Mostrar la imagen capturada
cv2.imshow("Screen", screen)
cv2.waitKey(0)
cv2.destroyAllWindows()
