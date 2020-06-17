import cv2
import numpy as np
import matplotlib.pyplot as plt


cap=cv2.VideoCapture(0)
ret,frame=cap.read()
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame+=(2*frame)
    cv2.imshow('original',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()

