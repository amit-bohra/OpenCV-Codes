import cv2
import numpy as np


def func(x):
    pass

cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,img1=cap.read()
    img1=cv2.flip(img1,1)
else:
    ret=False

cv2.namedWindow('image',cv2.WINDOW_NORMAL)

roi1=cv2.selectROI(img1,False)
y1=0
if y1==0:
    tracker=cv2.TrackerBoosting_create()
if y1==1:
    tracker=cv2.TrackerMIL_create()
if y1==2:
    tracker=cv2.TrackerKCF_create()
if y1==3:
    tracker=cv2.TrackerTLD_create()
if y1==4:
    tracker=cv2.TrackerMedianFlow_create()
ret=tracker.init(img1,roi1)
while True:
    ret,img=cap.read()
    img=cv2.flip(img,1)
    success,roi=tracker.update(img)
    (x,y,w,h)=tuple(map(int,roi))
    if success:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()

