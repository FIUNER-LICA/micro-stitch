from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
from Funciones import funPano, funMatch

def panoCam(panoramica1, last_frame, new_frame, X,Y,r, x1,y1):
    panoramica = panoramica1.copy()
    mask = last_frame[x1:x1+r,y1:y1+r,:]
    x2,y2,max_val = funMatch.MatchMask (new_frame,mask)
    # while max_val<0.8:
    #     y1=y1-r
    #     mask = last_frame[x1:x1+r,y1:y1+r,:]
    #     x2,y2,max_val = funMatch.MatchMask (new_frame,mask)

    tras_y=y1-y2
    tras_x = x1-x2
    if (tras_y==0 and tras_x==0):
        return panoramica, X,Y
    
    pos1_2 = [x1,x2,y1,y2]
    panoramica = funPano.pano(panoramica, last_frame, new_frame, tras_x, tras_y, X, Y, pos1_2)
    

    if (X+tras_x)>=0:
        X=X+tras_x
    else: X=0
    if (Y+tras_y)>=0:
        Y=Y+tras_y
    else: Y=0
    y1=int(last_frame.shape[1]/2) #para que estaba? se puede sacar.. 

    return panoramica,X,Y