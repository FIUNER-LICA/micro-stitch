class Mask:
    
    def __init__(self) -> None:
        self._mask_value = [] # lista de ndarray de mxnx3
        self._mask_position = [] # lista de tuplas (f,c)
        self.new_mask_position = None
        self._traslation = None

    def mask_by_simple_method(self, image, r):
        """ Agrega valores a '_mask_position' y a '_mask_value' 
        """
        pass

    def n_mask_by_default_method(self, image, r): # en principio n = 4...
        """_Se extraen 4 máscaras cuadradas de rxr. Las
            posiciones son fijas en las 4 esquinas de la
            imagen_

        Args:
            image (_type_): _imagen de MxN_
            r (_int_): _ancho y largo de las máscaras (imágenes de rxr)_
        """
        pass
    
    def traslation(self):
        try: 
            if not self.new_mask_position == None:
                print ('La traslación en filas y columnas es de: ')
        except:
            print ('Error. No se pudo realizar el cálculo de traslación')
            pass

