import cv2
import numpy as np
from copy import deepcopy as dp

flag=0
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
while ret:
    ret,frame=cap.read()
    if flag==0:
        trame=dp(frame)
        flag=1
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowgreen=np.array([40,50,50])
    highgreen=np.array([80,255,255])
    lowred=np.array([0,50,50])
    highred=np.array([20,255,255])
    lowblue=np.array([100,50,50])
    highblue=np.array([140,255,255])
    lowskin=np.array([0,58,50])
    highskin=np.array([30,255,255])
    greenmask=cv2.inRange(hsv,lowgreen,highgreen)
    redmask=cv2.inRange(hsv,lowred,highred)
    bluemask=cv2.inRange(hsv,lowblue,highblue)

    #color detection of skin
    copyframe=dp(frame)
    skinmask=cv2.inRange(hsv,lowred,highred)
    index=skinmask.nonzero()
    not_skinmask=dp(skinmask)
    not_skinmask[not_skinmask==0]=1
    not_skinmask[not_skinmask==255]=0
    not_skinmask[not_skinmask==1]=255
    nonindex=not_skinmask.nonzero()
    copyframe[index]=255
    copyframe[nonindex]=0
    #frame=cv2.addWeighted(frame,0.5,copyframe,0.5,0)
    #copyframe=np.vstack((copyframe,copyframe))

    cv2.imshow('original',frame)
    cv2.imshow('changed',copyframe)
    cv2.imshow('image_mask',skinmask)
    if cv2.waitKey(1)==27:
        break
    
cv2.destroyAllWindows()
cap.release()
