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
cv2.createTrackbar('corner','image',70,1000,func)
cv2.createTrackbar('quality','image',5,999,func)
cv2.createTrackbar('dist','image',10,300,func)
cv2.createTrackbar('rad','image',5,150,func)

while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('a.jpg')
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    c=cv2.getTrackbarPos('corner','image')
    q=cv2.getTrackbarPos('quality','image')
    d=cv2.getTrackbarPos('dist','image')
    r=cv2.getTrackbarPos('rad','image')
    q=q/1000
    if d<1:
        d=10
    if q==0:
        q+=0.001
    corners=cv2.goodFeaturesToTrack(imggray,c,q,d)
    corners=np.int0(corners)
    for i in corners:
        x,y=i.ravel()
        cv2.circle(img,(x,y),r,255,-1)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
