import cv2
import numpy as np
import random as rd
import matplotlib.pyplot as plt


cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
while ret:
    ret,frame=cap.read()
    row,col,lay=frame.shape
    p=0.05
    output=np.zeros(frame.shape,np.uint8)
    for i in range(row):
        for j in range(col):
            r=rd.random()
            if r<p/2:
                output[i][j]=0
            elif r<p:
                output[i][j]=255
            else:
                output[i][j]=frame[i][j]
    cv2.imshow('output',output)
    cv2.imshow('original',frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
