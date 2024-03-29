# This Python file uses the following encoding: utf-8
import sys
import os
from pathlib import Path

sys.path.append('../')

from PySide6.QtGui import QGuiApplication, QImage, QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import QQuickImageProvider
from PySide6.QtCore import QObject, Signal, Slot, QSize, Qt

from threading import Lock
import cv2
import numpy as np

from modules.app_module_cv2 import AppCV2

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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


class Controlers(QObject):

    def __init__(self) -> None:
        super().__init__()
    
    @Slot(bool, int)
    def camera_selector(self, play, camera_type):
        global video_image
        global parnoramic_image
        global engine
        global new_image
        if play:
            if camera_type == 0:
                capture = cv2.VideoCapture(0,cv2.CAP_ANY)
                video_image = MyImageProvider(capture)
                parnoramic_image = MyPanoramicProvider()

            engine.addImageProvider("myprovider", video_image)
            # engine.addImageProvider("panoprovider", parnoramic_image)

        else:
            if camera_type==0:
                parnoramic_image.finish_capture()
                video_image.finish_capture()  
    @Slot()
    def panoramic_init(self):
        global video_image
        global parnoramic_image
        global engine
        global new_image
        # parnoramic_image = SpinnakerPanoramicProvider()
        engine.addImageProvider("panoprovider", parnoramic_image)

            
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    app.setWindowIcon(QIcon(('../resources/images/logo.png')))
    qml_file = os.fspath(Path(__file__).resolve().parent / "main.qml")
    
    controlers = Controlers()

    engine.load(qml_file)
    engine.rootObjects()[0].setProperty('controlers', controlers)
    
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
