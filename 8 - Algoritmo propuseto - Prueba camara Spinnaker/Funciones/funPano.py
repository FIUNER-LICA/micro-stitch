import numpy as np

def pano(panoramica1, img, img2, tras_x, tras_y, X, Y, pos1_2): #ver si sacar img y usar solo panoramica
    
    panoramica = panoramica1.copy()
    x1,x2,y1,y2 = pos1_2
    # print(tras_x,tras_y)
    boollayer = np.ones((panoramica.shape[0],panoramica.shape[1]),dtype=bool)     #sub-matriz de booleanos
    
    if tras_y!=0 and tras_x==0: #traslacion neta horizontal
        
        aux = boollayer.copy() #capaz se puede poner uno solo fuera del if

        if tras_y>0:

            if boollayer.shape[1]<(Y+y1+img2.shape[1]-y2):
                boollayer.resize (boollayer.shape[0],Y+y1+img2.shape[1]-y2) ####
                boollayer[:,:]=False
                boollayer[:,:aux.shape[1]] = aux[:,:]

            boollayer [X-tras_x:X+img2.shape[0],Y+img2.shape[1]:Y+img2.shape[1]+tras_y] = True
            boollayer [X:X-tras_x,Y+tras_y:Y+tras_y+img2.shape[1]] = True

                #agrando panoramica
            aux_pano = panoramica.copy()
            panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
            panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
            if boollayer.shape[1]<(Y+y1+img2.shape[1]-y2):
                panoramica[X-tras_x:X-tras_x+aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy() #Ahora el x=0 no está donde estaba, por eso le resto la traslacion y copio normal el aux_pano 
            else: panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
            panoramica[X:X+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
        
        else:
            # if boollayer.shape[1]<(Y+y2+img2.shape[1]-y1):
            # if Y<np.abs(y2-y1):
            if Y+tras_y<0: 
                boollayer.resize (boollayer.shape[0],Y+y2+boollayer.shape[1]-y1) ####                
                boollayer[:,:]=False
                boollayer[:,-tras_y:-tras_y+aux.shape[1]] = aux[:,:]
            else:
                boollayer[:,:]=False
                boollayer[:,:] = aux[:,:]
            boollayer [X:X+img2.shape[0],Y:Y+tras_y] = True # revisar
            boollayer [X:img2.shape[0],Y:Y+img2.shape[1]] = True

            #agrando panoramica
            aux_pano = panoramica.copy()
            panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
            panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
            if Y+tras_y<0:
                panoramica[:aux_pano.shape [0],-tras_y:-tras_y+aux_pano.shape[1],:] = aux_pano.copy()# no fue checkeado aun
                panoramica[X:X+img2.shape[0],:img2.shape[1],:] = img2.copy()
            else: 
                panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                panoramica[X:X+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()

    if tras_x!=0 and tras_y==0: #traslacion neta vertical
        if tras_x>0:
            aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
            if boollayer.shape[0]<(X+x1+img2.shape[0]-x2):
             # if X+tras_x<0:
                boollayer.resize (X+x1+img2.shape[0]-x2,boollayer.shape[1]) ####
                boollayer[:,:]=False
                # boollayer[X:X+aux.shape[0],:] = aux[:,:]
            else: 
                boollayer[:,:]=False
                boollayer[:,:] = aux[:,:]

            boollayer [X+tras_x:X+img2.shape[0],Y+img2.shape[1]:Y+img2.shape[1]] = True
            boollayer [X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1]] = True ###VER!

                #agrando panoramica
            aux_pano = panoramica.copy()
            panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
            panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
            panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
            panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
        else:
            aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
            # if boollayer.shape[0]<(X+x2+img2.shape[0]-x1): 
            if X+tras_x<0:
                boollayer.resize (x2+aux.shape[0]-x1,boollayer.shape[1]) ####
                boollayer[:,:]=False
                boollayer[x2-x1:,:] = aux[:,:]
            
            boollayer [X-tras_x:X+img2.shape[0],Y+img2.shape[1]:Y+img2.shape[1]+tras_y] = True
            boollayer [X:X-tras_x,Y+tras_y:Y+tras_y+img2.shape[1]] = True
            #agrando panoramica
            aux_pano = panoramica.copy()
            panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
            panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
            if X+tras_x<0:
                panoramica[-tras_x:-tras_x+aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy() #Ahora el x=0 no está donde estaba, por eso le resto la traslacion y copio normal el aux_pano 
                panoramica[:img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
            else: 
                panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
    

    if tras_y!=0 and tras_x!=0: #traslacion diagonal

        if tras_y>0:
            #Redimencionamiento de la matriz de bool en y (horizontal)
            if boollayer.shape[1]<(Y+y1+img2.shape[1]-y2):
                aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
                boollayer.resize(boollayer.shape[0],Y+y1+img2.shape[1]-y2)
                boollayer[:,:]=False
                boollayer[:,:aux.shape[1]] = aux[:,:]
          
        #hacer un else que complete con los nuevos datos si no debe crecer en y.. capaz mas abajo directamente
        else:       
            # if boollayer.shape[1]<(Y+y2+img.shape[1]-y1):
            aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
            if (Y+tras_y)<0: 
                boollayer.resize (boollayer.shape[0],Y+y2+boollayer.shape[1]-y1) ####
                boollayer[:,:]=False
                boollayer[:,Y+y2-y1:] = aux[:,:]

        if tras_x>0:
            aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
            if boollayer.shape[0]<(X+x1+img2.shape[0]-x2):
                boollayer.resize(X+tras_x+img2.shape[0],boollayer.shape[1]) ####
                boollayer[:,:]=False
                boollayer[:aux.shape[0],:] = aux[:,:]

        else:
            aux = boollayer.copy() #capaz se puede poner uno solo fuera del if
            # if boollayer.shape[0]<(X+x2-x1+img2.shape[0]):
            if (X+tras_x)<0:
                boollayer.resize (x2+aux.shape[0]-x1,boollayer.shape[1]) ####
                
                boollayer[:,:]=False
                boollayer[x2-x1:,:] = aux[:,:]
           
    ### Completo con 1 la matriz de bool, y en paralelo agrando y copio los datos en la panoramica
        aux_pano = panoramica.copy()
        if tras_x>0:
            if tras_y>0:
                boollayer [X+tras_x:X+img2.shape[0],Y+img2.shape[1]:Y+img2.shape[1]] = True
                boollayer [X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1]] = True ###VER!
            #agrando panoramica
                panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
                panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
                panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
            else:
                
                boollayer [X+tras_x:X+tras_x+img2.shape[0],Y:Y-tras_y] = True
                boollayer [X+img2.shape[0]:X+tras_x+img2.shape[0],Y:Y+img2.shape[1]] = True
                
                #agrando panoramica
                panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
                panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
                if (Y+tras_y)<0:
                    panoramica[:aux_pano.shape [0],-tras_y:-tras_y+aux_pano.shape[1],:] = aux_pano.copy()
                    panoramica[X+tras_x:X+tras_x+img2.shape[0],:img2.shape[1],:] = img2.copy()
                else:
                    panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                    panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
        else:
            if tras_y>0:
                boollayer [X-tras_x:X+img2.shape[0],Y+img2.shape[1]:Y+img2.shape[1]+tras_y] = True
                boollayer [X:X-tras_x,Y+tras_y:Y+tras_y+img2.shape[1]] = True
                #agrando panoramica
                panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
                panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
                if (X+tras_x<0):
                    panoramica[-tras_x:-tras_x+aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy() #Ahora el x=0 no está donde estaba, por eso le resto la traslacion y copio normal el aux_pano 
                    panoramica[:img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
                else:
                    panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                    panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy() #ver
            else:
                boollayer [X-tras_x:X+img2.shape[0],Y:Y-tras_y] = True
                boollayer [X:X-tras_x,Y:Y+img2.shape[1]] = True
                #agrando panoramica
                panoramica.resize(boollayer.shape[0],boollayer.shape[1],3)        
                panoramica [:,:,:] = 0
                #vuelvo a ponerle los valores antes del resize
                # # # panoramica[X-tras_x:X-tras_x+aux_pano.shape [0],Y-tras_y:Y-tras_y+aux_pano.shape[1],:] = aux_pano.copy()
                # # # panoramica[X:X+img2.shape[0],Y:Y+img2.shape[1],:] = img2.copy()

                if (Y+tras_y)<0:
                    if (X+tras_x<0):
                        panoramica[-tras_x:-tras_x+aux_pano.shape [0],-tras_y:-tras_y+aux_pano.shape[1],:] = aux_pano.copy()
                        panoramica[:img2.shape[0],:img2.shape[1],:] = img2.copy()
                    else:
                        panoramica[:aux_pano.shape [0],-tras_y:-tras_y+aux_pano.shape[1],:] = aux_pano.copy()
                        panoramica[X+tras_x:X+tras_x+img2.shape[0],:img2.shape[1],:] = img2.copy()
                else:
                    if (X+tras_x<0):
                        panoramica[-tras_x:-tras_x+aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                        panoramica[:img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy()
                    else:
                        panoramica[:aux_pano.shape [0],:aux_pano.shape[1],:] = aux_pano.copy()
                        panoramica[X+tras_x:X+tras_x+img2.shape[0],Y+tras_y:Y+tras_y+img2.shape[1],:] = img2.copy() #ver

    
    return panoramica