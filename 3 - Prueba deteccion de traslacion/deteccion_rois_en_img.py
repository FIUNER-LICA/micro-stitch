from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

#############importante, ndarray se configura en filas por columnas. en fiji es x,y, columnas por filas
img_1 = cv2.imread("union_tras_hor.jpg", cv2.IMREAD_ANYCOLOR)
img_2 = cv2.imread("img_3.jpg", cv2.IMREAD_ANYCOLOR)
roi = cv2.imread("roi_central.jpg", cv2.IMREAD_ANYCOLOR) #

h, w= roi.shape[:-1]

# h1, w1= img_1.shape[:-1]
# h2, w2= img_2.shape[:-1]

# print (h1, " ", h2, " ", w1, " ", w2)

img = img_1.copy()
roi1 = roi.copy()

# img [:,:,0]=img_1 [:,:,2]
# roi1 [:,:,0]=roi [:,:,2]
# img [:,:,2]=img_1 [:,:,0]
# roi1 [:,:,2]=roi [:,:,0]

img2 = img_2.copy()

# Función que sirve para detectar si una imagen está contenida en otra
res = cv2.matchTemplate(img, roi1, cv2.TM_CCOEFF_NORMED)        # Esta, va a ser dato, no hará falta matchear, ni buscar la posición de la máscara (ambas cosas son dato)
print (type (res), "clase del match template")
inicio = time.perf_counter() 
res2 = cv2.matchTemplate(img2, roi1, cv2.TM_CCOEFF_NORMED)      # Matchea con el nuevo roi (en este caso el roi es la mascara, e img2 es el nuevo frame)
fin = time.perf_counter()

#puedo buscar la localizacion de los puntos con la funcion cv2.minMaxLoc()
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#depende el parámetro que haya puesto busco la posicion del maximo o minimo
#para el parametro elegido tendria que buscar el maximo

                # # # # # # # # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res2)
# Umbral admitido
threshold = .9

# Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
loc = np.where(res >= threshold)                                #Estas coordenadas son dato, posicion de la máscara (mask que saco del frame anterior)
loc2 = np.where(res2 >= threshold)                              #si no se encuentra, loc queda vacío, por lo que el pt no puede definirse.

if loc[0].size > 0 :
    print (loc)# devuelve tupla(x,y)
    x1 = loc[0][0] #filas
    y1 = loc[1][0] #columnas
else:
    print ("null")
                # # # # # # # # # print (max_loc, "loc 2", type (max_loc))
if loc2[0].size > 0 :
    print (loc2, "loc 2")# devuelve tupla(x,y)
    x2 = loc2[0][0]
    y2 = loc2[1][0]
else:
    print ("null")
#Asumiendo que las loc me dan una tupla de un punto único, y no un margen (como podría pasar)
tras_x = x1-x2
tras_y =  y1-y2

print ("La figura se trasladó en x:", tras_x, "\nY en y:", tras_y)
print ("Positivo a la derecha, negativo a la izquierda, en y")

if tras_y!=0 and tras_x==0: #traslacion neta horizontal
    if tras_y>0:
        result = np.ndarray((img.shape[0],y1+img2.shape[1]-y2, img.shape[2]))
        boollayer = np.zeros((img.shape[0],y1+img2.shape[1]-y2),dtype=bool)     #sub-matriz de booleanos

        print (result.shape, img.shape, img2.shape)
        result[:,:y1,:] = img[:,:y1,:]
        result[:,y1:,:] = img2[:,y2:,:]
    else:
        result = np.ndarray((img.shape[0],y2+img.shape[1]-y1, img.shape[2]))
        print (result.shape, img.shape, img2.shape)
        result[:,:y2,:] = img2[:,:y2,:]
        result[:,y2:,:] = img[:,y1:,:]

if tras_x!=0 and tras_y==0: #traslacion neta vertical
    if tras_x>0:
        result = np.ndarray((x1+img2.shape[0]-x2,img2.shape[1], img.shape[2]))
        print (result.shape, img.shape, img2.shape)
        result[:x1,:,:] = img[:x1,:,:]
        result[x1:,:,:] = img2[x2:,:,:]
    else:
        result = np.ndarray((x2+img.shape[0]-x1,img.shape[1], img.shape[2]))
        print (result.shape, img.shape, img2.shape)
        result[:x2,:,:] = img2[:x2,:,:]
        result[x2:,:,:] = img[x1:,:,:]

if tras_y!=0 and tras_x!=0: #traslacion diagonal

    if tras_y>0:
        result = np.ndarray((img.shape[0],y1+img2.shape[1]-y2, img.shape[2]))
        print (result.shape, img.shape, img2.shape)
        # result[:,:img2.shape[1],:] = img[:,:img2.shape[1],:] #acomodar, hacer generico # hacer con ndarray de bool
    else:
        result = np.ndarray((img.shape[0],y2+img.shape[1]-y1, img.shape[2]))
        print (result.shape, img.shape, img2.shape)
        # result[:,result.shape[1]-img2.shape[1]:,:] = img[:,:,:] #hacer con ndarray de bool # se completa result despues de analizar desplazamiento en x
    
    if tras_x>0:
        #
        result.resize(x1+img2.shape[0]-x2,result.shape[1], 3)
        #
        # result = np.ndarray((x1+img2.shape[0]-x2,img2.shape[1], img.shape[2]))
        print (result.shape, img.shape, img2.shape)
        if tras_y>0:
            result[:img.shape[0],:img.shape[1],:] = img[:,:,:]
            result[result.shape[0]-img2.shape[0]:,result.shape[1]-img2.shape[1]:,:] = img2[:,:,:] #hacer con ndarray de bool
        else:
            result[:img.shape[0],result.shape[1]-img2.shape[1]:,:] = img[:,:,:]
            result[result.shape[0]-img2.shape[0]:,:img2.shape[1],:] = img2[:,:,:]
    else:
        #
        result.resize(x2+img.shape[0]-x1,result.shape[1], 3)
        #
        print (result.shape, img.shape, img2.shape)

        if tras_y>0:
            result[:img.shape[0],result.shape[1]-img2.shape[1]:,:] = img2[:,:,:] #hacer con ndarray de bool
            result[result.shape[0]-img2.shape[0]:,:img2.shape[1],:] = img[:,:img2.shape[1],:]
        else:
            result[result.shape[0]-img2.shape[0]:,result.shape[1]-img2.shape[1]:,:] = img[:,:,:]
            result[:img2.shape[0],:img2.shape[1],:] = img2[:,:,:]

cv2.imwrite('union_tras_hor.jpg', result)
rr = cv2.imread ('union_tras_hor.jpg')

print ("Tiempo detección de la máscara en la roi: ", float(fin-inicio))

# plt.imshow(rr[:,:,::-1])
plt.imshow(result.astype(int)[:,:,::-1])
plt.show()
# # # for pt in zip(*loc[::-1]):  
# # #     cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (150, 150, 0), 1)
# # # # Ver caso en que encuentra mas de 1 coincidencia.. 
# # # print (pt)

 
# # # # Guardar el resultado
# # # cv2.imwrite('result.png', img)

# # # plt.imshow (img)

# # # plt.show()