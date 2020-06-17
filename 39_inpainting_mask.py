import cv2
import numpy as np
from copy import deepcopy as dp

drawflag=0

def func(x):
    pass

def draw(event,x,y,flags,param):
    global x1,y1,masked,drawflag,color,img,tmg
    if event==cv2.EVENT_LBUTTONDOWN:
        drawflag=1
    if drawflag==1:
        cv2.circle(masked,(x,y),y1,color,-1)
        if x1==2:
            a=y-y1
            b=y+y1
            c=x-x1
            d=x+x1
            if a<0:
                a=0
            if c<0:
                b=0
            if b>img.shape[0]:
                b=img.shape[0]
            if d>img.shape[1]:
                d=img.shape[1]
            img[a:b,c:d]=dp(tmg[a:b,c:d])
        else:
            cv2.circle(img,(x,y),y1,(0,255,0),-1)
    if event==cv2.EVENT_LBUTTONUP:
        drawflag=0
        
img=cv2.imread('a.jpg')
tmg=dp(img)
masked=np.zeros(img.shape[:2],np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)
cv2.createTrackbar('color','image',0,2,func)
cv2.createTrackbar('size','image',0,200,func)
cv2.createTrackbar('a1','image',0,255,func)
cv2.createTrackbar('b1','image',0,1,func)
x1=0
y1=0
while True:
    x1=cv2.getTrackbarPos('color','image')
    y1=cv2.getTrackbarPos('size','image')
    a1=cv2.getTrackbarPos('a1','image')
    b1=cv2.getTrackbarPos('b1','image')
    if x1==0:
        color=255
    if x1==1:
        color=127
    if x1==2:
        color=0
    if b1<1:
        b1=1
    if b1%2==0:
        b+=1
    dst=cv2.inpaint(img,masked,a1,b1)
    cv2.imshow('dst',dst)
    cv2.imshow('image',img)
    cv2.imshow('masked',masked)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('r'):
        masked=np.zeros(img.shape[:2],np.uint8)
        img=dp(tmg)
    if cv2.waitKey(1)==ord('s'):
        print('saved')
        cv2.imwrite('masked.jpg',masked)
cv2.destroyAllWindows()
