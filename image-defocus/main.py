from mainwindow_ui import *
from PyQt5.QtGui import QPixmap, QImage
from cv2 import cv2
import time

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.image = cv2.imread("lena_256.jpg",cv2.IMREAD_GRAYSCALE)
        # self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        self.z_pos = 0.0
        self.defocus = self.changeFocus()
        self.actionCerrar.triggered.connect(self.salirApp)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showImage)
        self.timer.start(1)
        self.ImageInfo = "Image info"
        self.startTime=time.time()
        self.endTime=time.time()
    
    def salirApp(self):
        exit()
        
    def resizeEvent(self, event):
        self.labelImage.resize(self.width(), self.height())
   
    def changeFocus(self):
        return pow(self.z_pos,2)

    def showImage(self):
        image_aux = cv2.GaussianBlur(self.image,(5,5),self.changeFocus())
        qimage_aux = QImage(image_aux, image_aux.shape[1], image_aux.shape[0],                                                                                                                                                 
                     QImage.Format_Grayscale8)                                                                                                                                                                 
        pixmap = QPixmap(qimage_aux)
        # self.labelImage.setScaledContents(True)
        self.labelImage.setPixmap(pixmap.scaled(self.labelImage.width(),
                                   self.labelImage.height(),QtCore.Qt.KeepAspectRatio))
        self.elapsedtime = self.endTime-self.startTime
        aux_lap_var = cv2.Laplacian(image_aux,cv2.CV_64F,0).var()
        # aux_lap_sob = cv2.Sobel(image_aux,cv2.CV_64F,1,0,ksize=5).var()
        self.ImageInfo = ("Image info:\n" +
                          "Varianza Lap.: " +str(aux_lap_var) + "\n"
                        #   "Varianza Sob.: " +str(aux_lap_sob) + "\n"
                          "Tiempo: "  + str(1.0/self.elapsedtime) +"\n"  
                          "Z-pos: "  + str(self.z_pos) +"\n"  )
        self.labelInfo.setText(self.ImageInfo)
        self.startTime=self.endTime
        self.endTime=time.time()

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Up):
            self.z_pos+=0.1
        if (event.key() == QtCore.Qt.Key_Down):
            self.z_pos-=0.1
        if (event.key() == QtCore.Qt.Key_Q):
            self.close()
  
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()