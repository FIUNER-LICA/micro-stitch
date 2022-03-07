from cv2 import cv2
import numpy as np
from scipy import signal
from scipy.ndimage import correlate


img = cv2.imread("FigurasGeom.tif") # 815 x 451

roi = cv2.imread("roi_fig.tif") #61 x 64
cv2.imwrite("roi1.png",roi)

a = np.fft.fftn(img)
#a_fase = np.arctan (a.imag/(a.real+0.000001))
# a_fase =((a_fase-np.min(a_fase))/(np.max(a_fase)-np.min(a_fase)))*255
a_mod = np.abs(a)
a_mod = ((a_mod-np.min(a_mod))/(np.max(a_mod)-np.min(a_mod)))*255
a_mod = np.fft.fftshift (a_mod)

print (roi.shape)

a_fase = np.angle(a)
a_fase =((a_fase-np.min(a_fase))/(np.max(a_fase)-np.min(a_fase)))*255
# cv2.imshow('mod',a_fase)
cv2.waitKey(0)

b = np.zeros((451,815,3),np.uint8)
b [:64,:61,:] = roi
b = np.fft.fftn(b)
print (b.shape)

cor = a.conj()*b
cor = np.fft.ifftn(cor)

corr = signal.correlate(img,roi,mode='same',method ='fft')
# cor = np.fft.ifftn(corr)

print (corr.shape)
corr22 = np.convolve(img,roi,mode='same')
print (np.max(corr22)


# print (np.where( np.argmax(corr22)==corr22 ))

cv2.imwrite("corr.png",corr.real)

print (corr22)