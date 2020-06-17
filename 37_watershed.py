import cv2
import numpy as np
from copy import deepcopy as dp
import matplotlib.pyplot as plt

def func(x):
    pass
a=0
a=int(input('Enter 1 for VideoCam else 0 '))
if a==1:
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,img=cap.read()
    else:
        ret=False
else:
    img=cv2.imread('coins.jpg')
cv2.namedWindow('timage',cv2.WINDOW_NORMAL)
cv2.createTrackbar('blur','timage',1,255,func)
cv2.createTrackbar('noise_open','timage',1,255,func)
cv2.createTrackbar('noise_iter','timage',1,255,func)
cv2.createTrackbar('erode','timage',20,255,func)
cv2.createTrackbar('eiter','timage',1,255,func)
cv2.createTrackbar('dilate','timage',6,255,func)
cv2.createTrackbar('diter','timage',1,255,func)
cv2.createTrackbar('a','timage',0,2,func)
cv2.createTrackbar('b','timage',70,100,func)
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('coins.jpg')
    blur=cv2.getTrackbarPos('blur','timage')
    ek=cv2.getTrackbarPos('erode','timage')
    ei=cv2.getTrackbarPos('eiter','timage')
    dk=cv2.getTrackbarPos('dilate','timage')
    di=cv2.getTrackbarPos('diter','timage')
    a1=cv2.getTrackbarPos('a','timage')
    b1=cv2.getTrackbarPos('b','timage')
    k=cv2.getTrackbarPos('noise_open','timage')
    oi=cv2.getTrackbarPos('noise_iter','timage')
    if ek%2==0:
        ek+=1
    if dk%2==0:
        dk+=1
    if blur<1:
        blur=1
    if blur%2==0:
        blur+=1
    if a1==1:
        a1=3
    if a1==2:
        a1=5
    if k<1:
        k=1
    if k%2==0:
        k+=1
    b1=b1/100
    okern=cv2.getStructuringElement(cv2.MORPH_RECT,(k,k))
    ekern=cv2.getStructuringElement(cv2.MORPH_RECT,(ek,ek))
    dkern=cv2.getStructuringElement(cv2.MORPH_RECT,(dk,dk))
    blurimg=cv2.GaussianBlur(img,(blur,blur),0)
    noise=cv2.morphologyEx(blurimg,cv2.MORPH_OPEN,okern,iterations=oi)
    imggray=cv2.cvtColor(noise,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(imggray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    back=cv2.dilate(thresh,dkern,iterations=di)
    #fore=cv2.erode(thresh,ekern,iterations=ei)
    dist_transform=cv2.distanceTransform(thresh,cv2.DIST_L2,a1)
    ret,fore=cv2.threshold(dist_transform,b1*dist_transform.max(),255,0)
    dist_transform=cv2.normalize(dist_transform,dist_transform,0,255,cv2.NORM_MINMAX)
    dist_transform=np.uint8(dist_transform)
    cv2.imshow('dist_transform',dist_transform)
    fore=np.uint8(fore)
    unknown=cv2.subtract(back,fore)
    ret,markers=cv2.connectedComponents(fore)
    markers+=1
    markers[unknown==255]=0
    markers=cv2.watershed(img,markers)
    img[markers==-1]=[255,0,0]
    cv2.imshow('fore',fore)
    cv2.imshow('image',img)
    cv2.imshow('back',back)
    cv2.imshow('unknown',unknown)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
