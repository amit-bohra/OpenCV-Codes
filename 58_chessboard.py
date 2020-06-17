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
    img=cv2.imread('chess.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('x','image',3,255,func)
cv2.createTrackbar('y','image',3,255,func)


while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('grid.png')
    img=cv2.resize(img,(500,500))
    x=cv2.getTrackbarPos('x','image')
    y=cv2.getTrackbarPos('y','image')
    if x<3:
        x=3
    if y<3:
        y=3
    #found,corners=cv2.findChessboardCorners(img,(x,y))
    found,corners=cv2.findCirclesGrid(img,(x,y),cv2.CALIB_CB_SYMMETRIC_GRID)
    if found:
        img=cv2.drawChessboardCorners(img,(x,y),corners,found)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
