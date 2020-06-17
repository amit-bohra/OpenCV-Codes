import cv2
import numpy as np
from copy import deepcopy as dp
import matplotlib.pyplot as plt

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
cv2.createTrackbar('name1','image',0,5,func)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
roi=cv2.selectROI(img)
x1,y1,w1,h1=roi
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
tmg=dp(img)
img2=tmg[y1:y1+h1,x1:x1+w1]
w, h = img2.shape[::-1]
while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('a.jpg')
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    x=cv2.getTrackbarPos('name1','image')
    method=eval(methods[x])
    res=cv2.matchTemplate(img,img2,method)
##    threshold=0.8
##    loc=np.where(res>=threshold)
##    for pt in zip(*loc[::-1]):
##        cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)


    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left=min_loc
    else:
        top_left=max_loc
    bottom_right=(top_left[0]+w,top_left[1]+h)
    cv2.rectangle(img,top_left,bottom_right,255,2)
    res=cv2.normalize(res,res,0,255,cv2.NORM_MINMAX)
    res=np.uint8(res)
    cv2.imshow('res',res)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print(min_val,max_val)
        print(min_loc,max_loc)
cv2.destroyAllWindows()
if a==1:
    cap.release()
