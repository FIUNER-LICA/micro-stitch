from sys import path, exit
path.append('../')

from modules.mask_extracting import Mask
import modules.panoramic_acquisition as pac
from modules.globals_DTO import *

import cv2
import numpy as np
import datetime

import PySpin
import sys
import keyboard
from threading import Event, Thread
import time

capture_stack = Event()
new_image = np.zeros((640,480,3),dtype="uint8")
pano = True

global continue_recording
continue_recording = True

def handle_close(evt):
    """
    This function will close the GUI when close event happens.

    :param evt: Event that occurs when the figure closes.
    :type evt: Event
    """

    global continue_recording
    continue_recording = False

def save_stack():
    global new_image
    global capture_stack
    global pano
    numero_frame_stack = 0
    while (True):
        capture_stack.wait()
        pano = True
        time.sleep (0.1)
        cv2.imwrite('../data/manual_stack_thread/stack_3/frame_{}.tiff'.format(numero_frame_stack), new_image[:,:,:])
        numero_frame_stack += 1
        print ('Frame guardado')
        capture_stack.clear()

# def save_key():
#     global capture_stack
#     while (True):
#         if cv2.waitKey(1) & 0xFF == ord('s'):
#             capture_stack.set()

def acquire_and_display_images(cam, nodemap, nodemap_tldevice):
    """
    This function continuously acquires images from a device and display them in a GUI.

    :param cam: Camera to acquire images from.
    :param nodemap: Device nodemap.
    :param nodemap_tldevice: Transport layer device nodemap.
    :type cam: CameraPtr
    :type nodemap: INodeMap
    :type nodemap_tldevice: INodeMap
    :return: True if successful, False otherwise.
    :rtype: bool
    """
    global continue_recording

    sNodemap = cam.GetTLStreamNodeMap()

    # Change bufferhandling mode to NewestOnly
    node_bufferhandling_mode = PySpin.CEnumerationPtr(sNodemap.GetNode('StreamBufferHandlingMode'))
    if not PySpin.IsAvailable(node_bufferhandling_mode) or not PySpin.IsWritable(node_bufferhandling_mode):
        print('Unable to set stream buffer handling mode.. Aborting...')
        return False

    # Retrieve entry node from enumeration node
    node_newestonly = node_bufferhandling_mode.GetEntryByName('NewestOnly')
    if not PySpin.IsAvailable(node_newestonly) or not PySpin.IsReadable(node_newestonly):
        print('Unable to set stream buffer handling mode.. Aborting...')
        return False

    # Retrieve integer value from entry node
    node_newestonly_mode = node_newestonly.GetValue()

    # Set integer value from entry node as new value of enumeration node
    node_bufferhandling_mode.SetIntValue(node_newestonly_mode)

    print('*** IMAGE ACQUISITION ***\n')
    try:
        node_acquisition_mode = PySpin.CEnumerationPtr(nodemap.GetNode('AcquisitionMode'))
        if not PySpin.IsAvailable(node_acquisition_mode) or not PySpin.IsWritable(node_acquisition_mode):
            print('Unable to set acquisition mode to continuous (enum retrieval). Aborting...')
            return False

        # Retrieve entry node from enumeration node
        node_acquisition_mode_continuous = node_acquisition_mode.GetEntryByName('Continuous')
        if not PySpin.IsAvailable(node_acquisition_mode_continuous) or not PySpin.IsReadable(
                node_acquisition_mode_continuous):
            print('Unable to set acquisition mode to continuous (entry retrieval). Aborting...')
            return False

        # Retrieve integer value from entry node
        acquisition_mode_continuous = node_acquisition_mode_continuous.GetValue()

        # Set integer value from entry node as new value of enumeration node
        node_acquisition_mode.SetIntValue(acquisition_mode_continuous)

        print('Acquisition mode set to continuous...')

        #  Begin acquiring images
        #
        #  *** NOTES ***
        #  What happens when the camera begins acquiring images depends on the
        #  acquisition mode. Single frame captures only a single image, multi
        #  frame captures a set number of images, and continuous captures a
        #  continuous stream of images.
        #
        #  *** LATER ***
        #  Image acquisition must be ended when no more images are needed.
        cam.BeginAcquisition()

        print('Acquiring images...')

        #  Retrieve device serial number for filename
        #
        #  *** NOTES ***
        #  The device serial number is retrieved in order to keep cameras from
        #  overwriting one another. Grabbing image IDs could also accomplish
        #  this.
        device_serial_number = ''
        node_device_serial_number = PySpin.CStringPtr(nodemap_tldevice.GetNode('DeviceSerialNumber'))
        if PySpin.IsAvailable(node_device_serial_number) and PySpin.IsReadable(node_device_serial_number):
            device_serial_number = node_device_serial_number.GetValue()
            print('Device serial number retrieved as %s...' % device_serial_number)

        # Close program
        print('Press enter to close the program..')

        # Figure(1) is default so you can omit this line. Figure(0) will create a new window every time program hits this line
        # fig = plt.figure(1)
        
        # Close the GUI when close event happens
        # fig.canvas.mpl_connect('close_event', handle_close)

        # Retrieve and display images


        # Inicio de variablesm, parámetros y creación de objetos
        global R #Fila inicial del frame
        global C # Columna inicial del frame
        global capture_stack
        global new_image
        is_first_image = True
        flag_view  = True
        global pano

        mask_object = Mask()
        panoramic = np.zeros((640,480,3),dtype="uint8")

        storer = Thread (target = save_stack, daemon=True)#, args=())
        # press_key = Thread(target = save_key, daemon = True)
        # press_key.start()
        storer.start()
        # numero_frame_stack = 0
        while(continue_recording):
            try:
                #  Retrieve next received image
                #
                #  *** NOTES ***
                #  Capturing an image houses images on the camera buffer. Trying
                #  to capture an image that does not exist will hang the camera.
                #
                #  *** LATER ***
                #  Once an image from the buffer is saved and/or no longer
                #  needed, the image must be released in order to keep the
                #  buffer from filling up.
                # if (not is_first_image):
                    # capture_stack.wait()
                image_result = cam.GetNextImage(1000)

                #  Ensure image completion
                if image_result.IsIncomplete():
                    print('Image incomplete with image status %d ...' % image_result.GetImageStatus())

                else:                    
                    # Getting the image data as a numpy array
                    new_image = image_result.GetNDArray()
                    # Event to save image

                    if (not is_first_image):
                        try:
                            panoramic, growing = pac.build(panoramic, last_image, new_image, mask_object)

                            # cv2.imwrite('./stack/frame_{}.jpg'.format(numero_frame_stack), new_image[:,:,:])
                            # numero_frame_stack += 1
                            if growing: 
                                last_image = new_image
                                flag_view = True
                            else:
                                flag_view = False

                            # if growing:
                            #     capture_stack.set()

                        except:
                            flag_view = False
                            pass

                    if is_first_image and (cv2.waitKey(1) & 0xFF == ord('i')):
                        panoramic = new_image.copy()
                        last_image = new_image.copy()
                        is_first_image = False

                        capture_stack.set()

                    if flag_view:
                        pan_screen = cv2.resize(panoramic,(640,480))
                        frame_screen=cv2.resize(new_image,(640,480))
                        frame_screen = cv2.cvtColor(frame_screen, cv2.COLOR_RGB2BGR)
                        pan_screen = cv2.cvtColor(pan_screen,cv2.COLOR_RGB2BGR)
                        hor_cat = cv2.hconcat([frame_screen,pan_screen])
                        cv2.imshow('Resultado con camara FLIR',hor_cat)

                    if cv2.waitKey(1) & 0xFF == ord('p'):
                        x = datetime.datetime.now()
                        cv2.imwrite('../data/manual_stack_thread/stack_3/panoramic_flir_{}_{}_{}_{}_{}.tiff'.format(x.hour,
                                                            x.minute,x.day,x.month, x.year), panoramic[:,:,:])
                        print ("Seguir con adquisición: No")
                        continue_recording=False 
                    
                    if cv2.waitKey(1) & 0xFF == ord('s'):
                        capture_stack.set()

                    if keyboard.is_pressed('ENTER'):
                        print('Program is closing...')
                        
                        # Close figure
                        input('Done! Press Enter to exit...')
                        cv2.destroyAllWindows()
                        continue_recording=False             

                #  Release image
                #
                #  *** NOTES ***
                #  Images retrieved directly from the camera (i.e. non-converted
                #  images) need to be released in order to keep from filling the
                #  buffer.
                image_result.Release()

            except PySpin.SpinnakerException as ex:
                print('Error: %s' % ex)
                return False

        #  End acquisition
        #
        #  *** NOTES ***
        #  Ending acquisition appropriately helps ensure that devices clean up
        #  properly and do not need to be power-cycled to maintain integrity.
        cam.EndAcquisition()

    except PySpin.SpinnakerException as ex:
        print('Error: %s' % ex)
        return False

    return True


def run_single_camera(cam):
    """
    This function acts as the body of the example; please see NodeMapInfo example
    for more in-depth comments on setting up cameras.

    :param cam: Camera to run on.
    :type cam: CameraPtr
    :return: True if successful, False otherwise.
    :rtype: bool
    """
    try:
        result = True

        nodemap_tldevice = cam.GetTLDeviceNodeMap()

        # Initialize camera
        cam.Init()

        # Retrieve GenICam nodemap
        nodemap = cam.GetNodeMap()

        # Configurando formato de imagen
        if cam.PixelFormat.GetAccessMode() == PySpin.RW:
            cam.PixelFormat.SetValue(PySpin.PixelFormat_RGB8)
            print('Pixel format set to %s...' % cam.PixelFormat.GetCurrentEntry().GetSymbolic())

        else:
            print('Pixel format not available...')
            result = False

        # Acquire images
        result &= acquire_and_display_images(cam, nodemap, nodemap_tldevice)

        # Deinitialize camera
        cam.DeInit()

    except PySpin.SpinnakerException as ex:
        print('Error: %s' % ex)
        result = False

    return result


def main():
    """
    Example entry point; notice the volume of data that the logging event handler
    prints out on debug despite the fact that very little really happens in this
    example. Because of this, it may be better to have the logger set to lower
    level in order to provide a more concise, focused log.

    :return: True if successful, False otherwise.
    :rtype: bool
    """
    result = True

    # Retrieve singleton reference to system object
    system = PySpin.System.GetInstance()

    # Get current library version
    version = system.GetLibraryVersion()
    print('Library version: %d.%d.%d.%d' % (version.major, version.minor, version.type, version.build))

    # Retrieve list of cameras from the system
    cam_list = system.GetCameras()

    num_cameras = cam_list.GetSize()

    print('Number of cameras detected: %d' % num_cameras)

    # Finish if there are no cameras
    if num_cameras == 0:

        # Clear camera list before releasing system
        cam_list.Clear()

        # Release system instance
        system.ReleaseInstance()

        print('Not enough cameras!')
        input('Done! Press Enter to exit...')
        return False

    # Run example on each camera
    for i, cam in enumerate(cam_list):

        print('Running example for camera %d...' % i)

        result &= run_single_camera(cam)
        print('Camera %d example complete... \n' % i)

    # Release reference to camera
    # NOTE: Unlike the C++ examples, we cannot rely on pointer objects being automatically
    # cleaned up when going out of scope.
    # The usage of del is preferred to assigning the variable to None.
    del cam

    # Clear camera list before releasing system
    cam_list.Clear()

    # Release system instance
    system.ReleaseInstance()

    input('Done! Press Enter to exit...')
    return result


if __name__ == '__main__':
    if main():
        sys.exit(0)
    else:
        sys.exit(1)
