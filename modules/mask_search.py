# from threading import Thread
from mask_extracting import Mask
from cv2 import matchTemplate, minMaxLoc, TM_CCOEFF_NORMED

def default_search(image, mask: Mask) -> None: # lista de 1 elemento
    """
    Se realiza la búsqueda de la máscara en el nuevo frame, utilizando 
    los métodos de OpenCV: matchTemplate (calcula la correlación) y
    minMaxLoc (halla los máximos, mínimos y sus posiciones respectivas 
    de una correlación).

    Args:
        image (ndarray): Nuevo frame.
        mask (Mask): máscara o template buscado
    """
    try:
        # print (mask.mask_value.shape)
        res = matchTemplate(image, mask.mask_value, TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = minMaxLoc(res)
        mask.new_mask_position = (max_loc[1], max_loc[0])
        if max_val>=0.8:
            mask.satisfactory_criterion = True
        else:
            mask.satisfactory_criterion = False
    except:
        print ('Error. No se encuentra la matriz de correlación')
    
    
    
def compound_search(image, mask: Mask): # lista de más de 1 elemento
    pass