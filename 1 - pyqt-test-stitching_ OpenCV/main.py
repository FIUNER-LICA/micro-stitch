from mainwindow_ui import *
import numpy as np
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from cv2 import cv2
import time

def calcularTiempo(func): 
# tomamos los argumentos de la función
    def inner(*args, **kwargs): 
    # Tiempo actual
        begin = time.time() 
    # Llamada a la función  
        res = func(*args, **kwargs) 
    # Tiempo final
        end = time.time() 
        print("Tiempo total de la función: ", func.__name__, end - begin)
        return res
    return inner

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        try:
            
            #self.image = cv2.imread("DSC00290.JPG")
            self.image = cv2.imread("Lenna.png") # poner menu
            self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
            #self.image = cv2.imread("Captura.PNG", cv2.IMREAD_UNCHANGED) # poner menu
            #self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2BGRA) #ENCONTRAR EL FORMATO DE IMG
                                                                    #enganchar openc cv y pyqtgraph
        finally:
            self.roi_x_pos=50
            self.roi_y_pos=50
            #self.roi_dx=500
            #self.roi_dy=500
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
            self.stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS) # crea un objeto de la clase stitcher, en un escenario (modo) dado por scans/panorama
            self.color_status = Qt.green
            self.stitcher.setWaveCorrection(False) # poniendo en True genera problemas
            self.stitcher.setRegistrationResol(1.0)
            #self.stitcher.setSeamEstimationResol(0.1)
            self.stitcher.setCompositingResol(1.0)
            #self.stitcher.setPanoConfidenceThresh(1)
            #self.adjuster = cv2.detail_BundleAdjusterReproj()
            #self.retval	=	cv2.detail.stitchingLogLevel()
#            self.pwarpe = cv2.RotationWarper_create(2.0)
#            self.stitcher.setWarper(self.pwarpe)
            #self.stitcher.panoConfidenceThresh()
            # stitcher.setSeamFinder(new detail::GraphCutSeamFinder(detail::GraphCutSeamFinderBase::COST_COLOR));
            #stitcher.setBlender(detail::Blender::createDefault(detail::Blender::MULTI_BAND, false))
            # self.stitcher.ExposureCompensator(cv2.detail.EXPOSURE_COMPENSATOR_NO)
            # stitcher.setWaveCorrectKind(detail::WAVE_CORRECT_HORIZ);
            # stitcher.setFeaturesMatcher(
            #         new detail::BestOf2NearestMatcher(false, 0.3, 6, 6));
            # stitcher.setBundleAdjuster(new detail::BundleAdjusterRay());
            self.startTime=time.time()
            self.endTime=time.time()
            self.frcounter=1
            
            self.bandera = True
            self.mascara = []
            self.l = True

    def newmatriz2 (self,matriz):
        for i in range(0,2):
            for j in range(70, 75):
                for k in range(70, 75):
                    matriz[i][j][k][0]=255
                    matriz[i][j][k][1]=255
                    matriz[i][j][k][2]=255
        return matriz

    def buildBiPano(self):
        imgs_aux = []
        if len(self.imgs)<1:
             self.imgs.append(self.roi)
        else:
            imgs_aux.append(self.imgs[-1])
            imgs_aux.append(self.roi)
#           
            if self.bandera:
                a=np.zeros_like(imgs_aux) #matriz parecida a imgs llena de ceros
                a =self.newmatriz2(a)
                self.mascara = a
                cv2.imwrite("prueba.png",a[1])
                self.bandera = False
            a = self.mascara
#
            err=np.sum(np.square(imgs_aux[1]-imgs_aux[0]))/np.sum(imgs_aux[1])
            if err > 0.2:
                print("err: ",err)
                status, aux_pano = self.stitcher.stitch(imgs_aux,a)
                if status == cv2.Stitcher_OK:
                    self.color_status = Qt.green
                    self.bi_pano = aux_pano
                    self.imgs.append(self.roi)
                    print("Pano size: ",len(self.imgs))
                else:
                    self.color_status = Qt.red
    @calcularTiempo         
    def buildPano(self):
        self.startTime=time.time()
        if len(self.imgs)>1:
            status, aux_pano = self.stitcher.stitch(self.imgs,self.mascara) #devuelve un estado y la imagen unida/armada
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
        #self.roi = cv2.cvtColor(self.roi,cv2.COLOR_BGRA2BGR) # una roi requiere conversión para mostrar// "Captura"
        #self.roi = cv2.cvtColor(self.roi,cv2.COLOR_RGB2BGR) # "Lenna"
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
        
        if (event.key() == QtCore.Qt.Key_P):       #hacer que los descriptores (o invariantes) una vez creada la panoramica 
           self.buildPano()                       #queden solamente algunos o los que son mas comunes entre las roi capturadas
                                                    #-- o si ya paso por algun lugar que reconozca rapido y no haga todo el procesamiento de nuevo
                                                    #es decir que no se gaste en reconstruir(o agregar el ultimo roi a los calculos)
                                                    #de nuevo y que deje como estába
        if (event.key() == QtCore.Qt.Key_Q):
            self.close()
        
    def paintEvent(self, event):
        
        self.qimage = QImage(self.image, self.image.shape[1],
                             self.image.shape[0],                                                                                                                                                 
                             QImage.Format_RGB888)
                             #QImage.Format_ARGB32) #para la imagen "Captura"
        painter = QPainter(self.qimage)
        painter.setPen(QPen(self.color_status,  1, Qt.DashLine))
        painter.drawRect(self.roi_x_pos,self.roi_y_pos,self.roi_dx,self.roi_dy)
        pixmap = QPixmap(self.qimage)
        
        self.lBigImage.setPixmap(pixmap.scaled(self.lBigImage.width(),
                                 self.lBigImage.height(),QtCore.Qt.KeepAspectRatio))

        #self.qroi = QImage(self.roi.data,                                                 #
        #                 self.roi.shape[1],
        #                self.roi.shape[0],
        #                3*self.roi.shape[1],                                                                                                                                               
        #                QImage.Format_RGB888)
        #roi_pixmap = QPixmap(self.qroi)
        #self.lStitching.setPixmap(roi_pixmap.scaled(self.lStitching.width(),
        #                            self.lStitching.height(),QtCore.Qt.KeepAspectRatio))   #
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