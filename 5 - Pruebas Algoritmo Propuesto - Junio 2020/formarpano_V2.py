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
r=200
inicio = time.perf_counter()
for new_frame in img_in[1:]: #hacer arreglo de imagenes y simular que va leyendo los nuevos frames
    # plt.imshow(panoramica[:,:,::-1])
    # plt.waitforbuttonpress()
    # plt.draw()
    mask = last_frame[x1:x1+r,y1:y1+r,:]
    x2,y2,max_val = funMatch.MatchMask (new_frame,mask)
    while max_val<0.7:
        y1=y1-r
        mask = last_frame[x1:x1+r,y1:y1+r,:]
        x2,y2,max_val = funMatch.MatchMask (new_frame,mask)

    tras_y=y1-y2
    tras_x = x1-x2
    pos1_2 = [x1,x2,y1,y2]
    panoramica = funPano.pano(panoramica, last_frame, new_frame, tras_x, tras_y, X, Y, pos1_2)
    
    last_frame = new_frame

    if (X+tras_x)>=0:
        X=X+tras_x
    else: X=0
    if (Y+tras_y)>=0:
        Y=Y+tras_y
    else: Y=0
    y1=int(last_frame.shape[1]/2)
fin = time.perf_counter()



s = str(panoramica.shape)
cv2.imwrite('./Img_Resultados/PANORAMICA_{}.jpg'.format(s), panoramica)
print ('tiempo', fin-inicio)

plt.imshow(panoramica[:,:,::-1])
plt.show()

