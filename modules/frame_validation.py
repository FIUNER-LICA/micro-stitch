""" _Previous analysis of the frame to form the panoramic image_
"""

def image_quality(image_1, image_2, window, K, L):
    """_ssim:
        This function compute de structural similarity index of the images
        X and Y and its components: Luminance, contrast and correlation
        usage 1 : ssim (X,Y)
        usage 2 : ssim (X,Y,window)
        usage 3 : ssim (X,Y,window,K)
        usage 4 : ssim (X,Y,window,K,L)_

    Args:
        image_1 (_type_): _one of the images for comparing_
        image_2 (_type_): _one of the images for comparing_
        window (_type_): _is the window of analysis_
        K (_type_): _is vector of two small constants that are
                        passed to assure numerical stability 
                        when denominators are close to zero_
        L (_type_): _is the maximum value of the dynamic 
                        range of the images_
    """
    pass

def focus_validation(image):
    pass
