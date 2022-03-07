import numpy as np
import scipy
from cv2 import cv2
from scipy import signal
from scipy.ndimage import correlate

img = cv2.imread("imagenes_tigre.jpg") # 1200 x 629

#hacerlo mas general
roi_principal = img [:200,:200,:]
# cv2.imwrite("roi_principal.png",roi_principal)

roi_x = img [50:250,0:200,:]
# cv2.imwrite("roi_x.png",roi_x)

roi_y = img [0:200,50:250,:]
# cv2.imwrite("roi_y.png",roi_y)

roi_xy = img [50:250,50:250,:]
# cv2.imwrite("roi_xy.png",roi_xy)

#mask
#hacerlo mas general
mask = np.zeros((200,200,3),np.uint8 )
mask [20:29,20:29] = roi_principal [20:29,20:29]
mask [20:29,171:180] = roi_principal [20:29,171:180]
mask [171:180,20:29] = roi_principal [171:180,20:29] 
mask [171:180,171:180] = roi_principal [171:180,171:180]
mask [96:105,96:105] = roi_principal [96:105,96:105]



a = np.fft.fftn(mask)
b = (np.fft.fftn(roi_x))


cor = a.conj()*b
a_fase = np.arctan (b.imag/(b.real))
a_fase =((a_fase-np.min(a_fase))/(np.max(a_fase)-np.min(a_fase)))*255

cv2.imshow('mod',a_fase)
cv2.waitKey(0)

cor = np.fft.ifftn(cor)
cv2.imwrite("corr.png",cor.real)

# corr = scipy.signal.correlate(a,b,mode='full',method ='fft')
# corr = np.fft.ifftn(corr)
# print (corr.shape)

# corr = corr [:,:,:3]
# print (corr.shape)
# cv2.imwrite("corr.png", corr.real)
