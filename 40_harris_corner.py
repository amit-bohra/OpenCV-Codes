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
cv2.createTrackbar('block','image',2,300,func)
cv2.createTrackbar('ksize','image',3,29,func)
cv2.createTrackbar('k','image',4,50,func)
cv2.createTrackbar('t','image',1,50,func)
cv2.createTrackbar('u','image',0,1000,func)
cv2.createTrackbar('v','image',0,1000,func)
cv2.createTrackbar('w','image',0,100,func)
cv2.createTrackbar('s','image',50,100,func)
cv2.createTrackbar('rad','image',0,100,func)
while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('a.jpg')
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    float32=np.float32(imggray)
    x=cv2.getTrackbarPos('block','image')
    ksize=cv2.getTrackbarPos('ksize','image')
    k=cv2.getTrackbarPos('k','image')
    t=cv2.getTrackbarPos('t','image')
    u=cv2.getTrackbarPos('u','image')
    v=cv2.getTrackbarPos('v','image')
    w=cv2.getTrackbarPos('w','image')
    s=cv2.getTrackbarPos('s','image')
    rad=cv2.getTrackbarPos('rad','image')
    s=50-s
    if rad<1:
        rad=1
    if w<1:
        w=1
    v=v/1000
    if x<1:
        x+=1
    if ksize<1:
        ksize=1
    if ksize%2==0:
        ksize+=1
    k=k/100
    t=t/100
    dst=cv2.cornerHarris(float32,x,ksize,k)
    dst=cv2.dilate(dst,None)
    ret,dst=cv2.threshold(dst,t*dst.max(),255,0)
    dst=np.uint8(dst)

    ret,labels,stats,centroids=cv2.connectedComponentsWithStats(dst)

    criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,u,v)
    corners=cv2.cornerSubPix(float32,np.float32(centroids),(w,w),(s,s),criteria)
    
    res=np.hstack((centroids,corners))
    res=np.int0(res)
    img[dst>t*dst.max()]=[0,0,255]
    #img[res[:,3],res[:,2]]=[0,255,0]
    for i in range(res[:,3].size):
        try:
            cv2.circle(img,(res[i,2],res[i,3]),rad,(0,255,0),-1)
        except OverflowError:
            pass
    cv2.imshow('image',dst)
    cv2.imshow('img',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
