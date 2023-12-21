"""
    Panoramic Acquisition
    =====================
    In this module a method 'build' is implemented, responsible for 
    expand/enlargement the panoramic image, from the input images.\n

    First is need import particular modules:
    * mask_extracting
    * build_panoramic_image
    * mask_search
    * globals_DTO

    Returns:
        numpy ndarray: The module returns the panoramic image
        bool: Flag for indicate if panoramic image incorporate a new image or not
"""
from sys import path
path.append('../')
# from modules.globals_DTO import *
from modules.mask_extracting import Mask
from modules import mask_search
from modules import build_panoramic_image

# Establecer conexión con la cámara. Adquirir imagen. --> OpenCV, PySpin, EasyPySpin

def build (panoramic, last_image, new_image, mask: Mask, R, C):
    """
    This method expands the panoramic image. For this, in addition to the parameters 
    it receives, it needs two global variables (R and C) from 'globals_DTO'. That 
    variables represent the value in rows and columns in which the previous image 
    (last_image) is located with respect to the origin (coordinates 0,0) of the 
    panoramic image.\n
    
    The secuence of task for build the panoramic image is the next:
    * Extact the mask. With some method from Mask object as mask_by_simple_method
    * Mask localization (in the new_image). With the mask_search module
    * Estimate the traslation. With the traslation_estimate method from Mask object
    * Expand/Build the panoramic image. With the build_panoramic_image module
    * Update the globals variables

    Args:
        panoramic (numpy ndarray): panoramic image to expand/build

        last_image (numpy ndarray): the last image or frame that was added to the panoramic image
        
        new_image (numpy ndarray): the new frame that could be added to the panoramic image
        
        mask (Mask): Mask object from mask_extracting module
    """
    # global R #Fila inicial del frame
    # global C # Columna inicial del frame
    growing = False

    # Extracción/Obtención de máscara
    mask.mask_by_simple_method(last_image, 200)
    
    # TODO: Quitar try-except para la máscara
    # try:
    #     mask.mask_by_simple_method(last_image, 200)
    # except:
    #     print ('Error. Falla en generación de máscara')

# Búsqueda/Localización de la máscara, si fue correctamente validada [validation_1 == validation_2 == 'OK']
    try:
        mask_search.default_search(new_image, mask)
        if not mask.satisfactory_criterion:
            growing = False
            return panoramic, growing , R, C
    except:
        print ('Error. Falla en búsqueda de mascará')
# Sí halló la máscara, calcular la traslación
    try:
        if not mask.new_mask_position == None: # implementar try-except en vez de if
            mask.traslation_estimate()
            # print (mask.traslation)
    except:
        print ('Error. Falla en el cálculo de traslación.')
# Construir/agrandar/completar la panorámica
# # en un bucle, image_0 pasaría a ser la panorámica
    try:
        if (abs(mask.traslation[0])>10 or abs(mask.traslation[1])>10):
            panoramic = build_panoramic_image.overlap_sector_combination_replacement(panoramic, new_image, R, C, 
                                                    mask.traslation[0], mask.traslation[1])
            growing = True
        else:
            growing = False
    # Actualizar parámetros para próximo frame:
    except:
        print ('Error. Falla en construcción de panorámica')
    if growing:
        if (R+mask.traslation[0])>0:
            R=R+mask.traslation[0]
        else: R=0

        if (C+ mask.traslation[1])>0:
            C=C+ mask.traslation[1]
        else: C=0
    return panoramic, growing, R, C