# This Python file uses the following encoding: utf-8
import sys
import os
from pathlib import Path

from numpy import uint8

sys.path.append('../')

from apps.app_module_cv2 import AppCV2
from apps.app_module_spinnaker import AppSpinnaker

from PySide6.QtGui import QGuiApplication, QImage
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import QQuickImageProvider
from PySide6.QtCore import QObject, Signal, Slot, QSize, Qt

from threading import Lock
import cv2
import numpy as np

new_image = np.zeros((640,480,3),dtype="uint8")
ret = False
app_camera = None
parnoramic_image = None
video_image = None


class MyImageProvider(QQuickImageProvider):

    def __init__(self, capture_object): # -> None:
        super(MyImageProvider, self).__init__(QQuickImageProvider.Image)
        self.cvimg = []
        self.capture = capture_object
        self._lock = Lock()

    def requestImage(self, p_str, size, u):
        global new_image
        global ret
        ret,self.frame = self.capture.read()
        with self._lock:
            new_image = self.frame
        self.height, self.width, self.depth = self.frame.shape
        self.cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.cvimg = QImage (self.cvimg.data, self.width, self.height, self.width*self.depth, QImage.Format_RGB888)       
        return self.cvimg

    def finish_capture(self):
        self.capture.release()
        self.frame = np.zeros((640,480,3),dtype="uint8")
        self.height, self.width, self.depth = self.frame.shape
        self.cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.cvimg = QImage (self.cvimg.data, self.width, self.height, self.width*self.depth, QImage.Format_RGB888)           


class MyPanoramicProvider(QQuickImageProvider):

    def __init__(self):#  -> None:
        super(MyPanoramicProvider, self).__init__(QQuickImageProvider.Image)
        self.cvimg = []
        self.capture = []
        self._build_panoramic = AppCV2()
        self._lock = Lock()
        self._panoramic = np.zeros((640,480,3),dtype="uint8")

    def requestImage(self, p_str, size, u):
        global new_image
        global ret
        # self._build_panoramic._new_image = new_image
        with self._lock:
            self.frame, growing_flag = self._build_panoramic.panoramic_build(new_image, ret)
        self.height, self.width, self.depth = self.frame.shape
        self.cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.cvimg = QImage (self.cvimg.data, self.width, self.height, self.width*self.depth, QImage.Format_RGB888)       
        # self.cvimg.scaled(QSize(300, 200),aspectMode = Qt.AspectRatioMode.KeepAspectRatio)
        return self.cvimg
    
    def finish_capture(self):
        self._build_panoramic.variables_restart()
        self.frame = np.zeros((640,480,3),dtype="uint8")
        self.height, self.width, self.depth = self.frame.shape
        self.cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.cvimg = QImage (self.cvimg.data, self.width, self.height, self.width*self.depth, QImage.Format_RGB888)       
        # self.cvimg.scaled(QSize(300, 200),aspectMode = Qt.AspectRatioMode.KeepAspectRatio)


class SpinnakerImageProvider(QQuickImageProvider):

    def __init__(self, app_spinnaker) -> None:
        super(SpinnakerImageProvider, self).__init__(QQuickImageProvider.Image)
        self.cvimg = []
        
        self._lock = Lock()

        self.capture = app_spinnaker

    def requestImage(self, p_str, size, u):
        global new_image
        global ret

        ret = self.capture.main()

        with self._lock:
            self.frame = self.capture.new_image
            new_image = self.frame
        self.height, self.width, self.depth = self.frame.shape
        self.cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.cvimg = QImage (self.cvimg.data, self.width, self.height, self.width*self.depth, QImage.Format_RGB888)       
        return self.cvimg
    
    def finish_capture(self):
        # @TODO: Puede ser que esté conectandose y desconectándose de la cámara en cada captura. Estar atento.
        # self.capture.release() 
        self.frame = np.zeros((640,480,3),dtype="uint8")
        self.height, self.width, self.depth = self.frame.shape
        self.cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.cvimg = QImage (self.cvimg.data, self.width, self.height, self.width*self.depth, QImage.Format_RGB888)           


class SpinnakerPanoramicProvider(QQuickImageProvider):

    def __init__(self) -> None:
        super(SpinnakerPanoramicProvider, self).__init__(QQuickImageProvider.Image)
        self.cvimg = []
        
        self._build_panoramic = AppSpinnaker()
    def requestImage(self, p_str, size, u):
        global new_image
        global ret
        self.frame, growing_flag = self._build_panoramic.panoramic_build(new_image, ret) #self.capture.new_image, ret)  
        self.height, self.width, self.depth = self.frame.shape
        self.cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.cvimg = QImage (self.cvimg.data, self.width, self.height, self.width*self.depth, QImage.Format_RGB888)       
        return self.cvimg

    def finish_capture(self):
        self._build_panoramic.variables_restart()
        self.frame = np.zeros((640,480,3),dtype="uint8")
        self.height, self.width, self.depth = self.frame.shape
        self.cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.cvimg = QImage (self.cvimg.data, self.width, self.height, self.width*self.depth, QImage.Format_RGB888)

class Controlers(QObject):

    def __init__(self) -> None:
        super().__init__()
    
    @Slot(bool, int)
    def camera_selector(self, play, camera_type):
        global video_image
        global parnoramic_image
        global engine
        # global app_camera
        global new_image
        if play:
            if camera_type==0:
                capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
                video_image = MyImageProvider(capture)
                
                parnoramic_image = MyPanoramicProvider()
                engine.addImageProvider("myprovider", video_image)
                engine.addImageProvider("panoprovider", parnoramic_image)
            if camera_type == 1:
                app_camera = AppSpinnaker()
                video_image_spinnaker = SpinnakerImageProvider(app_camera)
                parnoramic_image = SpinnakerPanoramicProvider()
                engine.addImageProvider("myprovider", video_image_spinnaker)
                engine.addImageProvider("panoprovider", parnoramic_image)

                # capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
                # video_image = MyImageProvider(capture)
                # parnoramic_image = MyPanoramicProvider()
                # engine.addImageProvider("myprovider", video_image)
                # engine.addImageProvider("panoprovider", parnoramic_image)
        else:
            if camera_type==0:
                parnoramic_image.finish_capture()
                video_image.finish_capture()  
                
            
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    qml_file = os.fspath(Path(__file__).resolve().parent / "main.qml")
    
    # app_cv2 =  AppCV2()
    # video_image = MyImageProvider( app_cv2)
    # parnoramic_image = MyPanoramicProvider( app_cv2 )
    controlers = Controlers()
    # video_image_spinnaker = SpinnakerImageProvider(AppSpinnaker())
    # engine.addImageProvider("myprovider", video_image)
    # engine.addImageProvider("panoprovider", parnoramic_image)
    # engine.rootObjects()[0].setProperty('controlers', controlers)

    engine.load(qml_file)
    engine.rootObjects()[0].setProperty('controlers', controlers)
    
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())