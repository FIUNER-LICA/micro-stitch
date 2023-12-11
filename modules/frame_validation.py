""" Previous analysis of the frame to form the panoramic image
"""
# from typing import Tuple
from skimage.metrics import structural_similarity as ssim
import cv2

def image_quality(image_1, image_2, channel_axis=2, multichannel=True):
    """_ssim:
        This function compute de structural similarity index of the images
        X and Y and its components: Luminance, contrast and correlation
        usage 1 : ssim (X,Y)
        usage 2 : ssim (X,Y,window)
        usage 3 : ssim (X,Y,window,K)
        usage 4 : ssim (X,Y,window,K,L)_
    """
    ssim_data = ssim(image_1, image_2, channel_axis, multichannel)
    return ssim_data

def focus_validation(image, *args):
    
    focus_data = ['None focuse data']
    for arg in args:
        if arg==0:
            lap_var = cv2.Laplacian(image,cv2.CV_64F,0).var()
            focus_data.append(lap_var)
            # focus_data = [lap_var]
        if arg ==1:
            lap_sob = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5).var()
            focus_data.append(lap_sob)
    return focus_data

# def image_quality(image_1, image_2, window, K, L):
#     """_ssim:
#         This function compute de structural similarity index of the images
#         X and Y and its components: Luminance, contrast and correlation
#         usage 1 : ssim (X,Y)
#         usage 2 : ssim (X,Y,window)
#         usage 3 : ssim (X,Y,window,K)
#         usage 4 : ssim (X,Y,window,K,L)_

#     Args:
#         image_1 (_type_): _one of the images for comparing_
#         image_2 (_type_): _one of the images for comparing_
#         window (_type_): _is the window of analysis_
#         K (_type_): _is vector of two small constants that are
#                         passed to assure numerical stability 
#                         when denominators are close to zero_
#         L (_type_): _is the maximum value of the dynamic 
#                         range of the images_
#     """
#     pass
