import cv2
import numpy as np
import matplotlib.pyplot
import time


cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
angle=0
scale=1
flag=0
while ret:
    ret,frame=cap.read()
    row,col,lay=frame.shape
    r=cv2.getRotationMatrix2D((col//2,row//2),angle,scale)
    output=cv2.warpAffine(frame,r,(col,row))
    angle+=6
    if flag==0:
        scale-=0.01
    if flag==1:
        scale+=0.01
    if scale<=0:
        flag=1
        scale=0
    if scale>=1.2:
        flag=0
        scale=1.2
    if angle>=360:
        angle=0
    #time.sleep(0.0001)
    cv2.imshow('rotation',output)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
