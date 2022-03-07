from mainwindow_ui import *
import numpy as np
import pylint
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from cv2 import cv2
import time

class funciones ():
    def __init__(self):
        self.test()

    def newmatriz (self):
        self.matriz =[]

        for i in range(512):
            self.matriz.append([])
            for j in range(512):
                self.matriz[i].append(0)

        for i in range(241, 271):
            for j in range(241, 271):
                self.matriz[i][j]=1
    
        return self.matriz

    def newmatriz2 (self, matriz):
        pass
        # #self.matriz =[]
        # # for i in range(241, 271):
        # #     for j in range(241, 271):
        # for i in range(70, 100):
        #     for j in range(70, 100):
        #         matriz[i][j][0]=255
        #         matriz[i][j][1]=255
        #         matriz[i][j][2]=255


        # return matriz

    def test(self):
        
        self.imgs = []
        self.matriz =[]
        self.matriz = self.newmatriz()
        self.pano=[]
        # print(self.matriz[256])
        self.dsize = 1
        self.imgs = self.matriz

        self.imgs = cv2.imread("Lenna.png")
        self.imgs1 = self.imgs#cv2.imread("prueba.png")
        self.stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS) # crea un objeto de la clase stitcher, en un escenario (modo) dado por scans/panorama
        self.stitcher.setRegistrationResol(0.2)         #tiene como parámetro: "double"
        self.stitcher.setSeamEstimationResol(2)         #tiene como parámetro: "double"
        self.stitcher.setCompositingResol(1.2)          #tiene como parámetro: "double"
        self.stitcher.setPanoConfidenceThresh(2.0)      #tiene como parámetro: "double"
        self.stitcher.setWaveCorrection(0)              #tiene como parámetro: "double"
        self.stitcher.setInterpolationFlags(3)          #tiene como parámetro: "InterpolationFlags interp_flags"
        #self.stitcher.detail_waveCorrectKind()              #tiene como parámetro: "detail::WaveCorrectKind kind"
        #self.stitcher.setFeaturesFinder(4)              #tiene como parámetro: "Ptr<Feature2D> features_finder"
        
        self.warper = cv2.WarperCreator()
        self.im = [self.imgs, self.imgs1]


        # self.stitched = cv2.copyMakeBorder(self.stitched, 10, 10, 10, 10,
		# 	cv2.BORDER_CONSTANT, (0, 0, 0))

        # print (type(self.imgs))
        # print (type(self.matriz))
        # print (self.imgs.ndim)
        # print (self.imgs.shape)
        # #print (self.imgs)
        self.a=np.zeros_like(self.imgs)
        # self.a=np.zeros(self.imgs.shape, dtype = self.imgs.dtype) #matriz parecida a imgs llena de ceros
        print (self.a.shape)
        self.a=self.newmatriz2(self.a)
        # retval	=	cv.detail.overlapRoi(	tl1, tl2, sz1, sz2, roi	)
        self.um = cv2.UMat()
        
        # keypoints, descriptors	=	cv.Feature2D.compute(self.imgs, keypoints[, descriptors]	)
        
        # self.sift_obj = cv2.xfeatures2d.SURF_create()
        # self.descriptors, self.keypoints = self.sift_obj.detectAndCompute(self.im, None)
        # self.retval = cv2.Stitcher.estimateTransform(self.stitcher,self.a)
        # print (self.retval)
        # #self.stitcher.Match_images()
        # #self.stitcher.estimateCameraParams()
        # print (self.a)
        # print (type(self.a))
        # print (np.max(self.a))
        # self.retval= cv2.getAffineTransform(UMat, UMat) --> src = coordenadas de vertices imagen actual, dst = coordenadas de vertices imagen siguiente
        # print (self.descriptors, self.keypoints)
        self.stitcher.stitch(self.imgs, self.a) #puede recibir otros parámetros: InputArrayOfArrays images, InputArrayOfArrays masks, OutputArray pano
        
        
        
        # self.sift = cv2.Feature2D.empty()

        # self.puntos_clave, self.descriptores	=	cv2.Feature2D.detectAndCompute (self.imgs, self.a)        

        print ('test ok')
        # cv2.imwrite("prueba.png",self.a)
if __name__ == "__main__":
    a = funciones()
    
