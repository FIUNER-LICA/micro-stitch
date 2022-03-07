from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

#############importante, ndarray se configura en filas por columnas. en fiji es x,y, columnas por filas

img_1 = cv2.imread("Prueba tiempo where-minmaxloc/muestra1.jpg", cv2.IMREAD_ANYCOLOR)
img_2 = cv2.imread("Prueba tiempo where-minmaxloc/muestra2.jpg", cv2.IMREAD_ANYCOLOR)
roi = cv2.imread("Prueba tiempo where-minmaxloc/roi.jpg", cv2.IMREAD_ANYCOLOR) #

img = img_1.copy()
roi1 = roi.copy()

img2 = img_2.copy()

time_w = np.array(0)
time_mml = np.array(0)

for i in range(1,100):
# Función que sirve para detectar si una imagen está contenida en otra
    res = cv2.matchTemplate(img, roi1, cv2.TM_CCOEFF_NORMED)
        # Esta, va a ser dato, no hará falta matchear, ni buscar la posición de la máscara (ambas cosas son dato)
    res2 = cv2.matchTemplate(img2, roi1, cv2.TM_CCOEFF_NORMED)
        # Matchea con el nuevo roi (en este caso el roi es la mascara, e img2 es el nuevo frame)

#puedo buscar la localizacion de los puntos con la funcion cv2.minMaxLoc()
    #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #depende el parámetro que haya puesto busco la posicion del maximo o minimo
    #para el parametro elegido tendria que buscar el maximo
                # # # # # # # # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res2)

# Umbral admitido
    threshold = .9

# Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
    loc = np.where(res >= threshold)                                
        #Estas coordenadas son dato, posicion de la máscara (mask que saco del frame anterior)
    
    inicio_w = time.perf_counter() 
    loc2 = np.where(res2 >= threshold)
        #si no se encuentra, loc queda vacío, por lo que el pt no puede definirse.
    fin_w = time.perf_counter()
    w = [fin_w -inicio_w]
    
    inicio_mml = time.perf_counter()
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res2)
    fin_mml = time.perf_counter()
    mml = [fin_mml - inicio_mml]

    time_w = np.append(time_w, w)
    time_mml = np.append(time_mml, mml)

media_w = np.mean(time_w[1:])
media_w = media_w*(np.ones(100))

media_mml = np.mean(time_mml[1:])
media_mml = media_mml*(np.ones(100))

fig, a = plt.subplots()
a.plot(time_w[1:],'r', label = 'np.where')
a.plot(time_mml[1:],'b', label = 'cv2.minMaxLoc')
a.plot(media_w,'black', label = 'media_w = {:.6f}'.format(media_w[1]))
a.plot(media_mml,'brown', label = 'media_mml = {:.6f}'.format(media_mml[1]))
a.set_xlabel ('n iterations')
a.set_ylabel ('Time (s)')
a.set_title('Comparison Time of Functions for 100 Iterations', fontsize =14 )
plt.legend(loc='upper right', fontsize = 8)
plt.margins(0.01,0.1)
plt.savefig('Prueba tiempo where-minmaxloc/Resultado.png', bbox_inches = 'tight')
plt.show()
