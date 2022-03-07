from cv2 import cv2
import matplotlib.pyplot as plt
def MatchMask(img2,mask):
    res = cv2.matchTemplate(img2, mask, cv2.TM_CCOEFF_NORMED)
    #Coordenadas
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print (max_val)
    y = max_loc[0]
    x = max_loc[1]
    return x,y,max_val

def carga_img():
    # img_1 = cv2.imread("./images/img_1.jpg", cv2.IMREAD_ANYCOLOR)
    # img_2 = cv2.imread("./images/img_2.jpg", cv2.IMREAD_ANYCOLOR)
    # img_3 = cv2.imread("./images/img_3.jpg", cv2.IMREAD_ANYCOLOR)
    # img_4 = cv2.imread("./images/img_4.jpg", cv2.IMREAD_ANYCOLOR)
    # img_5 = cv2.imread("./images/img_5.jpg", cv2.IMREAD_ANYCOLOR)
    # img_in =[img_1.copy(),img_2.copy(),img_3.copy(),img_4.copy(),img_5.copy()]

    # #   Pano de tigre con frames de 700x500
    # img_1 = cv2.imread("./images/img1.jpg", cv2.IMREAD_ANYCOLOR)
    # img_2 = cv2.imread("./images/img2.jpg", cv2.IMREAD_ANYCOLOR)
    # img_3 = cv2.imread("./images/img3.jpg", cv2.IMREAD_ANYCOLOR)
    # img_4 = cv2.imread("./images/img4.jpg", cv2.IMREAD_ANYCOLOR)
    # img_5 = cv2.imread("./images/img5.jpg", cv2.IMREAD_ANYCOLOR)
    # img_6 = cv2.imread("./images/img6.jpg", cv2.IMREAD_ANYCOLOR)
    # img_7 = cv2.imread("./images/img7.jpg", cv2.IMREAD_ANYCOLOR)
    # img_in =[img_7.copy()]
    # img_in =[img_1.copy(),img_2.copy(),img_3.copy(),img_4.copy(),img_5.copy(),img_6.copy(),img_7.copy()]

    # HEMATOXILINA EOSINA
    # # #   Pano a partir de 11 imágenes de 350x350
    # img_1 = cv2.imread("./images/HE1.jpg", cv2.IMREAD_ANYCOLOR)
    # img_2 = cv2.imread("./images/HE2.jpg", cv2.IMREAD_ANYCOLOR)
    # img_3 = cv2.imread("./images/HE3.jpg", cv2.IMREAD_ANYCOLOR)
    # img_4 = cv2.imread("./images/HE4.jpg", cv2.IMREAD_ANYCOLOR)
    # img_5 = cv2.imread("./images/HE5.jpg", cv2.IMREAD_ANYCOLOR)
    # img_6 = cv2.imread("./images/HE6.jpg", cv2.IMREAD_ANYCOLOR)
    # img_7 = cv2.imread("./images/HE7.jpg", cv2.IMREAD_ANYCOLOR)
    # img_8 = cv2.imread("./images/HE8.jpg", cv2.IMREAD_ANYCOLOR)
    # img_9 = cv2.imread("./images/HE9.jpg", cv2.IMREAD_ANYCOLOR)
    # img_10 = cv2.imread("./images/HE10.jpg", cv2.IMREAD_ANYCOLOR)
    # img_11 = cv2.imread("./images/HE11.jpg", cv2.IMREAD_ANYCOLOR)


    # img_in =[img_1.copy(),img_2.copy(),img_3.copy(),img_4.copy(),img_5.copy(),img_6.copy(),img_7.copy(),img_8.copy(),img_9.copy(),img_10.copy(),img_11.copy()]

    #   Pano a partir de 8 frames de 450x450
    # img_1 = cv2.imread("./images/1.jpg", cv2.IMREAD_ANYCOLOR)
    # img_2 = cv2.imread("./images/2.jpg", cv2.IMREAD_ANYCOLOR)
    # img_3 = cv2.imread("./images/3.jpg", cv2.IMREAD_ANYCOLOR)
    # img_4 = cv2.imread("./images/4.jpg", cv2.IMREAD_ANYCOLOR)
    # img_5 = cv2.imread("./images/5.jpg", cv2.IMREAD_ANYCOLOR)
    # img_6 = cv2.imread("./images/6.jpg", cv2.IMREAD_ANYCOLOR)
    # img_7 = cv2.imread("./images/7.jpg", cv2.IMREAD_ANYCOLOR)
    # img_8 = cv2.imread("./images/8.jpg", cv2.IMREAD_ANYCOLOR)
    
    # img_in =[img_1.copy(),img_2.copy(),img_3.copy(),img_4.copy(),img_5.copy(),img_6.copy(),img_7.copy(),img_8.copy()]
    
    # #   Prueba para corregir código con diferentes direcciones de interés de 300x300
    # img_1 = cv2.imread("./images2/1.jpg", cv2.IMREAD_ANYCOLOR)
    # img_2 = cv2.imread("./images2/2.jpg", cv2.IMREAD_ANYCOLOR)
    # img_3 = cv2.imread("./images2/3.jpg", cv2.IMREAD_ANYCOLOR)
    # img_4 = cv2.imread("./images2/4.jpg", cv2.IMREAD_ANYCOLOR)
    # img_5 = cv2.imread("./images2/5.jpg", cv2.IMREAD_ANYCOLOR)
    # img_6 = cv2.imread("./images2/6.jpg", cv2.IMREAD_ANYCOLOR)
    
    # img_in =[img_1.copy(),img_2.copy(),img_5.copy(),img_3.copy(),img_6.copy(),img_4.copy()]
        
    # ...#   mostrar_desplazamientos// "captura frame a frame"
    #  4 frames de 1024x1024 /

    img_1 = cv2.imread("./Captura stitching faf/1.jpg", cv2.IMREAD_ANYCOLOR)
    img_2 = cv2.imread("./Captura stitching faf/2.jpg", cv2.IMREAD_ANYCOLOR)
    img_3 = cv2.imread("./Captura stitching faf/3.jpg", cv2.IMREAD_ANYCOLOR)
    img_4 = cv2.imread("./Captura stitching faf/4.jpg", cv2.IMREAD_ANYCOLOR)
    img_in =[img_1.copy(),img_2.copy(),img_3.copy(),img_4.copy()]
    
    #   4 frames de 300x300

    # img_1 = cv2.imread("./Captura stitching faf/mostrar_desplazamientos/11.jpg", cv2.IMREAD_ANYCOLOR)
    # img_2 = cv2.imread("./Captura stitching faf/mostrar_desplazamientos/22.jpg", cv2.IMREAD_ANYCOLOR)
    # img_3 = cv2.imread("./Captura stitching faf/mostrar_desplazamientos/33.jpg", cv2.IMREAD_ANYCOLOR)
    # img_4 = cv2.imread("./Captura stitching faf/mostrar_desplazamientos/44.jpg", cv2.IMREAD_ANYCOLOR)
    # img_in =[img_1.copy(),img_2.copy(),img_3.copy(),img_4.copy()]

    #   4 frames de 1000x1000

    # img_1 = cv2.imread("./Captura stitching faf/mostrar_desplazamientos/1.jpg", cv2.IMREAD_ANYCOLOR)
    # img_2 = cv2.imread("./Captura stitching faf/mostrar_desplazamientos/2.jpg", cv2.IMREAD_ANYCOLOR)
    # # fig 3 en posicion 2000 - 1000
    # img_3 = cv2.imread("./Captura stitching faf/mostrar_desplazamientos/3.jpg", cv2.IMREAD_ANYCOLOR)
    # img_4 = cv2.imread("./Captura stitching faf/mostrar_desplazamientos/4.jpg", cv2.IMREAD_ANYCOLOR)
    # img_in =[img_1.copy(),img_2.copy(),img_3.copy(),img_4.copy()]

    #...#   Testeo tiempo mascaras 
    
    # # 2 frames de 1024x1024

    # img_1 = cv2.imread("./Testeo de tiempo de template/img/1.jpg", cv2.IMREAD_ANYCOLOR)
    # img_2 = cv2.imread("./Testeo de tiempo de template/img/2.jpg", cv2.IMREAD_ANYCOLOR)
    # img_in =[img_1.copy(),img_2.copy()]
    
    # 2 imágenes de 480x480 (pano completa de 640x480)

    # img_1 = cv2.imread("./Testeo de tiempo de template/img1/111.jpg", cv2.IMREAD_ANYCOLOR)
    # img_2 = cv2.imread("./Testeo de tiempo de template/img1/222.jpg", cv2.IMREAD_ANYCOLOR)
    # img_in =[img_1.copy(),img_2.copy()] 
    
    #...#   Formar pano 


    # 64 frames, de imagen generada

    # img_in = []
    # for r in range(64):
    #     img_1 = cv2.imread("./imagenes generadas/PANORAMICA_{}.jpg".format(r), cv2.IMREAD_ANYCOLOR)

    #     a= img_1.copy()
    #     img_in.append(a)



    return img_in

