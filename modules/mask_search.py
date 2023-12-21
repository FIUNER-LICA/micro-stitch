"""
Mask Search
===========
This module implements methods to search for a template or mask in some image.
--------------------------------------------------------------------------------

The implemented methods are:
* default_search
"""

# from threading import Thread
from sys import path
path.append("../")
from modules.mask_extracting import Mask
from cv2 import matchTemplate, minMaxLoc, TM_CCOEFF_NORMED

def default_search(image, mask: Mask) -> None: # lista de 1 elemento
    """
    The search for the mask in the new frame is performed, using the OpenCV 
    methods: matchTemplate (calculates the correlation) and minMaxLoc (finds 
    the maximum, minimum and their respective positions of a correlation).

    Args:
        image (ndarray): image in which the mask will be searched. It can be a 
                        new frame on the process for stitching

        mask (Mask): wanted template or mask. The Mask object comes from the 
                    mask_extracting module.
    """
    try:
        res = matchTemplate(image, mask.mask_value, TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = minMaxLoc(res)
        mask.new_mask_position = (max_loc[1], max_loc[0])
        if max_val>=0.8:
            mask.satisfactory_criterion = True
        else:
            mask.satisfactory_criterion = False
    except Exception as e:
        print ('Error. No se encuentra la matriz de correlación')
        print(e)
    
    
    
def compound_search(image, mask: Mask): # lista de más de 1 elemento
    pass