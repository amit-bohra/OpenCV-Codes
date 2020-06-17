import cv2
import numpy as np
import time

img1=cv2.imread('mandril_color.tif')
img2=cv2.imread('lena_color_512.tif')
img=cv2.bitwise_not(cv2.bitwise_xor(img1,img2))
img=cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)
rows,column,layer=img.shape
while True:
    r=cv2.getRotationMatrix2D((column/2,rows/2),5,1)
    img=cv2.warpAffine(img,r,(column,rows))
    cv2.imshow('window',img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
