from itertools import count
from tracemalloc import start
import cv2
import datetime
filename = 'C:/Users/sandr/Downloads/video_flir_12_12_19_8_2022.tiff'

retval, imgs = cv2.imreadmulti(filename)#, start = 1, count = 50)
# imgs = []
pano = []
stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
stitcher.setWaveCorrection(False)
stitcher.setRegistrationResol(0.3)
stitcher.setSeamEstimationResol(0.1)
stitcher.setCompositingResol(1.0)
# stitcher.setPanoConfidenceThresh(1)
# stitcher.setSeamFinder(new detail::GraphCutSeamFinder(detail::GraphCutSeamFinderBase::COST_COLOR));
# stitcher.setBlender(detail::Blender::createDefault(detail::Blender::MULTI_BAND, false));
# stitcher.setExposureCompensator(detail::ExposureCompensator::createDefault(detail::ExposureCompensator::GAIN_BLOCKS) );
# stitcher.setWaveCorrectKind(detail::WAVE_CORRECT_HORIZ);
# stitcher.setFeaturesMatcher(
#         new detail::BestOf2NearestMatcher(false, 0.3, 6, 6));
# stitcher.setBundleAdjuster(new detail::BundleAdjusterRay());
print (type(imgs))
print (len(imgs))

panoramic = []
try:
    status, panoramic =stitcher.stitch(imgs[:-1:5])
    
except:
    print ("Error en la generación de panorámica")
    pass

x = datetime.datetime.now()
cv2.imwrite('./panoramic_{}_{}_{}_{}_{}.tiff'.format(x.hour,
            x.minute,x.day,x.month, x.year), panoramic[:,:,:])
