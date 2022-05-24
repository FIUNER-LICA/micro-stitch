from cv2 import matchTemplate, minMaxLoc, TM_CCOEFF_NORMED

def MatchMask(img2,mask):
    res = matchTemplate(img2, mask, TM_CCOEFF_NORMED)
    #Coordenadas
    min_val, max_val, min_loc, max_loc = minMaxLoc(res)
    # print (max_val)
    y = max_loc[0]
    x = max_loc[1]
    return x,y,max_val