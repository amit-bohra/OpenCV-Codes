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
cv2.createTrackbar('name1','image',45,90,func)
cv2.createTrackbar('name2','image',45,90,func)
x=0
y=0
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('a.jpg',0)
    tx=cv2.getTrackbarPos('name1','image')
    ty=cv2.getTrackbarPos('name2','image')
    pts1=np.float32([[110,110],[210,110],[110,210],[210,210]])
    pts2=np.float32([[110,110],[210,110],[110,210],[210,210]])
    x=tx-45
    y=ty-45
    pts2=np.float32([[110+x,110+y],[210-x,110+y],[110+x,210-y],[210-x,210-y]])
    M=cv2.getPerspectiveTransform(pts1,pts2)
    img=cv2.warpPerspective(img,M,(img.shape[1],img.shape[0]))
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
