from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("imagenes_tigre.jpg", cv2.IMREAD_ANYCOLOR) # 815 x 451

roi2 = cv2.imread("Clipboard.png", cv2.IMREAD_ANYCOLOR) #61 x 64
# Corrección lectura a RGB
img = img1.copy()
roi = roi2.copy()

img [:,:,0]=img1 [:,:,2]
roi [:,:,0]=roi2 [:,:,2]
img [:,:,2]=img1 [:,:,0]
roi [:,:,2]=roi2 [:,:,0]
# #
h, w = roi.shape[:-1]

# Función que sirve para detectar si una imagen está contenida en otra
res = cv2.matchTemplate(img, roi, cv2.TM_CCOEFF_NORMED)
print (type (res))

# Umbral admitido
threshold = .9

# Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
loc = np.where(res >= threshold) #si no se encuentra, loc queda vacío, por lo que pt no puede definirse.
print (loc)
if loc[0].size > 0 & loc[1].size:
    print (loc)
else:
    print ("null")
print ("medida", w, h)
for pt in zip(*loc[::-1]):  #  Cambiar columnas y filas
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (150, 150, 0), 1)
# Ver caso en que encuentra mas de 1 coincidencia.. 
print (pt)

 
# Guardar el resultado
cv2.imwrite('result.png', img)

plt.imshow (img)

plt.show()

# plotea bien porque se cambió el RGB a BGR, para el mtpl. y lo guarda "mal" porque CV2 tiene formato RGB. al revés de mplt.