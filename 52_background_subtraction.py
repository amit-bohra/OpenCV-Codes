import cv2
import numpy as np
from copy import deepcopy as dp

def func(x):
    pass

cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,img=cap.read()
else:
    ret=False

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('k','image',0,255,func)
cv2.createTrackbar('val','image',0,2,func)
mog=cv2.bgsegm.createBackgroundSubtractorMOG()
gmg=cv2.bgsegm.createBackgroundSubtractorGMG()
cnt=cv2.bgsegm.createBackgroundSubtractorCNT()
gsoc=cv2.bgsegm.createBackgroundSubtractorGSOC()
lsbp=cv2.bgsegm.createBackgroundSubtractorLSBP()
mog2=cv2.createBackgroundSubtractorMOG2()
knn=cv2.createBackgroundSubtractorKNN()
while True:
    ret,img=cap.read()
    img=cv2.flip(img,1)
    mogmask=mog.apply(img)
    gmgmask=gmg.apply(img)
    cntmask=cnt.apply(img)
    gsocmask=gsoc.apply(img)
    lsbpmask=lsbp.apply(img)
    mog2mask=mog2.apply(img)
    knnmask=knn.apply(img)
    mogmask=cv2.resize(mogmask,(300,300))
    gmgmask=cv2.resize(gmgmask,(300,300))
    cntmask=cv2.resize(cntmask,(300,300))
    gsocmask=cv2.resize(gsocmask,(300,300))
    lsbpmask=cv2.resize(lsbpmask,(300,300))
    mog2mask=cv2.resize(mog2mask,(300,300))
    knnmask=cv2.resize(knnmask,(300,300))
    x=cv2.getTrackbarPos('k','image')
    y=cv2.getTrackbarPos('val','image')
    if x<1:
        x=1
    if x%2==0:
        x+=1
    kernel=cv2.getStructuringElement(y,(x,x))
    mogmask=cv2.morphologyEx(mogmask,cv2.MORPH_OPEN,kernel)
    mog2mask=cv2.morphologyEx(mog2mask,cv2.MORPH_OPEN,kernel)
    gmgmask=cv2.morphologyEx(gmgmask,cv2.MORPH_OPEN,kernel)
    cntmask=cv2.morphologyEx(cntmask,cv2.MORPH_OPEN,kernel)
    gsocmask=cv2.morphologyEx(gsocmask,cv2.MORPH_OPEN,kernel)
    lsbpmask=cv2.morphologyEx(lsbpmask,cv2.MORPH_OPEN,kernel)
    knnmask=cv2.morphologyEx(knnmask,cv2.MORPH_OPEN,kernel)
    cv2.imshow('mog',mogmask)
    cv2.imshow('mog2',mog2mask)
    cv2.imshow('gmg',gmgmask)
    cv2.imshow('cnt',cntmask)
    cv2.imshow('gsoc',gsocmask)
    cv2.imshow('lsbp',lsbpmask)
    cv2.imshow('knn',knnmask)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
cap.release()
