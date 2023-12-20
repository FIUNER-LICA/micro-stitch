from sys import path

path.append('../')

from modules.mask_extracting import Mask
import modules.panoramic_acquisition as pac
from modules.globals_DTO import *
import modules.frame_validation as f_val
from skimage.metrics import structural_similarity as ssim

import cv2
import numpy as np
import datetime

from time import perf_counter


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

# Inicio de variables, parámetros y creación de objetos
# global R # Fila inicial del frame
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


#cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) 

# Bandera para activar/desactivar el pre-análisis
image_analisys = False

# new_image_capture = Event()

# pre_analisys = Thread (target= focus_analisys, daemon=True, args=(0,0))

coordinates = (10,20)
font = cv2.FONT_HERSHEY_PLAIN
fontScale = 1
color = (255,255,255)
thickness = 1
fix_text = "API Backend: " + cap.getBackendName()\
            + '\n' + "cv2 fps: " + str(cap.get(cv2.CAP_PROP_FPS)) + '\n' 

t_end = perf_counter()

counter = 1
frame_rate = 0
n_prom = 10

changing_text = "measure FPS: " + str(frame_rate) + "\n"+\
                "var Laplacian: " + \
                "var Sobel:  " + \
                "SSIM: "    
    
while (cap.isOpened()):
    ret, new_image = cap.read()
    
    ## prepare and show frame with info text data
    frame_with_text_info =  new_image.copy()
    if counter % n_prom != 0:
        frame_rate += 1/(perf_counter()-t_end)
        counter += 1
    else:
        frame_rate /= n_prom
        #frame_rate_line = "measure FPS: " + str(round(frame_rate,2)) + "\n"
        var_lap = str(round(cv2.Laplacian(new_image,cv2.CV_64F,0).var(),2))
        var_sobel = str(round(cv2.Sobel(new_image,cv2.CV_64F,1,0,ksize=5).var(),2))
        str_ssim = str(round(ssim(last_image, new_image,channel_axis=2, multichannel=True ),2))

        changing_text = "measured FPS: " + str(round(frame_rate,2)) + "\n" + \
                        "var Laplacian: " + var_lap   + "\n" + \
                        "var Sobel:  " + var_sobel + "\n"  + \
                        "SSIM: "  + str_ssim


        frame_rate = 0
        counter = 1

    text = fix_text + changing_text 
    cv2.rectangle(frame_with_text_info, (0,0), (200,100), (0,0,0), -1)
    coordinates = (10,20)

    for line in text.split('\n'):
        cv2.putText(frame_with_text_info, line , coordinates , font, fontScale, color, thickness, cv2.LINE_AA)
        coordinates = (coordinates[0], coordinates[1] + 15)
    
    cv2.imshow('new_image',frame_with_text_info)
    ## end prepare image with info text data
    

    # if image_analisys:
    #     pre_analisys.start()
    #     new_image_capture.set() 
    
    if ret == True:
        #Dar inicio al stream y formación de panorámica
        if not is_first_image: # and focus:
            try:           
                image_stack.append(new_image)
                panoramic, growing, R, C = pac.build(panoramic, last_image, new_image, mask_object, R, C)
                if growing:
                    last_image = new_image# .copy() # @todo: Se puede sacar el .copy() SI NO SE AGREGO LA NUEVA IMAGEN NO DEBE ASIGNARSE A LAST IMAGE
                    flag_view = True
                else: 
                    flag_view = True
            except:
                flag_view = False
                

        if is_first_image:# and (cv2.waitKey(1) & 0xFF == ord('i')):
            panoramic = new_image.copy()
            last_image = new_image.copy()
            is_first_image = False

        if flag_view:
            view = cv2.resize(panoramic, (700,500))
            cv2.imshow('Panorámica',view)
            # cv2.resizeWindow('Panorámica', 700, 500)

        if cv2.waitKey(5) & 0xFF == ord('q') or cv2.getWindowProperty('new_image',cv2.WND_PROP_VISIBLE) < 1:
            break

        if cv2.waitKey(1) & 0xFF == ord('p'):
            x = datetime.datetime.now()
            image_stack = np.array(image_stack)
            # cv2.imwrite('../data/panoramic_cv2_{}_{}_{}_{}_{}.tiff'.format(x.hour,x.minute,x.day,x.month, x.year), panoramic[:,:,:])
            # cv2.imwritemulti('../data/panoramic_cv2_{}_{}_{}_{}_{}.tiff'.format(x.hour,x.minute,x.day,x.month, x.year), image_stack)#[:,:,:])
            break
    t_end = perf_counter()

cv2.destroyAllWindows()
cap.release()
