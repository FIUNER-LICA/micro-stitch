"""
Mask Extracting
===============

This module contains the implementation of 'Mask' object.\n
The masks are extracted from a numpy ndarray using different 
methods implemented in the Mask class.

Mask Content
------------

Mask object contains the data related to the mask (attributes):
    - Array values
    - Position from where it was extracted
    - Position where it was found
    - Pixels moved

Mask methods:
    Mask removal methods can be varied. To learn the details of these methods, we 
    recommend that you explore the description of each particular method.

"""

class Mask:

    def __init__(self) -> None:
        self._mask_value = [] # lista de ndarray de mxnx3
        self._mask_position = [] # lista de tuplas (f,c)
        self._new_mask_position = None
        self._traslation = [0,0]
        self._satisfactory_criterion = False

    def mask_by_simple_method(self, image, r = 50):       
        """
        The mask is extracted from the center of the image.\n
        This method assign the position and the value of all pixels on
        '_mask_position' and '_mask_value' respectively.

        Args:
            image (ndarray): last frame added to the panoramic image.
            r (int): number of pixels to dimension the lengh and hight of the mask [rxr].
        """
        try:
            row     = int ((image.shape[0]-r)/2)
            column  = int ((image.shape[1]-r)/2)
            self._mask_value = image[row:row+r,column:column+r,:]
            self._mask_position.append((row,column))
        except:
            print ("Error. No se pudo completar la extracción de máscara.")

    def n_mask_by_default_method(self, image, r): # en principio n = 4...
        """
        This method extract 4 masks with rxr size. The positions are fixed in the 4
        corners from the image.
        
        Args:
            image (_type_): image to MxN size.
            r (int): number of pixels to dimension the lengh and hight of each mask [rxr].
        """
        pass
    
    def traslation_estimate(self):
        """
        This method estimate the last shift or translation on rows and columns.
        The result is asignated to '_traslation' atribute as a list type 
        [row_traslation, column_traslation].
        """
        try: 
            if not self._new_mask_position == None:
                row_traslation = self._mask_position[-1][0]     - self._new_mask_position[0]
                column_traslation = self._mask_position[-1][1]  - self._new_mask_position[1]
                self._traslation = [row_traslation, column_traslation]
        except:
            print ('Error. No se pudo realizar el cálculo de traslación')

    @property
    def mask_value(self):
        return self._mask_value

    @mask_value.setter
    def mask_value(self, value):
        self._mask_value = value

    @property
    def mask_position(self):
        return self._mask_position

    @mask_position.setter
    def mask_position(self, value):
        self._mask_position = value
    
    @property
    def new_mask_position(self):
        return self._new_mask_position

    @new_mask_position.setter
    def new_mask_position(self, value):
        self._new_mask_position = value

    @property
    def traslation(self):
        return self._traslation

    @property
    def satisfactory_criterion(self):
        return self._satisfactory_criterion

    @satisfactory_criterion.setter
    def satisfactory_criterion(self, value):
        self._satisfactory_criterion = value