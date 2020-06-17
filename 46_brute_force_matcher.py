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
cv2.createTrackbar('z','image',0,2,func)
cv2.createTrackbar('z=0 cross','image',0,1,func)
cv2.createTrackbar('z=0 number','image',10,3000,func)
cv2.createTrackbar('flag','image',0,2,func)
cv2.createTrackbar('dist','image',70,100,func)
while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('a.jpg')
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    tmggray=cv2.imread('color_face.png',0)#dp(imggray)
    x=cv2.getTrackbarPos('nfeatures','image')
    y=cv2.getTrackbarPos('z=0 cross','image')
    z=cv2.getTrackbarPos('z','image')
    n1=cv2.getTrackbarPos('z=0 number','image')
    d=cv2.getTrackbarPos('flag','image')
    dist=cv2.getTrackbarPos('dist','image')
    dist/=100
    if d==0:
        f=0
    if d==1:
        f=2
    if d==2:
        f=4
    orb=cv2.ORB_create(nfeatures=x)
    kp1,des1=orb.detectAndCompute(imggray,None)
    kp2,des2=orb.detectAndCompute(tmggray,None)
    if z==0:
        bf=cv2.BFMatcher(cv2.NORM_HAMMING)
        matches=bf.match(des1,des2)
        matches=sorted(matches,key=lambda x1: x1.distance)
        if n1>=len(matches):
            n1=len(matches)-1
        img3=cv2.drawMatches(imggray,kp1,tmggray,kp2,matches[:n1],None,matchColor=(255,0,0),flags=f,singlePointColor=(0,255,0))
    if z==1:
        bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
        matches=bf.knnMatch(des1,des2,k=1)
        img3=cv2.drawMatchesKnn(imggray,kp1,tmggray,kp2,matches,None,matchColor=(255,0,0),flags=f,singlePointColor=(0,255,0))
    if z==2:
        bf=cv2.BFMatcher()
        matches=bf.knnMatch(des1,des2,k=2)
        good=[]
        for m,n in matches:
            if m.distance < dist*n.distance:
                good.append([m])
        img3=cv2.drawMatchesKnn(imggray,kp1,tmggray,kp2,good,None,matchColor=(255,0,0),flags=f,singlePointColor=(0,255,0))
    cv2.imshow('image',img3)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print(matches)
cv2.destroyAllWindows()
if a==1:
    cap.release()
