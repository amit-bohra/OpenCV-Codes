import cv2
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy as dp


listy=['haarcascade_frontalface_default.xml','haarcascade_frontalface_alt_tree.xml','haarcascade_frontalface_alt2.xml','haarcascade_frontalface_alt.xml']
face_cascade=cv2.CascadeClassifier(listy[0])
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,img=cap.read()
else:
    ret=False

tracker=cv2.TrackerBoosting_create()
flag=0
while ret:
    ret,img=cap.read()
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    tmg=dp(img)
    face_rect=face_cascade.detectMultiScale(img1,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rect:
        roi = (x,y,w,h)
        cv2.rectangle(tmg,(x,y),(x+w,y+h),(0,255,0),4)
    cv2.imshow('image',tmg)
    cv2.waitKey(1)
    if len(face_rect)!=0:
        flag=1
        break
ret=tracker.init(img,roi)
flag1=0
flag2=1
while True:
    ret,img=cap.read()
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if flag2==1:
        success,roi=tracker.update(img)
        (x,y,w,h)=tuple(map(int,roi))
        if success:
            p1=(x,y)
            p2=(x+w,y+h)
            cv2.rectangle(img,p1,p2,(0,255,0),4)
    tmg=dp(img)
    face_rect=face_cascade.detectMultiScale(img1,minNeighbors=5)
    for (x,y,w,h) in face_rect:
        roi = (x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
        if len(face_rect)!=0:
            flag1=1
            flag2=0
    if flag1==1:
        ret=tracker.init(img,roi)
        flag1=0
        flag2=1
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
    
    
    
    
