import cv2
import matplotlib.pyplot as plt
import numpy as np


cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
while(ret):
    ret,frame=cap.read()
    output1=cv2.Canny(frame,0,200,L2gradient=False)
    output2=cv2.Canny(frame,0,300,L2gradient=True)
    cv2.imshow('original',frame)
    cv2.imshow('l1',output1)
    cv2.imshow('l2',output2)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
