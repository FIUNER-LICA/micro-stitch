from cv2 import cv2
import numpy as np
from Funciones import PanoCam
import time
import datetime

import sys
import PySpin

def main():

    cap = cv2.VideoCapture(0,cv2.CAP_ANY)#cv2.CAP_DSHOW)

    b = True
    b2 = False
    bandera = True
    X = 0
    Y = 0
    r = 110
    panoramica = np.zeros((10,10))

    while (cap.isOpened()):
        ret,imagen = cap.read()
        # print(imagen.shape) 480x640
        if ret==True:
            if b and (cv2.waitKey(1) & 0xFF == ord('l')):
                panoramica=imagen.copy()
                b=False
                last_frame = imagen.copy()
                b2 = True
                x1=int(last_frame.shape[0]/2)
                y1=int(last_frame.shape[1]/2)
            if b2:
                try:
                    panoramica, X, Y= PanoCam.panoCam(panoramica, last_frame, imagen, X, Y, r, x1, y1)
                    last_frame = imagen.copy()
                    x1=int(last_frame.shape[0]/2)
                    y1=int(last_frame.shape[1]/2)
                    bandera = True
                except:
                    bandera = False
                    pass
            if bandera:
                a = cv2.resize(panoramica,(1000,700))
                cv2.imshow('Panorámica',a)
            # time.sleep(0.01)
            if cv2.waitKey(1) & 0xFF == ord('p'):
                x = datetime.datetime.now()
                cv2.imwrite('./Panoramica_{}_{}_{}_{}_{}.jpg'.format(x.hour,x.minute,x.day,x.month, x.year), panoramica[:,:,:])
                break
    # print(panoramica.shape, imagen.shape)
    cv2.destroyAllWindows()
    cap.release()
    cv2.destroyAllWindows()

main()


