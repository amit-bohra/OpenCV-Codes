import cv2
import numpy as np


def func(x):
    pass
a=0
a=int(input('Enter 1 for VideoCam else 0 '))
if a==1:
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,img=cap.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        ret=False
else:
    img=cv2.imread('a.jpg',0)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('name1','image',5,10,func)

x=5
temp=5
val=5
if a==1:
    ret,img1=cap.read()
else:
    img1=cv2.imread('a.jpg',0)
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('a.jpg',0)
    x=cv2.getTrackbarPos('name1','image')
    val=x
    tmg=cv2.pyrDown(img1)
    tmg1=cv2.pyrUp(tmg)
    laplacian=cv2.subtract(img1,tmg1)
    if temp<val:
        img1=cv2.pyrUp(img1)
        temp=val
    if temp>val:
        img1=cv2.pyrDown(img1)
        
        temp=val
    cv2.imshow('image',img)
    cv2.imshow('gaussian',img1)
    cv2.imshow('laplacian',laplacian)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
