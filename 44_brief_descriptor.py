import cv2
import numpy as np


def func(x):
    pass
a=0
a=int(input('Enter 1 for VideoCam else 0 '))
if a==1:
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,img=cap.read()
    else:
        ret=False
else:
    img=cv2.imread('a.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('a.jpg')
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    star = cv2.xfeatures2d.StarDetector_create()
    brief=cv2.xfeatures2d.BriefDescriptorExtractor_create()
    kp=star.detect(imggray,None)
    img=cv2.drawKeypoints(img,kp,None,color=(255,0,0))
    kp,des=brief.compute(img,kp)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
