import numpy as np
import scipy as sp
def ssim(X,Y,*args):#(X,Y,window,K,L):
    Inf = 0

    nargin = len(args)+2
    if ((nargin < 2 | nargin > 5)|(np.size(X) != np.size(Y))):
        QI = -Inf
        CORR = -Inf
        LUM = -Inf
        CON = -Inf
        return 
    [M,N] = X.shape[:1]
    if (nargin == 2):
        if ((M < 11) | (N < 11)):
            QI = -Inf
            CORR = -Inf
            LUM = -Inf
            CON = -Inf
            return
        window= cv2.GaussianBlur() 	.GaussianBlur(	src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]	)
        # window = fspecial('gaussian', 11, 1.5);     
        K(1) = 0.01                        
        K(2) = 0.03                                       
        L = 255                               
  endif;

    return [QI,CORR,LUM,CON]





#Filtro gaussiano equivalente a la fun fspecial
def matlab_style_gauss2D(shape=(3,3),sigma=0.5):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h