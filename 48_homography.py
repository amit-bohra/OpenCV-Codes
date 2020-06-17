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
cv2.createTrackbar('algo','image',1,1,func)
cv2.createTrackbar('min_match','image',10,1000,func)
cv2.createTrackbar('aise','image',1,10,func)
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
    algo=cv2.getTrackbarPos('algo','image')
    min_match=cv2.getTrackbarPos('min_match','image')
    f=float(cv2.getTrackbarPos('aise','image'))
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
    good=[]
    try:
        for m,n in matches:
            if m.distance<0.7*n.distance:
                good.append(m)
    except ValueError:
        pass
    if len(good)>min_match:
        src_pts=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
        dst_pts=np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
        M,mask=cv2.findHomography(src_pts,dst_pts,  cv2.RANSAC,f)
        matchesMask=mask.ravel().tolist()
        h,w=imggray.shape
        pts=np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
        dst=cv2.perspectiveTransform(pts,M)
        tmggray=cv2.polylines(tmggray,[np.int32(dst)],True,255,3,cv2.LINE_AA)
    else:
        matchesMask=None
    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)
    img3 = cv2.drawMatches(imggray,kp1,tmggray,kp2,good,None,**draw_params)    
    cv2.imshow('image1',img3)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print(matches)
cv2.destroyAllWindows()
if a==1:
    cap.release()
