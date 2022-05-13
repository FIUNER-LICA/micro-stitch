from Funciones import funPano, funMatch
from concurrent.futures import ThreadPoolExecutor

def panoCam(panoramica, last_frame, new_frame, X,Y,r, x1,y1):

    mask = last_frame[x1:x1+r,y1:y1+r,:]

    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     future1 = executor.submit(funMatch.MatchMask, new_frame, mask)
    #     x2,y2,max_val = future1.result()
    #     future2 = executor.submit(funMatch.MatchMask, new_frame, mask)
    #     x2,y2,max_val = future2.result()

    x2,y2,max_val = funMatch.MatchMask (new_frame,mask)
    # x2,y2,max_val = funMatch.MatchMask (new_frame,mask)
    # x2,y2,max_val = funMatch.MatchMask (new_frame,mask)
    # x2,y2,max_val = funMatch.MatchMask (new_frame,mask)

    if  max_val<0.8:
        return panoramica,X,Y
        
    tras_y=y1-y2
    tras_x = x1-x2
    if (tras_y==0 and tras_x==0):
        return panoramica, X,Y
    
    panoramica = funPano.pano(panoramica, new_frame, tras_x, tras_y, X, Y)

    if (X+tras_x)>=0:
        X=X+tras_x
    else: X=0
    if (Y+tras_y)>=0:
        Y=Y+tras_y
    else: Y=0

    print (tras_x,tras_y)
    return panoramica,X,Y