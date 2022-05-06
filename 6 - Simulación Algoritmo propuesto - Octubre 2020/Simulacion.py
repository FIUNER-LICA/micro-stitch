from torch import rand, randint
from mainwindow_ui import *
import numpy as np
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from cv2 import cv2
from Funciones import PanoCam
import time
import datetime
import random

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        try:
            self.image = cv2.imread("2.jpg") # poner menu
            self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        finally:
            self.roi_x_pos=600
            self.roi_y_pos=600
            self.roi_dx=640
            self.roi_dy=480
            self.img_width=self.image.shape[1]
            self.img_height=self.image.shape[0]
            self.roi_step=60
            self.roi=self.image[self.roi_x_pos:self.roi_x_pos+self.roi_dx,
                                self.roi_y_pos:self.roi_y_pos+self.roi_dy,:]
            
            self.roi = cv2.cvtColor(self.roi,cv2.COLOR_BGR2RGB)
            self.last_frame = self.image[self.roi_x_pos:self.roi_x_pos+self.roi_dx,
                                self.roi_y_pos:self.roi_y_pos+self.roi_dy,:]
            self.panoramica = self.image[self.roi_y_pos:self.roi_y_pos+self.roi_dy,
                                self.roi_x_pos:self.roi_x_pos+self.roi_dx,:]
            self.X = 0
            self.Y = 0
            self.r = 40
            self.frcounter=1
            self.timer = QtCore.QTimer()
            self.imgs = []
            self.bi_pano = []
            self.pano = []
            self.timer.timeout.connect(self.newFrame)
            self.timer.start(1)            
            self.color_status = Qt.green

    def buildBiPano(self):
        self.x1=int(self.last_frame.shape[0]/2)
        self.y1=int(self.last_frame.shape[1]/2) 
        self.panoramica, self.X, self.Y= PanoCam.panoCam(self.panoramica, self.last_frame, self.roi, self.X, self.Y, self.r, self.x1, self.y1)
        self.last_frame = self.roi
        self.qpanoramica=QImage(bytes(self.panoramica), 
                         self.panoramica.shape[1],
                         self.panoramica.shape[0],
                         3*self.panoramica.shape[1],
                         QImage.Format_RGB888)
        pano_pixmap = QPixmap(self.qpanoramica)
        self.lStitching.setPixmap(pano_pixmap.scaled(self.lStitching.width(),
                                self.lStitching.height(),QtCore.Qt.KeepAspectRatio))

    def newFrame(self):
        self.roi=self.image[self.roi_y_pos:self.roi_y_pos+self.roi_dy,
                                self.roi_x_pos:self.roi_x_pos+self.roi_dx].copy() 
        # if random.randint(0,100)<10:
        #     self.roi[self.roi < 20] = 0
        #     self.roi -=20
            
                
        self.buildBiPano()
        self.endTime=time.time()
        if (self.frcounter==1):
            self.startTime=self.endTime    
            self.frcounter=1
        else:
            self.frcounter+=1


    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Down):
            if ((self.roi_y_pos+self.roi_dy+self.roi_step)<=self.img_height):
                self.roi_y_pos+=self.roi_step
                self.buildBiPano()
        if (event.key() == QtCore.Qt.Key_Up):
            if ((self.roi_y_pos-self.roi_step)>0):
                self.roi_y_pos-=self.roi_step
                self.buildBiPano()
        if (event.key() == QtCore.Qt.Key_Left):
            if ((self.roi_x_pos-self.roi_step)>0):
                self.roi_x_pos-=self.roi_step
                self.buildBiPano()
        if (event.key() == QtCore.Qt.Key_Right):
            if ((self.roi_x_pos+self.roi_dx+self.roi_step)<=self.img_width):
                self.roi_x_pos+=self.roi_step  
                self.buildBiPano()
        
        if (event.key() == QtCore.Qt.Key_P):
            # fecha_y_hora = time.strftime("%c")
            # fecha = time.strftime("%x")
            # hora = time.strftime("%X")
            x = datetime.datetime.now()
            cv2.imwrite('./Panoramica_{}_{}_{}_{}_{}.jpg'.format(x.hour,x.minute,x.day,x.month, x.year), self.panoramica[:,:,::-1])
        if (event.key() == QtCore.Qt.Key_Q):
            self.close()

    def paintEvent(self, event):
        
        self.qimage = QImage(self.image, self.image.shape[1],
                            self.image.shape[0],                                                                                                                                                 
                            QImage.Format_RGB888)
                            # QImage.Format_ARGB32) #para la imagen "Captura"
        painter = QPainter(self.qimage)
        painter.setPen(QPen(self.color_status,  20, Qt.DashLine))
        painter.drawRect(self.roi_x_pos,self.roi_y_pos,self.roi_dx,self.roi_dy)
        pixmap = QPixmap(self.qimage)
        self.lBigImage.setPixmap(pixmap.scaled(self.lBigImage.width(),
                                 self.lBigImage.height(),QtCore.Qt.KeepAspectRatio))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()