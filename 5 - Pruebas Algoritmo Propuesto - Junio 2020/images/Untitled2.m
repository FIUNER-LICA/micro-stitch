clear all;  % Borra las variables del espacio de trabajo.
close all;  % Cierra las ventanas de graficaci?n.
clc;        % Borra la ventana de comandos.

% img2 = imread('PANORAMICA_HE2.jpg');
% img = imread('Hematoxilina eosina-Paravani Enrique.jpeg');
img2 = imread('PANORAMICA_4000x3000.jpg');
img = imread('1copia.jpg');
[QI,CORR,LUM,CON] = ssim2(mean(img,3),mean(img2,3));

x1= mean (QI(:));
x2= mean (CORR(:));
x3= mean (LUM(:));
x4= mean (CON(:));

PSNR = psnr(mean(img,3),mean(img2,3),255);

figure(1)

subplot(1,2,1)
imshow (img);

subplot (1,2,2)
imshow (img2);

figure(2)
subplot (2,2,1)
imshow (LUM,[]);
title('LUM')
subplot (2,2,2)
imshow (CON,[]);
title('CON')
subplot (2,2,3)
imshow (CORR,[]);
title('CORR')
subplot (2,2,4)
imshow (QI,[]);
title('Índice de calidad')