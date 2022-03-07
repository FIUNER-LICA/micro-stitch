function PSNR = psnr(OR_IMAGE,MOD_IMAGE,MAX_INTENSITY)
# usage: psnr(OR_IMAGE,MOD_IMAGE,MAX_INTENSITY)
         MSE=meansq((OR_IMAGE-MOD_IMAGE)(:));
         PSNR=20*log10(MAX_INTENSITY/sqrt(MSE));
endfunction
