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
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('h','image',10,255,func)
cv2.createTrackbar('h1','image',10,255,func)
cv2.createTrackbar('t','image',7,255,func)
cv2.createTrackbar('s','image',3,255,func)
while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('a.jpg')
    h=cv2.getTrackbarPos('h','image')
    h1=cv2.getTrackbarPos('h1','image')
    t=cv2.getTrackbarPos('t','image')
    s=cv2.getTrackbarPos('s','image')
    if t<1:
        t=1
    if s<1:
        s=1
    if t%2==0:
        t+=1
    if s%2==0:
        s+=1
    dst=cv2.fastNlMeansDenoisingColored(img,None,h,h1,t,s)
    img3=np.hstack((img,dst))
    cv2.imshow('image',img3)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
