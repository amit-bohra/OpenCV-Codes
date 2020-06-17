import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy as dp

listy=['haarcascade_frontalface_default.xml','haarcascade_frontalface_alt_tree.xml','haarcascade_frontalface_alt2.xml','haarcascade_frontalface_alt.xml']
face_cascade=cv2.CascadeClassifier(listy[0])
tracker=cv2.TrackerTLD_create()

cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,img=cap.read()
else:
    ret=False

flag=0
while ret:
    ret,img=cap.read()
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_rect=face_cascade.detectMultiScale(img1,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
        roi=(x,y,w,h)
        flag=1
    cv2.imshow('image',img)
    cv2.waitKey(1)
    if flag==1:
        break

ret=tracker.init(img,roi)
flag=0
while True:
    ret,img=cap.read()
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_rect=face_cascade.detectMultiScale(img1,scaleFactor=1.2,minNeighbors=5)
    if len(face_rect)==0:
        flag=0
    for (x,y,w,h) in face_rect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
        roi=(x,y,w,h)
        ret=tracker.init(img,roi)
        flag=1
    if flag==0:
        success,roi=tracker.update(img)
        (x,y,w,h)=tuple(map(int,roi))
        if success:
            p1=(x,y)
            p2=(x+w,y+h)
            cv2.rectangle(img,p1,p2,(0,255,0),4)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
print(roi)
        
    
