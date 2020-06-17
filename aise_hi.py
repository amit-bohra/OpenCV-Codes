import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,binary=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
    cv2.imshow('color',img)
    cv2.imshow('gray',gray)
    cv2.imshow('binary',binary)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
