from cv2 import cv2
def MatchMask(img2,mask):
    res = cv2.matchTemplate(img2, mask, cv2.TM_CCOEFF_NORMED)
    #Coordenadas
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print (max_val)
    y = max_loc[0]
    x = max_loc[1]
    return x,y,max_val