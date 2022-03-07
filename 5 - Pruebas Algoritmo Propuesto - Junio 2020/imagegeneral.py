from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

#############importante, ndarray se configura en filas por columnas. en fiji es x,y, columnas por filas
img_1 = cv2.imread("muestra1.jpg", cv2.IMREAD_ANYCOLOR)
img_2 = cv2.imread("union.jpg", cv2.IMREAD_ANYCOLOR)
roi = cv2.imread("roi.jpg", cv2.IMREAD_ANYCOLOR) #

h, w= roi.shape[:-1]

img = img_1.copy()
roi1 = roi.copy()

img2 = img_2.copy()
X = 0   #posición en la panorámica del ultimo frame, a partir del cual sacaria la máscara, es decir, la sacaría de X+x_mask --> que yo se el ancho del roi/frame 1024
Y = 0
panoramica = img_1.copy()
# Función que sirve para detectar si una imagen está contenida en otra
res = cv2.matchTemplate(img, roi1, cv2.TM_CCOEFF_NORMED)        # Esta, va a ser dato, no hará falta matchear, ni buscar la posición de la máscara (ambas cosas son dato)
print (type (res), "clase del match template")
inicio = time.perf_counter() 
res2 = cv2.matchTemplate(img2, roi1, cv2.TM_CCOEFF_NORMED)      # Matchea con el nuevo roi (en este caso el roi es la mascara, e img2 es el nuevo frame)
fin = time.perf_counter()
print ("TIEMPOO", fin-inicio)

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
a = np.zeros (3)
boollayer = np.ones((img.shape[0],img.shape[1]),dtype=bool)     #sub-matriz de booleanos
print (boollayer[0][0])

plt.imshow(boollayer)
plt.show()


if tras_y!=0 and tras_x==0: #traslacion neta horizontal
    if tras_y>0:
        result = np.ndarray((img.shape[0],y1+img2.shape[1]-y2, img.shape[2]))

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
        #Redimencionamiento de la matriz de bool en y (horizontal)
        if boollayer.shape[1]<(y1+img2.shape[1]-y2):
            aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
            boollayer.resize (boollayer.shape[0],y1+img2.shape[1]-y2) ####
            boollayer[:,:]=False
            boollayer[:,:aux.shape[1]] = aux[:,:]
            print (aux.shape[1])

            plt.imshow(boollayer)
            plt.show()
        #hacer un else que complete con los nuevos datos si no debe crecer en y.. capaz mas abajo directamente
        print (result.shape, img.shape, img2.shape)
    else:
        result = np.ndarray((img.shape[0],y2+img.shape[1]-y1, img.shape[2]))
        
        if boollayer.shape[1]<(y2+img.shape[1]-y1):
            aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
            boollayer.resize (boollayer.shape[0],y2+img.shape[1]-y1) ####
            boollayer[:,:]=False
            boollayer[:,y2-y1:] = aux[:,:]
            print (aux.shape[1])


            plt.imshow(boollayer)
            plt.show()

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
###
        if boollayer.shape[0]<(x1+img2.shape[0]-x2):
            aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
            boollayer.resize (x1+img2.shape[0]-x2,boollayer.shape[1]) ####
            boollayer[:,:]=False
            boollayer[:aux.shape[0],:] = aux[:,:]
            print (aux.shape[0])

            plt.imshow(boollayer)
            plt.show()

    else:
        #
        result.resize(x2+img.shape[0]-x1,result.shape[1], 3)
        #
###
        if boollayer.shape[0]<(x2+img.shape[0]-x1):
            aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
            boollayer.resize (x2+img.shape[0]-x1,boollayer.shape[1]) ####
            boollayer[:,:]=False
            boollayer[x2-x1:,:] = aux[:,:]
            print (aux.shape[0])
            print (boollayer.shape[0])

            plt.imshow(boollayer)
            plt.show()
        print (result.shape, img.shape, img2.shape)

        if tras_y>0:
            result[:img.shape[0],result.shape[1]-img2.shape[1]:,:] = img2[:,:,:] #hacer con ndarray de bool
            result[result.shape[0]-img.shape[0]:,:img2.shape[1],:] = img[:,:img2.shape[1],:]
        else:
            result[result.shape[0]-img.shape[0]:,result.shape[1]-img2.shape[1]:,:] = img[:,:,:]
            result[:img2.shape[0],:img2.shape[1],:] = img2[:,:,:]

        #Completo con 1 la matriz de bool, y en paralelo agrando y copio los datos en la panoramica   
    boollayer_1 = boollayer.copy()
    aux_pano = panoramica.copy()
    if tras_x>0:
        if tras_y>0:
            boollayer [X+tras_x:X+img2.shape[0],Y+img2.shape[1]:Y+img2.shape[1]+tras_y] = True
            boollayer [X+img2.shape[0]:,Y+tras_y:Y+tras_y+img2.shape[1]] = True
            # plt.imshow(boollayer)
            # plt.show()
            #agrando panoramica
            panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
            panoramica [:,:,:] = 0
            #vuelvo a ponerle los valores antes del resize
            panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
            # plt.imshow(panoramica)
            # plt.show()
            aux = (boollayer_1^boollayer)
            # plt.imshow(aux)
            # plt.show()
            
            
            
            l = 0; m = 0
            # inicio = time.perf_counter() 
            for i in range (0,aux.shape[0]):
                for j in range (0,aux.shape[1]):
                    if (tras_x <= i) & (tras_y<=j):
                        if aux[i,j]:
                            panoramica[i,j,:]=img2[m,l,:]
                        if l==img2.shape[1]-1:
                            l=0
                            m = m+1
                        else: l = l+1
            # fin = time.perf_counter() 

            plt.imshow(aux)
            plt.show()

plt.imshow(panoramica)
plt.show()

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

img_1 = cv2.imread("union_tras_hor.jpg", cv2.IMREAD_ANYCOLOR)
