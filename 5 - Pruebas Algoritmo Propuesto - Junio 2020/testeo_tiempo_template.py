from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
from Funciones import funPano, funMatch#, ssim

img_in = funMatch.carga_img()
last_frame = img_in[0].copy()
panoramica = img_in[0].copy()
x1=int(last_frame.shape[0]/2)
y1=int(last_frame.shape[1]/2)
X = 0
Y = 0

vec = []
vec2 = []
vec3 = []
cont = 0
c = 100
m = 6
M = 130

# c repeticiones de generación de panorámica variando la máscara de m a M
for k in range(c):
    vec2=[]
    vec=[]
    cont = 0
    for r in range(m,M,5):
        cont = cont+1
        for new_frame in img_in[1:]: #hacer arreglo de imagenes y simular que va leyendo los nuevos frames

            inicio = time.perf_counter()

            mask = last_frame[x1:x1+r,y1:y1+r,:]            
            x2,y2,max_val = funMatch.MatchMask (new_frame,mask)

            tras_x = x1-x2
            tras_y = y1-y2
            pos1_2 = [x1,x2,y1,y2]

            panoramica = funPano.pano(panoramica, last_frame, new_frame, tras_x, tras_y, X, Y, pos1_2)
            last_frame = new_frame

            if (X+tras_x)>=0:
                X=X+tras_x
            else: X=0
            if (Y+tras_y)>=0:
                Y=Y+tras_y
            else: Y=0

            fin= time.perf_counter()

        s= fin - inicio
        vec = vec+[r]
        vec2 = vec2+[s]
        # cv2.imwrite('./Img_Resultados/sizeMask/PANORAMICA_{}.jpg'.format(r), panoramica)
        panoramica = []
        panoramica = img_in[0].copy()
        last_frame = img_in[0].copy()
        x1=int(last_frame.shape[0]/2)
        y1=int(last_frame.shape[1]/2)
        X = 0
        Y = 0
    vec3.append(vec2)


t= np.array(vec3).reshape(c,cont)

h = np.mean(t, axis=0)

archivo = open("./Testeo de tiempo de template/Tabla tamaño vs tiempo.txt", 'w')
archivo.write("Tamaño de máscara \t Tiempo promedio ({} rep)\r\r".format(c))
for i in range(0,len(vec),int(len(vec)/10)):
    archivo.write(str(vec[i])+"\t")
    archivo.write(str(h[i]))
    archivo.write("\r")
archivo.close()

archivo = open("./Testeo de tiempo de template/matriz datos.txt", 'w')
archivo.write("Tamaño de máscara \t")
for i in range(0,cont):
    archivo.write(str(vec[i])+'\t')
archivo.write('\n')

for i in range(0,c):
    archivo.write('Rep({})\t'.format(i+1))
    for j in range (cont):
        archivo.write(str(t[i][j])+'\t')
    archivo.write('\n')
archivo.close

 
# Desvío estandar
des = np.std(t,axis = 0,ddof = 1)
#des = t.std(axis = 0,ddof = 1) #Otra forma de calcular
porc = np.around((des/h)*100,decimals=1)
archivo = open("./Testeo de tiempo de template/desvio std.txt", 'w')
archivo.write("Desvío estandar ({} rep)\r\r".format(c))
archivo.write("Tamaño de máscara\tMedia\tDesvío\t%Des\r\r")
for i in range(0,len(vec),int(len(vec)/10)):
    archivo.write(str(vec[i])+"\t")
    archivo.write(str(h[i])+"\t")
    archivo.write(str(des[i])+"\t")
    archivo.write(str(porc[i])+" %\r")
archivo.close()

# PLOT

fig, (a) = plt.subplots(nrows=1)
# a.plot(vec,h,'r')
a.errorbar(vec,h,des, color = 'k', mfc='red',ecolor = '0.45', fmt='-o', capsize = 5)
a.set_title ('Tamaño de máscara vs Tiempo promedio ({} rep)'.format(c))
a.set_xlabel ('Tamaño Template')
a.set_ylabel ('Tiempo')
plt.grid(True,which='major',ls='-',c = '0.80')
plt.minorticks_on()
plt.grid(True,which='minor',ls='-.',c = '0.90')
plt.savefig('./Testeo de tiempo de template/media_desvio_{}rep.jpg'.format(c))
plt.show()

fig, (a) = plt.subplots(nrows=1)
# a.plot(vec,h,'r')
a.errorbar(vec,h,des, color = 'k', mfc='red',ecolor = '0.45', fmt='o', capsize = 5)
a.set_title ('Tamaño de máscara vs Tiempo promedio ({} rep)'.format(c))
a.set_xlabel ('Tamaño Template')
a.set_ylabel ('Tiempo')
plt.grid(True,which='major',ls='-',c = '0.80')
plt.minorticks_on()
plt.grid(True,which='minor',ls='-.',c = '0.90')
plt.savefig('./Testeo de tiempo de template/media_desvio_{}rep_2.jpg'.format(c))
plt.show()

x2,y2,max_val = funMatch.MatchMask (new_frame,mask)
tras_x = x1-x2
tras_y = y1-y2
pos1_2 = [x1,x2,y1,y2]
panoramica = funPano.pano(panoramica, last_frame, new_frame, tras_x, tras_y, X, Y, pos1_2)

cv2.imwrite('./Testeo de tiempo de template/PANO_prueba_tiempo_{}rep.png'.format(c), panoramica)

# Notas:
# vec --> vector/lista que guarda tamaños de máscaras/templates 
# vec2 --> vector/lista de valores de tiempo correspondientes a los diferentes tamaños de máscaras
# vec3 --> guarda todos los datos de tiempo
# h --> vector de medias por tamaño de máscara