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
cv2.createTrackbar('features','image',500,5000,func)
cv2.createTrackbar('flag','image',4 ,4,func)
while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('a.jpg')
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    x=cv2.getTrackbarPos('features','image')
    y=cv2.getTrackbarPos('flag','image')
    orb=cv2.ORB_create(nfeatures=x)
    kp,des=orb.detectAndCompute(imggray,None)
    img=cv2.drawKeypoints(img,kp,None,color=(255,0,0),flags=4)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
