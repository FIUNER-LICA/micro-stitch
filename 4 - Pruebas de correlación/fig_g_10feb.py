from cv2 import cv2
import numpy as np
from scipy import signal
from scipy.ndimage import correlate
import matplotlib.pyplot as plt



img = cv2.imread("FigurasGeom.tif") # 815 x 451

roi = cv2.imread("roi_fig.tif") #61 x 64
cv2.imwrite("roi1.png",roi)

w, h = roi.shape[:-1]
 
# Función que sirve para detectar si una imagen está contenida en otra
res = cv2.matchTemplate(img, roi, cv2.TM_CCOEFF_NORMED)
print (np.max(res), np.min(res))
# Umbral admitido
threshold = .99
 
# Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):  #  Cambiar columnas y filas
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (150, 150, 0), 1)
 
# Guardar el resultado
cv2.imwrite('result.png', img)

plt.imshow (res)

plt.show()