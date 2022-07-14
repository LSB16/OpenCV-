import numpy as np
import cv2

src = cv2.imread('./source/son.jpg')

if src is None: raise Exception('image load failed')

mask = np.zeros(src.shape[:2], np.uint8)
bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rc = cv2.selectROI(src)

cv2.grabCut(src, mask, rc, None, None, 1, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype(np.uint8)
dst = src * mask2[:,:, np.newaxis]
 
cv2.imshow('dst',dst)

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(dst, (x,y), 3, (255,0,0), cv2.FILLED)
        cv2.circle(mask, (x,y), 3, cv2.GC_FGD, cv2.FILLED)
        cv2.imshow('dst',dst)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(dst, (x,y), 3, (0,0,255),cv2.FILLED)
        cv2.circle(mask, (x,y), 3, cv2.GC_BGD, cv2.FILLED)
        cv2.imshow('dst',dst)

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(dst, (x,y), 3, (255,0,0), cv2.FILLED)
            cv2.circle(mask, (x,y), 3, cv2.GC_FGD, cv2.FILLED)
            cv2.imshow('dst',dst)

        if flags & cv2.EVENT_FLAG_RBUTTON:
            cv2.circle(dst, (x,y), 3, (0,0,255), cv2.FILLED)
            cv2.circle(mask, (x,y), 3, cv2.GC_BGD, cv2.FILLED)
            cv2.imshow('dst',dst)    

cv2.setMouseCallback('dst', onMouse)

while True:
    key = cv2.waitKey()
    if key == 13:
        cv2.grabCut(src, mask, rc, None, None, 1, cv2.GC_INIT_WITH_MASK)
        mask2 = np.where((mask== 0) | (mask == 2) , 0, 1).astype(np.uint8)
        dst = src * mask2[:,:, np.newaxis]
        cv2.imshow('dst',dst)

    elif key == 27: break

cv2.destroyAllWindows()