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
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        ret=False
else:
    img=cv2.imread('abc.png',0)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('min_canny','image',0,255,func)
cv2.createTrackbar('max_canny','image',0,255,func)
ind=0
z=0
temp=0
cv2.createTrackbar('index','image',0,1,func)
cv2.createTrackbar('blur','image',3,100,func)
cv2.createTrackbar('kernel','image',3,100,func)
cv2.createTrackbar('iteration','image',1,50,func)
while True:
    if a==1:
        ret,img=cap.read()
        imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        img=cv2.imread('abc.png',0)
    x=cv2.getTrackbarPos('min_canny','image')
    y=cv2.getTrackbarPos('max_canny','image')
    z=cv2.getTrackbarPos('index','image')
    g=cv2.getTrackbarPos('blur','image')
    k=cv2.getTrackbarPos('kernel','image')
    it=cv2.getTrackbarPos('iteration','image')
    if g%2==0:
        g+=1
    if g<=2:
        g=3
    if it<1:
        it=1
    if k<=2:
        k=3
    if k%2==0:
        k+=1
    img0=cv2.GaussianBlur(img,(g,g),0)
    img1=cv2.Canny(img0,x,x+y)
    img2=cv2.dilate(img1,cv2.getStructuringElement(cv2.MORPH_RECT,(k,k)),iterations=it)
    img3=cv2.Canny(img,x,x+y,L2gradient=True)
    contours,hierarchy=cv2.findContours(img2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #area=[cv2.contourArea(contours[x]) for x in range(len(contours)) ]
    perimeter=[cv2.arcLength(contours[x],False) for x in range(len(contours))]
    if len(perimeter)!=0:   #len(area)!=0:
        max_ar=max(perimeter)
        ind_max_ar=perimeter.index(max_ar)
        cnt=contours[ind_max_ar]
        tx,ty,bx,by=cv2.boundingRect(cnt)
        #cv2.rectangle(img,(tx,ty),(tx+bx,ty+by),(0,255,0),2)
        #img=cv2.drawContours(img,contours,ind_max_ar,(0,255,0),3)
        M=cv2.moments(cnt)
        epsilon=0.01*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(img,[approx],-1,(0,0,0),5)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.circle(img,(cx,cy),10,(0,0,255),-1)
    if temp!=z:
        ind+=1
        temp=z
        if ind>=len(hierarchy[0]):
            ind=0
        print(ind)
    cv2.imshow('image',img)
    cv2.imshow('canny',img2)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print('approx',approx)
        print('moment',M)
        print('min',x)
        print('max',x+y)
        print('contours len', len(contours))
        print('contours',contours)
        print('len hierarchy[0]',len(hierarchy[0]))
        print(hierarchy)
cv2.destroyAllWindows()
if a==1:
    cap.release()
