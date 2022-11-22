import numpy as np
# from numpy import ndarray, int8

def store_valid_images(image):
    pass

def overlap_sector_combination_replacement(panoramic,image, R, C, tras_r, tras_c):
    # print("llega hasta aca 1")
    # print (tras_r)
    # print (tras_c)
    # print (R, C)
    enlarged_rows = panoramic.shape[0]
    enlarged_column = panoramic.shape[1]

    if tras_c!=0 and tras_r==0: #traslacion neta horizontal
       
        if tras_c>0:
            if panoramic.shape[1]<(C+tras_c+image.shape[1]):
                enlarged_column = C+tras_c+image.shape[1]

            loc_pixels_pano = 0, panoramic.shape [0], 0, panoramic.shape[1]
            loc_pixels_img = R, R+image.shape[0], C+tras_c, C+tras_c+image.shape[1]
        
        else:
            if (C+tras_c)<0:
                """-(C+tras_c) --> Puede ser que extienda el 
                tamaño de la panorámica, pero no desde la posición 0, 
                entonces ya no sería tras_y completamente lo que aumenta""" 
                enlarged_column = -(C+tras_c)+panoramic.shape[1]

                loc_pixels_pano = 0, panoramic.shape [0], -(C+tras_c), -(C+tras_c)+panoramic.shape[1]
                loc_pixels_img = R, R+image.shape[0], 0, image.shape[1]
            else: 
                loc_pixels_pano = 0, panoramic.shape [0],0, panoramic.shape[1]
                loc_pixels_img = R, R+image.shape[0],C+tras_c, C+tras_c+image.shape[1]

    if tras_r!=0 and tras_c==0: #traslacion neta vertical

        if tras_r>0:

            if panoramic.shape[0]<(R+tras_r+image.shape[0]):
                enlarged_rows = R+tras_r+image.shape[0]

            loc_pixels_pano = 0,panoramic.shape [0], 0,panoramic.shape[1]
            loc_pixels_img = R+tras_r, R+tras_r+image.shape[0],C+tras_c, C+tras_c+image.shape[1]
        else:
            if R+tras_r<0:
                enlarged_rows = -(R+tras_r)+ panoramic.shape[0]

                loc_pixels_pano = -(R+tras_r) , -(R+tras_r)+panoramic.shape [0] , 0 , panoramic.shape[1]
                loc_pixels_img = 0 , image.shape[0],C+tras_c , C+tras_c+image.shape[1]
            else: 
                loc_pixels_pano = 0 , panoramic.shape [0] , 0 , panoramic.shape[1]
                loc_pixels_img = R+tras_r , R+tras_r+image.shape[0] , C+tras_c , C+tras_c+image.shape[1]

    if tras_c!=0 and tras_r!=0: #traslacion diagonal
        
        if tras_c>0:
            if panoramic.shape[1]<(C+tras_c+image.shape[1]):
                enlarged_column = C+tras_c+image.shape[1]
        else:       
            if (C+tras_c)<0: 
                enlarged_column = -(C+tras_c)+panoramic.shape[1]

        if tras_r>0:
            if panoramic.shape[0]<(R+tras_r+image.shape[0]):
                enlarged_rows = R+tras_r+image.shape[0]
        else:
            if (R+tras_r)<0:
                enlarged_rows = -(R+tras_r)+ panoramic.shape[0]

        if tras_r>0:
            if tras_c>0:
                loc_pixels_pano = 0, panoramic.shape [0] , 0 , panoramic.shape[1]
                loc_pixels_img = R+tras_r , R+tras_r+image.shape[0] , C+tras_c , C+tras_c+image.shape[1]
            else:                
                if (C+tras_c)<0:
                    loc_pixels_pano = 0 , panoramic.shape [0] , -(C+tras_c) , -(C+tras_c)+panoramic.shape[1]
                    loc_pixels_img = R+tras_r , R+tras_r+image.shape[0] , 0 , image.shape[1]
                else:
                    loc_pixels_pano = 0 , panoramic.shape [0] , 0 , panoramic.shape[1]
                    loc_pixels_img = R+tras_r , R+tras_r+image.shape[0] , C+tras_c , C+tras_c+image.shape[1] # @TODO: pensar diferencia con abs(c+tras_c)
        else:
            if tras_c>0:
                if (R+tras_r<0):
                    loc_pixels_pano = -(R+tras_r) , -(R+tras_r)+panoramic.shape [0] , 0 , panoramic.shape[1]
                    loc_pixels_img = 0 , image.shape[0] , C+tras_c , C+tras_c+image.shape[1] 
                else:
                    loc_pixels_pano = 0 , panoramic.shape [0] , 0 , panoramic.shape[1]
                    loc_pixels_img = R+tras_r , R+tras_r+image.shape[0] , C+tras_c , C+tras_c+image.shape[1]
            else:
                if (C+tras_c)<0:
                    if (R+tras_r<0):
                        loc_pixels_pano = -(R+tras_r) , -(R+tras_r)+panoramic.shape [0] , -(C+tras_c) , -(C+tras_c)+panoramic.shape[1]
                        loc_pixels_img = 0 , image.shape[0] , 0 , image.shape[1]
                    else:
                        loc_pixels_pano = 0 , panoramic.shape [0] , -(C+tras_c) , -(C+tras_c)+panoramic.shape[1]
                        loc_pixels_img = R+tras_r , R+tras_r+image.shape[0] , 0 , image.shape[1]     
                else:
                    if (R+tras_r<0):
                        loc_pixels_pano = -(R+tras_r) , -(R+tras_r)+panoramic.shape [0] , 0 , panoramic.shape[1]
                        loc_pixels_img = 0 , image.shape[0] , C+tras_c , C+tras_c+image.shape[1]   
                    else:
                        loc_pixels_pano = 0 , panoramic.shape [0] , 0 , panoramic.shape[1]
                        loc_pixels_img = R+tras_r , R+tras_r+image.shape[0] , C+tras_c , C+tras_c+image.shape[1]
    # print("llega hasta aca 2")
    panoramic_return = np.ndarray(shape = (enlarged_rows , enlarged_column , 3), dtype = np.uint8) 
    # print("llega hasta aca 3")
    panoramic_return [loc_pixels_pano[0] : loc_pixels_pano[1],loc_pixels_pano[2] : loc_pixels_pano[3],:] = panoramic
    # print("llega hasta aca 4 \n", image.shape)
    # print (panoramic_return [loc_pixels_img[0]:loc_pixels_img[1],loc_pixels_img[2]:loc_pixels_img[3],:].shape)
    panoramic_return [loc_pixels_img[0]:loc_pixels_img[1],loc_pixels_img[2]:loc_pixels_img[3],:] = image
    # print("llega hasta aca 5")
    return panoramic_return

    
def overlap_sector_combination_linear_interp(panoramic,image, F, C, tras_f, tras_c):
    pass