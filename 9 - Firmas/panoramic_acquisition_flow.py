import frame_validation
from mask_extracting import Mask
import mask_quest
import build_panoramic_image

# Establecer conexión con la cámara. Adquirir imagen. --> OpenCV, PySpin, EasyPySpin
image_0 = None
image_1 = None
F = 0 # Fila inicial del frame
C = 0 # Columna inicial del frame
mascara = Mask()

# Validación de frame
# # (No necesariamente deben retornar algo, solo para entendimiento)
window = [], K = [] , L = []

validation_1 = frame_validation.image_quality(image_0,image_1,window, K, L)
validation_2 = frame_validation.focus_validation(image_0)

# Extracción/Obtención de máscara

mascara.mask_by_simple_method()

# Búsqueda/Localización de la máscara, si fue correctamente validada [validation_1 == validation_2 == 'OK']

mask_quest.default_search(image_1, mascara)

# Sí halló la máscara, calcular la traslación

if not mascara.new_mask_position == None: # implementar try-except en vez de if
    mascara.traslation()

# Construir/agrandar/completar la panorámica
# # en un bucle, image_0 pasaría a ser la panorámica

build_panoramic_image.overlap_sector_combination_replacement(   image_0, image_1, F, C, 
                                                mascara._traslation[0], mascara._traslation[1])

