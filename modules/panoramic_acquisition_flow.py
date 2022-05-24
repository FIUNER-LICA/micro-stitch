import frame_validation
from mask_extracting import Mask
import mask_search
import build_panoramic_image

# Establecer conexión con la cámara. Adquirir imagen. --> OpenCV, PySpin, EasyPySpin
image_0 = None
panoramic = image_0
image_1 = None
R = 0 # Fila inicial del frame
C = 0 # Columna inicial del frame
mascara = Mask()

# Validación de frame
# # (No necesariamente deben retornar algo, solo para entendimiento)
window = [], K = [] , L = []

validation_1 = frame_validation.image_quality(image_0,image_1,window, K, L)
validation_2 = frame_validation.focus_validation(image_0)

# Extracción/Obtención de máscara

mascara.mask_by_simple_method(image_0, 60)

# Búsqueda/Localización de la máscara, si fue correctamente validada [validation_1 == validation_2 == 'OK']

mask_search.default_search(image_1, mascara)

# Sí halló la máscara, calcular la traslación

if not mascara.new_mask_position == None: # implementar try-except en vez de if
    mascara.traslation_estimate()

# Construir/agrandar/completar la panorámica
# # en un bucle, image_0 pasaría a ser la panorámica
if not mascara.traslation == [0,0]:    
    panoramic = build_panoramic_image.overlap_sector_combination_replacement(image_0, image_1, R, C, 
                                                mascara.traslation[0], mascara.traslation[1])
    # Actualizar parámetros para próximo frame:
    if (R+mascara.traslation[0])>=0:
            R=R+mascara.traslation[0]
    else: R=0

    if (C+ mascara.traslation[1])>=0:
            C=C+ mascara.traslation[1]
    else: C=0

image_0 = image_1.copy()
