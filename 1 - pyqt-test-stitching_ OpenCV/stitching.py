import PyCapture2
import cv2
import numpy as np
import threading


def print_format7_capabilities(fmt7_info):
    print('\n*** CAMERA FORMAT 7 CAPABILITIES ***\n')
    print('Mode: ({})'.format(fmt7_info.mode))
    print('Max image pixels: ({}, {})'.format(fmt7_info.maxWidth, fmt7_info.maxHeight))
    print('Image unit size: ({}, {})'.format(fmt7_info.imageHStepSize, fmt7_info.imageVStepSize))
    print('Offset unit size: ({}, {})'.format(fmt7_info.offsetHStepSize, fmt7_info.offsetVStepSize))
    print('Pixel format bitfield: 0x{}'.format(fmt7_info.pixelFormatBitField))
    print('Packet size: ({})'.format(fmt7_info.packetSize))
    print('Vendor pixel format bit field: ({})'.format(fmt7_info.vendorPixelFormatBitField))
    print('Min packet size: ({})'.format(fmt7_info.minPacketSize))
    print('Max packet size: ({})'.format(fmt7_info.maxPacketSize))
    print('Percentage: ({}%)'.format(fmt7_info.percentage))
    print()

def buildPano(cv_image):
    imgs_aux = []
    if len(imgs)<1:
         imgs.append(cv_image)
    else:
        imgs_aux.append(imgs[-1])
        imgs_aux.append(cv_image)
        # print(np.sum(np.square(imgs_aux[1]-imgs_aux[0])))
        # print(stitcher.estimateTransform(imgs_aux))
        # status, aux_pano = stitcher.stitch(imgs_aux)
        # if status == cv2.cv2.Stitcher_OK:
        #     imgs.append(cv_image)
    cv2.cv2.imshow('pano', cv_image)

def showImage(image):
    image_aux = image.convert(PyCapture2.PIXEL_FORMAT.BGR)
    cv_image = cv2.cv2.UMat(np.array(image_aux.getData(), 
               dtype="uint8").reshape(image_aux.getRows()
               ,image_aux.getCols(),3))
    cv2.cv2.imshow('video',cv_image)
    
    buildPano(cv_image)      
    
bus = PyCapture2.BusManager()
numCams = bus.getNumOfCameras()
camera = PyCapture2.Camera()
uid = bus.getCameraFromIndex(0)
camera.connect(uid)


fmt7_info,supported=camera.getFormat7Info(PyCapture2.MODE.MODE_4)
if supported: 
    print_format7_capabilities(fmt7_info)

# Configure camera format7 settings
fmt7_img_set = PyCapture2.Format7ImageSettings(fmt7_info.mode, 0, 0,
                           fmt7_info.maxWidth, fmt7_info.maxHeight,
                           PyCapture2.PIXEL_FORMAT.RGB8)

fmt7_pkt_inf, isValid = camera.validateFormat7Settings(fmt7_img_set)


camera.setFormat7ConfigurationPacket(fmt7_pkt_inf.recommendedBytesPerPacket, 
                                      fmt7_img_set)

cv2.cv2.namedWindow('video',cv2.cv2.WINDOW_NORMAL)
cv2.cv2.moveWindow('video',20,20)
cv2.cv2.namedWindow('pano',cv2.cv2.WINDOW_NORMAL)
cv2.cv2.moveWindow('pano',500,500)


imgs = []
pano = []
stitcher = cv2.cv2.Stitcher_create(cv2.cv2.Stitcher_SCANS)
stitcher.setWaveCorrection(False)
stitcher.setRegistrationResol(0.3)
stitcher.setSeamEstimationResol(0.1)
stitcher.setCompositingResol(0.6)
# stitcher.setPanoConfidenceThresh(1)
# stitcher.setSeamFinder(new detail::GraphCutSeamFinder(detail::GraphCutSeamFinderBase::COST_COLOR));
# stitcher.setBlender(detail::Blender::createDefault(detail::Blender::MULTI_BAND, false));
# stitcher.setExposureCompensator(detail::ExposureCompensator::createDefault(detail::ExposureCompensator::GAIN_BLOCKS) );
# stitcher.setWaveCorrection(true);
# stitcher.setWaveCorrectKind(detail::WAVE_CORRECT_HORIZ);
# stitcher.setFeaturesMatcher(
#         new detail::BestOf2NearestMatcher(false, 0.3, 6, 6));
# stitcher.setBundleAdjuster(new detail::BundleAdjusterRay());




print(stitcher.registrationResol())

camera.startCapture(showImage)
cv2.cv2.waitKey(0)

camera.stopCapture() 
camera.disconnect()  
cv2.cv2.destroyAllWindows()

# status,pano=stitcher.stitch(imgs)

# cv2.cv2.namedWindow('pano',cv2.cv2.WINDOW_NORMAL)
# cv2.cv2.moveWindow('pano',500,500)
# cv2.cv2.imshow('pano',pano)

# cv2.cv2.destroyAllWindows()
