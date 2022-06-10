import sys
sys.path.append('../modules')
from globals_DTO import *
import frame_validation
from mask_extracting import Mask
import mask_search
import build_panoramic_image

# Establecer conexión con la cámara. Adquirir imagen. --> OpenCV, PySpin, EasyPySpin

def build (panoramic, last_image, new_image, mask: Mask):
    global R #Fila inicial del frame
    
    global C # Columna inicial del frame
    # print (R, C)
        
# mask = Mask()

# # # # Validación de frame
# # # # # (No necesariamente deben retornar algo, solo para entendimiento)
# # # window = [], K = [] , L = []

# # # validation_1 = frame_validation.image_quality(image_0,image_1,window, K, L)
# # # validation_2 = frame_validation.focus_validation(image_0)

    # Extracción/Obtención de máscara
    try:
        mask.mask_by_simple_method(last_image, 100)
    except:
        print ('Error. Falla en generación de máscara')
# Búsqueda/Localización de la máscara, si fue correctamente validada [validation_1 == validation_2 == 'OK']
    try:
        mask_search.default_search(new_image, mask)
        if not mask.satisfactory_criterion:
            return panoramic
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
        if (abs(mask.traslation[0])>20 or abs(mask.traslation[1])>20):
            panoramic = build_panoramic_image.overlap_sector_combination_replacement(panoramic, new_image, R, C, 
                                                    mask.traslation[0], mask.traslation[1])
    # Actualizar parámetros para próximo frame:
    except:
        print ('Error. Falla en construcción de panorámica')

    if (R+mask.traslation[0])>=0:
        R=R+mask.traslation[0]
    else: R=0

    if (C+ mask.traslation[1])>=0:
        C=C+ mask.traslation[1]
    else: C=0
    return panoramic