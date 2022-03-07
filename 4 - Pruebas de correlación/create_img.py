import random
import numpy as np
from cv2 import cv2

#let's create a n x n matrix with all pixels in black color
img = np.zeros((5000,5000,3),np.uint8)

#let's use "for" cycle to change colorspace of pixel in a random way
for x in range(5000):
    for y in range(5000):
        #We use "0" for black color (do nothing) and "1" for white color (change pixel value to [255,255,255])
        value = random.randint(0,1)
        if value == 1:
            img[x,y] = [255,255,255]

#save our image as a "png" image
# cv2.imwrite("prueba.png",img)