from cv2 import cv2
import numpy as np
from scipy import signal
from scipy.ndimage import correlate
import matplotlib.pyplot as plt



img = cv2.imread("FigurasGeom.tif",cv2.IMREAD_GRAYSCALE) # 815 x 451

roi = cv2.imread("roi_fig.tif",cv2.IMREAD_GRAYSCALE) #61 x 64
cv2.imwrite("roi1.png",roi)

a = np.fft.fftn(img)
# a = np.abs (a)
#a_fase = np.arctan (a.imag/(a.real+0.000001))
# a_fase =((a_fase-np.min(a_fase))/(np.max(a_fase)-np.min(a_fase)))*255
a_mod = np.abs(a)
a_mod = ((a_mod-np.min(a_mod))/(np.max(a_mod)-np.min(a_mod)))*255
# a_mod = np.fft.fftshift (a_mod)
a_mod = np.fft.fftn (a_mod)

print (roi.shape)

a_fase = np.angle(a)
a_fase =((a_fase-np.min(a_fase))/(np.max(a_fase)-np.min(a_fase)))*255
# cv2.imshow('mod',a_fase)
cv2.waitKey(0)

b1 = np.zeros((451,815),np.uint8)
b1 [:64,:61] = roi
b = np.fft.fftn(b1)
b = np.abs (b)

print (b.shape)

cor = a*b.conj()
cor = np.fft.ifftn(cor)
corr = signal.correlate(img,roi,mode='same',method ='fft') #scipy
# print (np.where (corr == np.amax(corr)))

print (corr.shape)

cv2.imwrite("cor.png",corr.real)

cor2 = cor
cor2 = np.abs (cor2)
# cor2 = np.rot90 (cor2)
# cor2 = np.rot90 (cor2)
print (cor2.shape) # 2D
print (np.amax(cor2))
print (np.where (cor2 == np.amax(cor2)))

plt.subplot(2,2,1)
plt.imshow(roi)

plt.subplot(2,2,2)
plt.imshow(img)
plt.plot(351, 101, '*')

plt.subplot(2,2,3)
plt.imshow (b1)

plt.subplot(2,2,4)
plt.imshow (cor2)
plt.plot(351, 101, '*')

plt.show()

