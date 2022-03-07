from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img_1 = cv2.imread("./ImagenesHE/1.jpg", cv2.IMREAD_ANYCOLOR)

img = img_1.copy()

h = img.shape[1]
w = img.shape[0]

w1 = int(w/4)
h1 = int(h/4)
c = 0
d = 0
e = 0
f = 0
for i in range(8):
    for j in range(8):
        if i%2==0:
            c=i*8+f
            if j==7:
                result = np.ndarray((w1,h1,img.shape[2]))
                a=int(j*int(h1/2))
                l = int (i*int(w1/2))
                result[:,:,:] = img[l:l+w1,h-h1:,:]
                cv2.imwrite('./imagenes generadas/PANORAMICA_{}.jpg'.format(c), result)
                f=f+1
            else:
                result = np.ndarray((w1,h1,img.shape[2]))
                a=int(j*int(h1/2))
                l = int (i*int(w1/2))
                result[:,:,:] = img[ l:l+w1,a:a+h1,:]
                cv2.imwrite('./imagenes generadas/PANORAMICA_{}.jpg'.format(c), result)
                f=f+1
        else:
            f=0
            # d = i*8+8-1
            d = i*8+e
            # d=d-e

            if i==7:
                if j==7:
                    result = np.ndarray((w1,h1,img.shape[2]))
                    a=int(j*int(h1/2))
                    l = int (i*int(w1/2))
                    result[:,:,:] = img[w-w1:,:h1,:]
                    # result[:,:,:] = img[w-w1:,h-h1:,:]
                    cv2.imwrite('./imagenes generadas/PANORAMICA_{}.jpg'.format(d), result)
                    e=e+1
                else:
                    result = np.ndarray((w1,h1,img.shape[2]))
                    a=int(j*int(h1/2))
                    l = int (i*int(w1/2))
                    result[:,:,:] = img[w-w1:,h-(h1+a):h-a,:]
                    # result[:,:,:] = img[w-w1:,a:a+h1,:]
                    cv2.imwrite('./imagenes generadas/PANORAMICA_{}.jpg'.format(d), result)
                    e=e+1
            else:
                
                if j==7:
                    result = np.ndarray((w1,h1,img.shape[2]))
                    # result[:,:,:] = img[l:l+w1,h-h1:,:]
                    result[:,:,:] = img[l:l+w1,:h1,:]
                    cv2.imwrite('./imagenes generadas/PANORAMICA_{}.jpg'.format(d), result)
                    
                else:
                    result = np.ndarray((w1,h1,img.shape[2]))
                    a=int(j*int(h1/2))
                    l = int (i*int(w1/2))
                    # result[:,:,:] = img[ l:l+w1,a:a+h1,:]
                    result[:,:,:] = img[l:l+w1,h-(h1+a):h-a,:]
                    cv2.imwrite('./imagenes generadas/PANORAMICA_{}.jpg'.format(d), result)
                    e = e+1
    d=0
    e = 0