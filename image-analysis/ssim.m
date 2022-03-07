function [QI,CORR,LUM,CON] = ssim(X,Y,window,K,L);
  %% ----------------------------------------------------------------
  %% Code modified from:
  %% https://ece.uwaterloo.ca/~z70wang/research/ssim/ssim_index.m
  %% Reference paper:
  %% Z. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli, "Image
  %% quality assessment: From error measurement to structural similarity"
  %% IEEE Transactios on Image Processing, vol. 13, no. 1, Jan. 2004.
  %% ------------------------------------------------------------------
  %% This function compute de structural similarity index of the images
  %% X and Y and its components: Luminance, contrast and correlation
  %% usage 1 : ssim (X,Y)
  %% usage 2 : ssim (X,Y,window)
  %% usage 3 : ssim (X,Y,window,K)
  %% usage 4 : ssim (X,Y,window,K,L)
  %% X and Y are the images for comparing, "window" is the window of
  %% analysis, K is vector of two small constants that are
  %% passed to assure numerical stability when denominators are
  %% close to zero and L is the maximum value of the dynamic range of
  %% the images.
  %% ------------------------------------------------------------------
  %% Version 1.0
  %% Year 2012
  %% Author: Javier E. Diaz Zamboni. Facultad de Ingeniería, Universidad
  %% Nacional de Entre Ríos, Argentina.
  %% contact: javierdiaz(at)bioingenieria(dot)edu(dot)ar
  %% ------------------------------------------------------------------
  
  if ((nargin < 2 || nargin > 5)||(size(X) ~= size(Y)))
    QI = -Inf;
    CORR = -Inf;
    LUM = -Inf;
    CON = -Inf;
    return;
  endif;
  [M N] = size(X);
  if (nargin == 2)
    if ((M < 11) || (N < 11))
      QI = -Inf;
      CORR = -Inf;
      LUM = -Inf;
      CON = -Inf;
      return;     
    endif;
    window = fspecial('gaussian', 11, 1.5);     
    K(1) = 0.01;                        
    K(2) = 0.03;                                        
    L = 255;                                  
  endif;
  if (nargin == 3)
    if ((M < 11) || (N < 11))
      QI = -Inf;
      CORR = -Inf;
      LUM = -Inf;
      CON = -Inf;
      return;
    endif;
    window = fspecial('gaussian', 11, 1.5);
    L = 255;
    if (length(K) == 2)
      if (K(1) < 0 || K(2) < 0)
        QI = -Inf;
        CORR = -Inf;
        LUM = -Inf;
        CON = -Inf;
        return;
      endif;
    else
      QI = -Inf;
      CORR = -Inf;
      LUM = -Inf;
      CON = -Inf;
      return;      
    endif;
  endif;
  if (nargin == 4)
    [H W] = size(window);
    if ((H*W) < 4 || (H > M) || (W > N))
      QI = -Inf;
      CORR = -Inf;
      LUM = -Inf;
      CON = -Inf;
      return;      
    endif;
    L = 255;
    if (length(K) == 2)
      if (K(1) < 0 || K(2) < 0)
        QI = -Inf;
        CORR = -Inf;
        LUM = -Inf;
        CON = -Inf;
        return;    
      endif;
    else
      QI = -Inf;
      CORR = -Inf;
      LUM = -Inf;
      CON = -Inf;
      return;      
    endif;
  endif;
  if (nargin == 5)
    [H W] = size(window);
    if ((H*W) < 4 || (H > M) || (W > N))
      QI = -Inf;
      CORR = -Inf;
      LUM = -Inf;
      CON = -Inf;
      return;      
    endif;
    if (length(K) == 2)
      if (K(1) < 0 || K(2) < 0)
        QI = -Inf;
        CORR = -Inf;
        LUM = -Inf;
        CON = -Inf;
        return;    
      endif;
    else
      QI = -Inf;
      CORR = -Inf;
      LUM = -Inf;
      CON = -Inf;
      return;      
    endif;
  endif;

  C1 = (K(1)*L)^2;
  C2 = (K(2)*L)^2;
  window = window/sum(window(:));
  X = double(X);
  Y = double(Y);
  mu1 = filter2(window, X, 'valid');
  mu2 = filter2(window, Y, 'valid');
  mu1_sq = mu1.*mu1;
  mu2_sq = mu2.*mu2;
  mu1_mu2 = mu1.*mu2;
  sigma1_sq = filter2(window, X.*X, 'valid') - mu1_sq;
  sigma2_sq = filter2(window, Y.*Y, 'valid') - mu2_sq;
  index=sigma1_sq<0;
  sigma1_sq(index)=0;
  index=sigma2_sq<0;
  sigma2_sq(index)=0;

  sigma12 = filter2(window, X.*Y , 'valid') - mu1_mu2;
  LUM=(2*mu1.*mu2+C1)./(mu1_sq+mu2_sq+C1);
  
  CON=(2*sqrt(sigma1_sq).*sqrt(sigma2_sq)+C2)./(sigma1_sq+sigma2_sq+C2);
  
  CORR=(sigma12+C2/2)./(sqrt(sigma1_sq).*sqrt(sigma2_sq)+C2/2);
  
  QI=CORR.*LUM.*CON;
  
endfunction
