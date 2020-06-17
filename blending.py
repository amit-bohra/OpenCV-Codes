import cv2
import numpy as np


def ep(one):
    pass

img1=cv2.imread('mandril_color.tif')
img2=cv2.imread('lena_color_512.tif')
img1=cv2.bitwise_not(img1)
window='Transition'
cv2.namedWindow(window)
cv2.createTrackbar('apha',window,0,100,ep)
i=0
flag=0
while(True):
    alpha=cv2.getTrackbarPos('apha',window)/100
    beta=1-alpha
    output=cv2.addWeighted(img1,alpha,img2,beta,0)
    cv2.imshow(window,output)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
