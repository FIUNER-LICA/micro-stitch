from sys import path
path.append('../modules')

from mask_extracting import Mask
import panoramic_acquisition as pac
from globals_DTO import *

from cv2 import cv2
import numpy as np
import datetime

# from skimage.metrics import structural_similarity as ssim

# Inicio de variablesm, parámetros y creación de objetos
global R #Fila inicial del frame
global C # Columna inicial del frame

is_first_image = True
flag_view  = True

mask_object = Mask()
panoramic = np.zeros((640,480,3),dtype="uint8")
cap = cv2.VideoCapture(2, cv2.CAP_DSHOW) # 0,cv2.CAP_ANY) #

while (cap.isOpened()):
    ret, new_image = cap.read()
    
    if ret == True:
        #Dar inicio al stream y formación de panorámica
        if (not is_first_image):
            try:
                panoramic = pac.build(panoramic, last_image, new_image, mask_object)
                last_image = new_image# .copy() # Se puede sacar el .copy()
                flag_view = True
            except:
                flag_view = False
                pass

        if is_first_image and (cv2.waitKey(1) & 0xFF == ord('i')):
            panoramic = new_image.copy()
            last_image = new_image.copy()
            is_first_image = False

        if flag_view:
            view = cv2.resize(panoramic, (700,500))
            cv2.imshow('Panorámica',view)
            # cv2.resizeWindow('Panorámica', 700, 500)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('p'):
            x = datetime.datetime.now()
            cv2.imwrite('./panoramic_{}_{}_{}_{}_{}.jpg'.format(x.hour,x.minute,x.day,x.month, x.year), panoramic[:,:,:])
            break

cv2.destroyAllWindows()
cap.release()

    # aux_lap_var = cv2.Laplacian(new_image,cv2.CV_64F,0).var()
    # aux_lap_sob = cv2.Sobel(new_image,cv2.CV_64F,1,0,ksize=5).var()
    # if not is_first_image:
    #     aux_ssim = ssim(last_image, new_image,channel_axis=2, multichannel=True )
    #     print ("Image info:\n" +
    #                       "Varianza Lap.: " +str(aux_lap_var) + "\n"
    #                       "Varianza Sob.: " +str(aux_lap_sob) + "\n"
    #                       "SSIM : " + str(aux_ssim) + "\n")
