import random
import numpy as np
from cv2 import cv2

img = cv2.imread("prueba.png")

print (img.shape)

roi_principal = img [0:500,0:500,:]
# cv2.imwrite("roi_principal.png",roi_principal)

roi_x = img [150:650,0:500,:]
# cv2.imwrite("roi_x.png",roi_x)

roi_y = img [0:500,150:650,:]
# cv2.imwrite("roi_y.png",roi_y)

roi_xy = img [150:650,150:650,:]
# cv2.imwrite("roi_xy.png",roi_xy)


