import numpy as np

def pano(panoramica_original, img2, tras_x, tras_y, X, Y):

    enlarged_rows = panoramica_original.shape[0]
    enlarged_column = panoramica_original.shape[1]

    if tras_y!=0 and tras_x==0: #traslacion neta horizontal
       
        if tras_y>0:
            if panoramica_original.shape[1]<(Y+tras_y+img2.shape[1]):
                enlarged_column = Y+tras_y+img2.shape[1]

            loc_pixels_pano = 0, panoramica_original.shape [0], 0, panoramica_original.shape[1]
            loc_pixels_img = X, X+img2.shape[0], Y+tras_y, Y+tras_y+img2.shape[1]
        
        else:
            if (Y+tras_y)<0:
                """-(Y+tras_y) --> Puede ser que extienda el 
                tamaño de la panorámica, pero no desde la posición 0, 
                entonces ya no sería tras_y completamente lo que aumenta""" 
                enlarged_column = -(Y+tras_y)+panoramica_original.shape[1]

                loc_pixels_pano = 0, panoramica_original.shape [0], -(Y+tras_y), -(Y+tras_y)+panoramica_original.shape[1]
                loc_pixels_img = X, X+img2.shape[0], 0, img2.shape[1]
            else: 
                loc_pixels_pano = 0, panoramica_original.shape [0],0, panoramica_original.shape[1]
                loc_pixels_img = X, X+img2.shape[0],Y+tras_y, Y+tras_y+img2.shape[1]

    if tras_x!=0 and tras_y==0: #traslacion neta vertical

        if tras_x>0:

            if panoramica_original.shape[0]<(X+tras_x+img2.shape[0]):
                enlarged_rows = X+tras_x+img2.shape[0]

            loc_pixels_pano = 0,panoramica_original.shape [0], 0,panoramica_original.shape[1]
            loc_pixels_img = X+tras_x, X+tras_x+img2.shape[0],Y+tras_y, Y+tras_y+img2.shape[1]
        else:
            if X+tras_x<0:
                enlarged_rows = -(X+tras_x)+ panoramica_original.shape[0]

                loc_pixels_pano = -(X+tras_x) , -(X+tras_x)+panoramica_original.shape [0] , 0 , panoramica_original.shape[1]
                loc_pixels_img = 0 , img2.shape[0],Y+tras_y , Y+tras_y+img2.shape[1]
            else: 
                loc_pixels_pano = 0 , panoramica_original.shape [0] , 0 , panoramica_original.shape[1]
                loc_pixels_img = X+tras_x , X+tras_x+img2.shape[0] , Y+tras_y , Y+tras_y+img2.shape[1]

    if tras_y!=0 and tras_x!=0: #traslacion diagonal
        
        if tras_y>0:
            if panoramica_original.shape[1]<(Y+tras_y+img2.shape[1]):
                enlarged_column = Y+tras_y+img2.shape[1]
        else:       
            if (Y+tras_y)<0: 
                enlarged_column = -(Y+tras_y)+panoramica_original.shape[1]

        if tras_x>0:
            if panoramica_original.shape[0]<(X+tras_x+img2.shape[0]):
                enlarged_rows = X+tras_x+img2.shape[0]
        else:
            if (X+tras_x)<0:
                enlarged_rows = -(X+tras_x)+ panoramica_original.shape[0]

        if tras_x>0:
            if tras_y>0:
                loc_pixels_pano = 0, panoramica_original.shape [0] , 0 , panoramica_original.shape[1]
                loc_pixels_img = X+tras_x , X+tras_x+img2.shape[0] , Y+tras_y , Y+tras_y+img2.shape[1]
            else:                
                if (Y+tras_y)<0:
                    loc_pixels_pano = 0 , panoramica_original.shape [0] , -(Y+tras_y) , -(Y+tras_y)+panoramica_original.shape[1]
                    loc_pixels_img = X+tras_x , X+tras_x+img2.shape[0] , 0 , img2.shape[1]
                else:
                    loc_pixels_pano = 0 , panoramica_original.shape [0] , 0 , panoramica_original.shape[1]
                    loc_pixels_img = X+tras_x , X+tras_x+img2.shape[0] , Y+tras_y , Y+tras_y+img2.shape[1]
        else:
            if tras_y>0:
                if (X+tras_x<0):
                    loc_pixels_pano = -(X+tras_x) , -(X+tras_x)+panoramica_original.shape [0] , 0 , panoramica_original.shape[1]
                    loc_pixels_img = 0 , img2.shape[0] , Y+tras_y , Y+tras_y+img2.shape[1] 
                else:
                    loc_pixels_pano = 0 , panoramica_original.shape [0] , 0 , panoramica_original.shape[1]
                    loc_pixels_img = X+tras_x , X+tras_x+img2.shape[0] , Y+tras_y , Y+tras_y+img2.shape[1]
            else:
                if (Y+tras_y)<0:
                    if (X+tras_x<0):
                        loc_pixels_pano = -(X+tras_x) , -(X+tras_x)+panoramica_original.shape [0] , -(Y+tras_y) , -(Y+tras_y)+panoramica_original.shape[1]
                        loc_pixels_img = 0 , img2.shape[0] , 0 , img2.shape[1]
                    else:
                        loc_pixels_pano = 0 , panoramica_original.shape [0] , -(Y+tras_y) , -(Y+tras_y)+panoramica_original.shape[1]
                        loc_pixels_img = X+tras_x , X+tras_x+img2.shape[0] , 0 , img2.shape[1]     
                else:
                    if (X+tras_x<0):
                        loc_pixels_pano = -(X+tras_x) , -(X+tras_x)+panoramica_original.shape [0] , 0 , panoramica_original.shape[1]
                        loc_pixels_img = 0 , img2.shape[0] , Y+tras_y , Y+tras_y+img2.shape[1]   
                    else:
                        loc_pixels_pano = 0 , panoramica_original.shape [0] , 0 , panoramica_original.shape[1]
                        loc_pixels_img = X+tras_x , X+tras_x+img2.shape[0] , Y+tras_y , Y+tras_y+img2.shape[1]

    panoramica = np.ndarray(shape = (enlarged_rows , enlarged_column , 3), dtype = np.int8) 
    panoramica [loc_pixels_pano[0] : loc_pixels_pano[1],loc_pixels_pano[2] : loc_pixels_pano[3],:] = panoramica_original
    panoramica [loc_pixels_img[0]:loc_pixels_img[1],loc_pixels_img[2]:loc_pixels_img[3],:] = img2
    return panoramica