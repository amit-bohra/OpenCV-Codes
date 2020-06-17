import cv2
import numpy as np
import time


img=cv2.imread('lena_color_512.png',1)
imggray=cv2.imread('lena_gray_512.tif',1)

i=0
while True:
    imgc=cv2.applyColorMap(img,i)
    imggrayc=cv2.applyColorMap(imggray,i)
    imgc=np.hstack((imgc,imggrayc))
    print(i)
    time.sleep(1)
    i+=1
    if i==20:
        i=0
    cv2.imshow('img_colormap',imgc)
    cv2.imshow('img_colorandgraymaps',img)
    if cv2.waitKey(5)==27:
        break
cv2.destroyAllWindows()
        
