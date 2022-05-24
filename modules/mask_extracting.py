class Mask:
    
    def __init__(self) -> None:
        self._mask_value = [] # lista de ndarray de mxnx3
        self._mask_position = [] # lista de tuplas (f,c)
        self._new_mask_position = None
        self._traslation = None 

    def mask_by_simple_method(self, image, r = 50):       
        """Agrega valores a '_mask_position' y a '_mask_value'.
        La máscara se extrae del centro de la imagen.

        Args:
            image (ndarray): último frame agregado a la imagen panorámica.
            r (int): tamaño en píxeles de la máscara de rxr.
        """
        try:
            row     = int ((image.shape[0]-r)/2)
            column  = int ((image.shape[1]-r)/2)
            self._mask_value = image[row:row+r,column:column+r,:]
            self._mask_position.append((row,column))
        except:
            print ("Error. No se pudo completar la extracción de máscara.")

    def n_mask_by_default_method(self, image, r): # en principio n = 4...
        """Se extraen 4 máscaras cuadradas de rxr. Las
            posiciones son fijas en las 4 esquinas de la
            imagen

        Args:
            image (_type_): imagen de MxN.
            r (int): ancho y largo de las máscaras (imágenes de rxr).
        """
        pass
    
    def traslation_estimate(self):
        try: 
            if not self._new_mask_position == None:
                row_traslation = self._mask_position[-1][0]     - self._new_mask_position[0]
                column_traslation = self._mask_position[-1][1]  - self._new_mask_position[1]
                self._traslation = [row_traslation, column_traslation]
                print ('La traslación en filas y columnas es de: ')
        except:
            print ('Error. No se pudo realizar el cálculo de traslación')
            pass

    @property
    def mask_value(self):
        return self._mask_value

    @mask_value
    def mask_value(self, value):
        self._mask_value = value

    @property
    def mask_position(self):
        return self._mask_position

    @mask_position
    def mask_position(self, value):
        self._mask_position = value
    
    @property
    def new_mask_position(self):
        return self._new_mask_position

    @new_mask_position
    def new_mask_position(self, value):
        self._new_mask_position = value

    @property
    def traslation(self):
        return self._traslation