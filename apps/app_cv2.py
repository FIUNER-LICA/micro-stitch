from sys import path

path.append('../modules')

from modules.mask_extracting import Mask
import modules.panoramic_acquisition as pac
from modules.globals_DTO import *
import modules.frame_validation as f_val

from cv2 import cv2
import numpy as np
import datetime
from threading import Event, Thread

# Inicio de variables, parámetros y creación de objetos
# global R #Fila inicial del frame
# global C # Columna inicial del frame
R = 0
C = 0

is_first_image = True
flag_view  = True
focus = True
growing = True

mask_object = Mask()
panoramic = np.zeros((640,480,3),dtype="uint8")
new_image = np.zeros((640,480,3),dtype="uint8")

image_stack =[]# np.zeros((640,480,3),dtype="uint8")


cap = cv2.VideoCapture(0,cv2.CAP_ANY) # 2, cv2.CAP_DSHOW) # 

def focus_analisys(threshold, args):
    global new_image
    global focus
    while (True):
        new_image_capture.wait()
        try:
            
            focus_value = f_val.focus_validation(new_image, args)
            if focus_value[1] > threshold:
                print (focus_value[1], threshold)
                focus=True
            else:
                focus = False 
        except: 
            print ("Error en cálculo de foco. Revise los parámetros.")
        new_image_capture.clear()

# Bandera para activar/desactivar el pre-análisis
image_analisys = False

new_image_capture = Event()

pre_analisys = Thread (target= focus_analisys, daemon=True, args=(0,0))


while (cap.isOpened()):
    ret, new_image = cap.read()

    if image_analisys:
        pre_analisys.start()
        new_image_capture.set() 
    
    if ret == True:
        #Dar inicio al stream y formación de panorámica
        if (not is_first_image) and focus:
            try:           
                image_stack.append(new_image)
                panoramic, growing = pac.build(panoramic, last_image, new_image, mask_object)
                last_image = new_image# .copy() # @todo: Se puede sacar el .copy() SI NO SE AGREGO LA NUEVA IMAGEN NO DEBE ASIGNARSE A LAST IMAGE
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
            image_stack = np.array(image_stack)
            # cv2.imwrite('../data/panoramic_cv2_{}_{}_{}_{}_{}.tiff'.format(x.hour,x.minute,x.day,x.month, x.year), panoramic[:,:,:])
            cv2.imwritemulti('../data/panoramic_cv2_{}_{}_{}_{}_{}.tiff'.format(x.hour,x.minute,x.day,x.month, x.year), image_stack)#[:,:,:])
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
