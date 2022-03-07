function PSNR = psnr(OR_IMAGE,MOD_IMAGE,MAX_INTENSITY)
% usage: psnr(OR_IMAGE,MOD_IMAGE,MAX_INTENSITY)
         MSE=mean(((OR_IMAGE(:)-MOD_IMAGE(:)).^2));
         PSNR=20*log10(MAX_INTENSITY/sqrt(MSE));
end
