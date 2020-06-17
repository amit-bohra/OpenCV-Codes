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
    img=cv2.imread('sudoku.jpg')
cv2.namedWindow('image')
cv2.namedWindow('EDGE',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('acc','image',100,255,func)
cv2.createTrackbar('thresh','image',200,255,func)
cv2.createTrackbar('min','image',100,255,func)
cv2.createTrackbar('max','image',200,255,func)
cv2.createTrackbar('angle','image',1,180,func)
while True:
    x=cv2.getTrackbarPos('acc','image')
    y=cv2.getTrackbarPos('thresh','image')
    r=cv2.getTrackbarPos('min','image')
    s=cv2.getTrackbarPos('max','image')
    t=cv2.getTrackbarPos('angle','image')
    if s<1:
        s=1
    if t<1:
        t=1
    if x<1:
        x=1
    if y<1:
        y=1
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('sudoku.jpg')
    img1=cv2.resize(img,(500,500))
    #img2=cv2.GaussianBlur(img1,(3,3),0)
    img3=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(img3,r,s,apertureSize=3)
    #lines=cv2.HoughLines(edges,1,t/180,y)

    minlen=100
    mingap=10
    lines=cv2.HoughLinesP(edges,1,t/180,y,minlen,mingap)
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    
##    if len(lining)!=0:
##        for line in lining:
##            for rho,theta in line:
##                a1=np.cos(theta)
##                b1=np.sin(theta)
##                x0=a1*rho
##                y0=b1*rho
##                x1=int(x0 + 1000*(-b1))
##                y1=int(y0 + 1000*(a1))
##                x2 = int(x0 - 1000*(-b1))
##                y2 = int(y0 - 1000*(a1))
##                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.imshow('EDGE',edges)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
