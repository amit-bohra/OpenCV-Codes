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
    else:
        ret=False
else:
    img=cv2.imread('a.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('thresh','image',4,150,func)
cv2.createTrackbar('supp','image',1,1,func)
cv2.createTrackbar('neigh','image',0,2,func)
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('a.jpg')
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    x=cv2.getTrackbarPos('thresh','image')
    y=cv2.getTrackbarPos('supp','image')
    z=cv2.getTrackbarPos('neigh','image')
    fast=cv2.FastFeatureDetector_create(threshold=x)
    if y==0:
        fast.setNonmaxSuppression(0)
    else:
        fast.setNonmaxSuppression(1)
    fast.setType(z)
    kp=fast.detect(imggray,None)
    img2=cv2.drawKeypoints(img,kp,None,color=(255,0,0))
    cv2.imshow('image',img2)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print(fast.getType())
cv2.destroyAllWindows()
if a==1:
    cap.release()
