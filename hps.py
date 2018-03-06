import numpy as np
import cv2 as cv
img_rgb = cv.imread('ori.png')
mask = np.zeros(img_rgb.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
h,w,c= img_rgb.shape
rect = (1, 1, w - 2, h - 2)
output = np.zeros(img_rgb.shape, np.uint8)  # output image to be shown
rect_or_mask = 0
while(1):

    cv.imshow('output',output)
    cv.imshow('input',img_rgb)
    k = cv.waitKey(1)
    # key bindings
    if k == 27:         # esc to exit
        break
    elif k == ord('n'):  # segment the image
        if (rect_or_mask == 0):         # grabcut with rect
            bgdmodel = np.zeros((1,65),np.float64)
            fgdmodel = np.zeros((1,65),np.float64)
            rect = (0, 0, w - 1, h - 1)
            cv.grabCut(img_rgb,mask,rect,bgdmodel,fgdmodel,1,cv.GC_INIT_WITH_RECT)
            rect_or_mask = 1
        elif rect_or_mask == 1:         # grabcut with mask
            bgdmodel = np.zeros((1,65),np.float64)
            fgdmodel = np.zeros((1,65),np.float64)
            cv.grabCut(img_rgb,mask,rect,bgdmodel,fgdmodel,1,cv.GC_INIT_WITH_MASK)

    mask2 = np.where((mask==1) + (mask==3),255,0).astype('uint8')
    output = cv.bitwise_and(img_rgb,img_rgb,mask=mask2)

'''cv.imshow('output',output)
cv.imshow('input',img_rgb)
cv.waitKey(0)'''