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
    k=np.array(([0,-1,0],[-1,5,-1],[0,-1,0]),np.float32)
    frame=cv2.filter2D(frame,-1,k)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output1=cv2.Canny(gray,0,200,L2gradient=False)
    output2=cv2.Canny(gray,0,300,L2gradient=True)
    lines1=cv2.HoughLines(output1,1,np.pi/180,200)
    lines2=cv2.HoughLines(output2,1,np.pi/180,200)
    if lines1 is not None:
        for rho,theta in lines1[0]:
            a=np.cos(theta)
            b=np.sin(theta)
            x0=a*rho
            y0=b*rho
            pts1=(int(x0+1000*(-b)),int(y0+1000*(a)))
            pts2=(int(x0-1000*(-b)),int(y0-1000*(a)))
            cv2.line(frame,pts1,pts2,(0,255,0),3)
    cv2.imshow('original',frame)
    cv2.imshow('l1',output1)
    cv2.imshow('l2',output2)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
