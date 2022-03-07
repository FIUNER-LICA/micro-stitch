import numpy as np
from cv2 import cv2
mask = np.zeros((500,500,3),np.uint8)

#hacerlo mas general
mask [100:109,100:109] = [255,255,255]
mask [100:109,391:400] = [255,255,255]
mask [391:400,100:109] = [255,255,255]
mask [391:400,391:400] = [255,255,255]
mask [246:255,246:255] = [255,255,255]

# cv2.imwrite("mask.png",mask)