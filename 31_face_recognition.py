import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy as dp
#import face_recognition as fr
#from PIL import Image


listy=['haarcascade_frontalface_default.xml','haarcascade_frontalface_alt_tree.xml','haarcascade_frontalface_alt2.xml','haarcascade_frontalface_alt.xml']


def func(x):
    pass

a=0
a=int(input('Enter 1 for VideoCam else 0 '))
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('name1','image',0,3,func)
cv2.createTrackbar('tracker','image',0,4,func)
x=0
y=0
if y==0:
    tracker=cv2.TrackerBoosting_create()
if y==1:
    tracker=cv2.TrackerMIL_create()
if y==2:
    tracker=cv2.TrackerKCF_create()
if y==3:
    tracker=cv2.TrackerTLD_create()
if y==4:
    tracker=cv2.TrackerMedianFlow_create()
face_cascade=cv2.CascadeClassifier(listy[x])
while True:
    if a==1:
        cap=cv2.VideoCapture(0)
        if cap.isOpened():
            ret,img=cap.read()
        else:
            ret=False
    else:
        img=cv2.imread('a.jpg')
    tmg=dp(img)
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_rect=face_cascade.detectMultiScale(img1,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rect:
        roi=tmg[x:x+w,y:y+h]
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if len(face_rect)!=0:
        break
ret=tracker.init(img,tuple(roi))
while True:
    x=cv2.getTrackbarPos('name1','image')
    y=cv2.getTrackbarPos('tracker','image')
    if y==0:
        tracker=cv2.TrackerBoosting_create()
    if y==1:
        tracker=cv2.TrackerMIL_create()
    if y==2:
        tracker=cv2.TrackerKCF_create()
    if y==3:
        tracker=cv2.TrackerTLD_create()
    if y==4:
        tracker=cv2.TrackerMedianFlow_create()
    face_cascade=cv2.CascadeClassifier(listy[x])
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('a.jpg')
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_rect=face_cascade.detectMultiScale(img1,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rect:
        roi=img[x:x+w,y:y+h]
        success,roi=tracker.update(img)
        (x,y,w,h)=tuple(map(int,roi))
        if success:
            p1=(x,y)
            p2=(x+w,y+h)
            cv2.rectangle(img,p1,p2,(0,255,255),3)
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),10)
##    face_locations=fr.face_locations(img)
##    for fl in face_locations:
##        top,right,bottom,left=fl
##        cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),-1)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
