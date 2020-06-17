import cv2
import numpy as np
from copy import deepcopy as dp

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
cv2.createTrackbar('nfeatures','image',500,10000,func)
cv2.createTrackbar('table_number','image',6,100,func)
cv2.createTrackbar('key size','image',12,31,func)
cv2.createTrackbar('multi','image',1,100,func)
cv2.createTrackbar('flag','image',0,2,func)
cv2.createTrackbar('check','image',100,500,func)
while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('a.jpg')
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    tmggray=cv2.imread('color.png',0)
    x=cv2.getTrackbarPos('nfeatures','image')
    y=cv2.getTrackbarPos('table_number','image')
    z=cv2.getTrackbarPos('key size','image')
    n1=cv2.getTrackbarPos('multi','image')
    d=cv2.getTrackbarPos('flag','image')
    c=cv2.getTrackbarPos('check','image')
    if d==0:
        f=0
    if d==1:
        f=2
    if d==2:
        f=4
    if z<1:
        z=1
    if z>32:
        z=32
    orb=cv2.ORB_create(nfeatures=x)
    kp1,des1=orb.detectAndCompute(imggray,None)
    kp2,des2=orb.detectAndCompute(tmggray,None)
    FLANN_INDEX_LSH=6
    index_params=dict(algorithm=FLANN_INDEX_LSH,
                     table_number=y,
                     key_size=z,
                     multi_probe_level=n1)
    search_params=dict(checks=c)
    flann=cv2.FlannBasedMatcher(index_params,search_params)
    matches=flann.knnMatch(des1,des2,k=2)
    matchesMask=[[0,0] for i in range(len(matches))]
    try:
        for i,[m,n] in enumerate(matches):
            if m.distance < 0.7*n.distance:
                matchesMask[i]=[1,0]
    except ValueError:
        pass
    img3=cv2.drawMatchesKnn(imggray,kp1,tmggray,kp2,matches,None,matchesMask = matchesMask,matchColor=(255,0,0),flags=f,singlePointColor=(0,255,0))    
    cv2.imshow('image',img3)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print(matches)
cv2.destroyAllWindows()
if a==1:
    cap.release()
