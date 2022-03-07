from mainwindow_ui import *
import numpy as np
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from cv2 import cv2
import time

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        try:
            self.image = cv2.imread("Lenna.png")
            self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        finally:
            self.roi_x_pos=50
            self.roi_y_pos=50
            self.roi_dx=150
            self.roi_dy=150
            self.img_width=self.image.shape[1]
            self.img_height=self.image.shape[0]
            self.roi_step=10
            self.roi=self.image[self.roi_x_pos:self.roi_x_pos+self.roi_dx,
                                self.roi_y_pos:self.roi_y_pos+self.roi_dy,:]
            self.roi = cv2.cvtColor(self.roi,cv2.COLOR_BGR2RGB)
            self.timer = QtCore.QTimer()
            self.imgs = []
            self.bi_pano = []
            self.pano = []
            self.timer.timeout.connect(self.newFrame)
            self.timer.start(1)
            self.stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
            self.color_status = Qt.green
            self.stitcher.setWaveCorrection(False) # poniendo en True genera problemas
            self.stitcher.setRegistrationResol(1.0)
            # stitcher.setSeamEstimationResol(0.1)
            self.stitcher.setCompositingResol(1.0)
            # stitcher.setPanoConfidenceThresh(1)
            # stitcher.setSeamFinder(new detail::GraphCutSeamFinder(detail::GraphCutSeamFinderBase::COST_COLOR));
            # stitcher.setBlender(detail::Blender::createDefault(detail::Blender::MULTI_BAND, false));
            # self.stitcher.ExposureCompensator(cv2.detail.EXPOSURE_COMPENSATOR_NO)
            # stitcher.setWaveCorrection(true);
            # stitcher.setWaveCorrectKind(detail::WAVE_CORRECT_HORIZ);
            # stitcher.setFeaturesMatcher(
            #         new detail::BestOf2NearestMatcher(false, 0.3, 6, 6));
            # stitcher.setBundleAdjuster(new detail::BundleAdjusterRay());
            self.startTime=time.time()
            self.endTime=time.time()
            self.frcounter=1
    
    def buildBiPano(self):
        imgs_aux = []
        if len(self.imgs)<1:
             self.imgs.append(self.roi)
        else:
            imgs_aux.append(self.imgs[-1])
            imgs_aux.append(self.roi)
            err=np.sum(np.square(imgs_aux[1]-imgs_aux[0]))/np.sum(imgs_aux[1])
            if err > 0.2:
                print("err: ",err)
                status, aux_pano = self.stitcher.stitch(imgs_aux)
                if status == cv2.Stitcher_OK:
                    self.color_status = Qt.green
                    self.bi_pano = aux_pano
                    self.imgs.append(self.roi)
                    print("Pano size: ",len(self.imgs))
                else:
                    self.color_status = Qt.red
            
    def buildPano(self):
        self.startTime=time.time()
        if len(self.imgs)>1:
            status, aux_pano = self.stitcher.stitch(self.imgs)
            if status == cv2.Stitcher_OK:
                self.pano = aux_pano
                self.qpano=QImage(self.pano.data,
                                  self.pano.shape[1],
                                  self.pano.shape[0],
                                  3*self.pano.shape[1],                                                                                                                                               
                                  QImage.Format_RGB888)
                pano_pixmap = QPixmap(self.qpano)
                self.lStitching.setPixmap(pano_pixmap.scaled(self.lStitching.width(),
                                        self.lStitching.height(),QtCore.Qt.KeepAspectRatio))
        self.endTime=time.time()     
        print("Tiempo:", self.endTime-self.startTime)
        self.startTime=self.endTime
  
    def newFrame(self):
        self.roi=self.image[self.roi_y_pos:self.roi_y_pos+self.roi_dy,
                                self.roi_x_pos:self.roi_x_pos+self.roi_dx] 
        # self.roi = cv2.cvtColor(self.roi,cv2.COLOR_RGB2BGR) # una roi requiere conversión para mostrar
        # mean = 0
        # var = 0.0
        # sigma = 1
        # gauss = np.random.normal(mean,sigma,self.roi.shape)
        # gauss = gauss.reshape(self.roi.shape[0],self.roi.shape[1],self.roi.shape[2])
        # self.roi = np.clip(self.roi + gauss,0,255)
        # self.roi =  cv2.convertScaleAbs(self.roi, alpha=255/1)
        
        
        self.buildBiPano()
        self.endTime=time.time()
        if (self.frcounter==1):
            self.statusBar().showMessage("Frame Rate Pano: "+ str(self.frcounter/(self.endTime-self.startTime)))
            self.startTime=self.endTime    
            self.frcounter=1
        else:
            self.frcounter+=1
     
    def resizeEvent(self, event):
        self.lBigImage.resize(self.width()/2, self.height())
        self.lStitching.setGeometry(self.lBigImage.width()+10,self.lBigImage.y(),self.width()-10, self.height())
        
        

        self.lStitching.resize(self.width(), self.height())
        # self.line.setGeometry(self.width(),0,20,self.height())
        
        self.update()
   
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Down):
            if ((self.roi_y_pos+self.roi_dy+self.roi_step)<=self.img_height):
                self.roi_y_pos+=self.roi_step
        if (event.key() == QtCore.Qt.Key_Up):
            if ((self.roi_y_pos-self.roi_step)>0):
                self.roi_y_pos-=self.roi_step
        if (event.key() == QtCore.Qt.Key_Left):
            if ((self.roi_x_pos-self.roi_step)>0):
                self.roi_x_pos-=self.roi_step
        if (event.key() == QtCore.Qt.Key_Right):
            if ((self.roi_x_pos+self.roi_dx+self.roi_step)<=self.img_width):
                self.roi_x_pos+=self.roi_step    
        
        if (event.key() == QtCore.Qt.Key_P):
            self.buildPano()

        
        if (event.key() == QtCore.Qt.Key_Q):
            self.close()
        
    def paintEvent(self, event):
        
        self.qimage = QImage(self.image, self.image.shape[1],
                             self.image.shape[0],                                                                                                                                                 
                             QImage.Format_RGB888)
        painter = QPainter(self.qimage)
        painter.setPen(QPen(self.color_status,  1, Qt.DashLine))
        painter.drawRect(self.roi_x_pos,self.roi_y_pos,self.roi_dx,self.roi_dy)
        pixmap = QPixmap(self.qimage)
        
        self.lBigImage.setPixmap(pixmap.scaled(self.lBigImage.width(),
                                 self.lBigImage.height(),QtCore.Qt.KeepAspectRatio))

        # self.qroi=QImage(self.roi.data,
        #                  self.roi.shape[1],
        #                  self.roi.shape[0],
        #                  3*self.roi.shape[1],                                                                                                                                               
        #                  QImage.Format_RGB888)
        # roi_pixmap = QPixmap(self.qroi)
        # self.lStitching.setPixmap(roi_pixmap.scaled(self.lStitching.width(),
        #                            self.lStitching.height(),QtCore.Qt.KeepAspectRatio))
        if not (self.pano is None):
            if len(self.pano)>0:
                self.qpano=QImage(self.pano.data,
                                  self.pano.shape[1],
                                  self.pano.shape[0],
                                  3*self.pano.shape[1],                                                                                                                                               
                                  QImage.Format_RGB888)
                pano_pixmap = QPixmap(self.qpano)
                self.lStitching.setPixmap(pano_pixmap.scaled(self.lStitching.width(),
                                  self.lStitching.height(),QtCore.Qt.KeepAspectRatio))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()