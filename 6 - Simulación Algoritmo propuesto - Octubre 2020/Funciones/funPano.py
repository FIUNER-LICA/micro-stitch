import numpy as np

def pano(panoramica1, img, img2, tras_x, tras_y, X, Y, pos1_2): #ver si sacar img y usar solo panoramica
    panoramica = panoramica1.copy()
    x1,x2,y1,y2 = pos1_2

    boollayer = np.ones((panoramica.shape[0],panoramica.shape[1]),dtype=bool)     #sub-matriz de booleanos
    aux = boollayer.copy()
    aux_pano = panoramica.copy()

    if tras_y!=0 and tras_x==0: #traslacion neta horizontal
       
        if tras_y>0:

            if boollayer.shape[1]<(Y+y1+img2.shape[1]-y2):
                boollayer.resize (boollayer.shape[0],Y+y1+img2.shape[1]-y2) ####
                #agrando panoramica
                panoramica.resize(boollayer.shape[0],boollayer.shape[1],3) 
                panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
            panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy() #Ahora el x=0 no está donde estaba, por eso le resto la traslacion y copio normal el aux_pano 
            panoramica[X:X+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
        
        else:
            if (Y+tras_y)<0:
                """-(Y+tras_y) --> Puede ser que extienda el 
                tamaño de la panorámica, pero no desde la posición 0, 
                entonces ya no sería tras_y completamente lo que aumenta""" 
                boollayer.resize (boollayer.shape[0],-(Y+tras_y)+boollayer.shape[1])
                
                #agrando panoramica
                panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)
                panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
                panoramica[:aux_pano.shape [0],-(Y+tras_y):-(Y+tras_y)+aux_pano.shape[1],:] = aux_pano.copy()
                panoramica[X:X+img2.shape[0],:img2.shape[1],:] = img2.copy()
            else: 
                panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                panoramica[X:X+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()

    if tras_x!=0 and tras_y==0: #traslacion neta vertical

        if tras_x>0:

            if boollayer.shape[0]<(X+x1+img2.shape[0]-x2):
                boollayer.resize (X+x1+img2.shape[0]-x2,boollayer.shape[1]) ####
                #agrando panoramica
                panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
                panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
            panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
            panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
        else:
            if X+tras_x<0:
                boollayer.resize (-(X+tras_x)+ boollayer.shape[0],boollayer.shape[1])
                # agrando panoramica
                panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
                panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
                panoramica[-(X+tras_x):-(X+tras_x)+aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy() #Ahora el x=0 no está donde estaba, por eso le resto la traslacion y copio normal el aux_pano 
                panoramica[:img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
            else: 
                panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
    
    if tras_y!=0 and tras_x!=0: #traslacion diagonal
        
        if tras_y>0:
            #Redimencionamiento de la matriz de bool en y (horizontal)
            if boollayer.shape[1]<(Y+y1+img2.shape[1]-y2):
                boollayer.resize(boollayer.shape[0],Y+y1+img2.shape[1]-y2)
          
        else:       
            if (Y+tras_y)<0: 
                boollayer.resize (boollayer.shape[0],-(Y+tras_y)+boollayer.shape[1])

        if tras_x>0:
            if boollayer.shape[0]<(X+x1+img2.shape[0]-x2):
                boollayer.resize(X+tras_x+img2.shape[0],boollayer.shape[1]) ####

        else:
            if (X+tras_x)<0:
                boollayer.resize (-(X+tras_x)+ boollayer.shape[0],boollayer.shape[1]) ####
        
        #agrando panoramica
        panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
        panoramica [:,:,:] = 0
        if tras_x>0:
            if tras_y>0:
                #vuelvo a ponerle los valores antes del resize
                panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
            else:                
                #vuelvo a ponerle los valores antes del resize
                if (Y+tras_y)<0:
                    panoramica[:aux_pano.shape [0],-(Y+tras_y):-(Y+tras_y)+aux_pano.shape[1],:] = aux_pano.copy()
                    panoramica[X+tras_x:X+tras_x+img2.shape[0],:img2.shape[1],:] = img2.copy()
                else:
                    panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                    panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
        else:

            if tras_y>0:
                #vuelvo a ponerle los valores antes del resize
                if (X+tras_x<0):
                    panoramica[-(X+tras_x):-(X+tras_x)+aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                    panoramica[:img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
                else:
                    panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                    panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy() #ver
            else:

                if (Y+tras_y)<0:
                    if (X+tras_x<0):
                        panoramica[-(X+tras_x):-(X+tras_x)+aux_pano.shape [0],-(Y+tras_y):-(Y+tras_y)+aux_pano.shape[1],:] = aux_pano.copy()
                        panoramica[:img2.shape[0],:img2.shape[1],:] = img2.copy()
                    else:
                        panoramica[:aux_pano.shape [0],-(Y+tras_y):-(Y+tras_y)+aux_pano.shape[1],:] = aux_pano.copy()
                        panoramica[X+tras_x:X+tras_x+img2.shape[0],:img2.shape[1],:] = img2.copy()
                else:
                    if (X+tras_x<0):
                        panoramica[-(X+tras_x):-(X+tras_x)+aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                        panoramica[:img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
                    else:
                        panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                        panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy() #ver

    return panoramica