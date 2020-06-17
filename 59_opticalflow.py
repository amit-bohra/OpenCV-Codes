import cv2
import numpy as np


def func(x):
    pass

cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,img=cap.read()
else:
    ret=False

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('corner','image',70,1000,func)
cv2.createTrackbar('quality','image',5,999,func)
cv2.createTrackbar('dist','image',10,300,func)
cv2.createTrackbar('rad','image',5,150,func)

while True:
    ret,img=cap.read()
    img=cv2.flip(img,1)
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    c=cv2.getTrackbarPos('corner','image')
    q=cv2.getTrackbarPos('quality','image')
    d=cv2.getTrackbarPos('dist','image')
    r=cv2.getTrackbarPos('rad','image')
    q=q/1000
    if d<1:
        d=10
    if q==0:
        q+=0.001
    corners=cv2.goodFeaturesToTrack(imggray,c,q,d)
    torners=np.int0(corners)
    for i in torners:
        x,y=i.ravel()
        cv2.circle(img,(x,y),r,255,-1)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        prevPts=corners
        prevgray=imggray
        prevframe=img
        mask=np.zeros_like(prevframe)
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()

cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('winsize','image',100,500,func)
cv2.createTrackbar('iter','image',1,20,func)
cv2.createTrackbar('point','image',1,1000,func)
while True:
    ret,img=cap.read()
    img=cv2.flip(img,1)
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    s=cv2.getTrackbarPos('winsize','image')
    i=cv2.getTrackbarPos('iter','image')
    p=cv2.getTrackbarPos('point','image')
    p=p/100
    if s<3:
        s=3
    lk_params=dict(winSize=(s,s),maxLevel=2,criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, i,p))
    nextPts,status,err=cv2.calcOpticalFlowPyrLK(prevgray,imggray,prevPts,None,**lk_params)
    good_new=nextPts[status==1]
    good_prev=prevPts[status==1]
    for new,prev in zip(good_new,good_prev):
        x_new,y_new=new.ravel()
        xprev,yprev=prev.ravel()
        #cv2.line(mask,(x_new,y_new),(xprev,yprev),(0,255,0),3)
        cv2.circle(img,(x_new,y_new),8,(0,0,255),-1)
    img=cv2.add(img,mask)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    prevgray=imggray.copy()
    prevPts=good_new.reshape(-1,1,2)
cv2.destroyAllWindows()
cap.release()    
    
