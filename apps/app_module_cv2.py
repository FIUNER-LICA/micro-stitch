from sys import path

path.append('../')

from modules.globals_DTO import *
from modules.mask_extracting import Mask
import modules.panoramic_acquisition as pac
import modules.frame_validation as f_val
import numpy as np
from threading import Event, Thread

class AppCV2:
    def __init__(self) -> None:
        
        self._is_first_image = True
        self._focus = True
        self._growing = True

        self._last_image = []
        self._mask_object = Mask()
        self._panoramic = np.zeros((640,480,3),dtype="uint8")
        self._new_image = np.zeros((640,480,3),dtype="uint8")

        self._image_stack =[]# np.zeros((640,480,3),dtype="uint8")

        # Bandera para activar/desactivar el pre-análisis
        self._image_analisys = False
        if self._image_analisys:
            self._new_image_capture = Event()
            self._pre_analisys = Thread (target= self.focus_analisys, daemon=True, args=(0,0))
            self._pre_analisys.start()

    def focus_analisys(self, threshold, args):
        while (True):
            self._new_image_capture.wait()
            try:
                
                focus_value = f_val.focus_validation(self._new_image, args)
                if focus_value[1] > threshold:
                    print (focus_value[1], threshold)
                    self._focus=True
                else:
                    self._focus = False 
            except: 
                print ("Error en cálculo de foco. Revise los parámetros.")
            self._new_image_capture.clear()

    def panoramic_build(self, new_image, ret = False):
        global R
        global C
        self._new_image = new_image

        if self._image_analisys:
            self._new_image_capture.set() 
    
        if ret:
        #Dar inicio al stream y formación de panorámica
            if (not self._is_first_image) and self._focus:
                try:           
                    # self._image_stack.append(self._new_image)
                    self._panoramic, self._growing, R, C = pac.build(self._panoramic, self._last_image, self._new_image, self._mask_object, R, C)
                    if self._growing:
                        self._last_image = self._new_image# .copy() # @todo: Se puede sacar el .copy() SI NO SE AGREGO LA NUEVA IMAGEN NO DEBE ASIGNARSE A LAST IMAGE
                except:
                    pass

            if self._is_first_image:
                self._panoramic = self._new_image.copy()
                self._last_image = self._new_image.copy()
                self._is_first_image = False
        
        return self._panoramic, self._growing
    
    def variables_restart(self):
        global R
        global C
        R = 0
        C = 0

        self._is_first_image = True
        self._focus = True
        self._growing = True

        self._last_image = []
        self._mask_object = Mask()
        self._panoramic = np.zeros((640,480,3),dtype="uint8")
        self._new_image = np.zeros((640,480,3),dtype="uint8")

        self._image_stack =[]# np.zeros((640,480,3),dtype="uint8")

        # Bandera para activar/desactivar el pre-análisis
        self._image_analisys = False
        print ("variables reestablecidas")