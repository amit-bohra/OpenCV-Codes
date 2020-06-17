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
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.namedWindow('other',cv2.WINDOW_NORMAL)

cv2.createTrackbar('mini','img',1,255,func)
cv2.createTrackbar('maxi','img',1,255,func)
cv2.createTrackbar('p','img',1,255,func)
cv2.createTrackbar('t','img',25,360,func)
cv2.createTrackbar('thresh','img',1,255,func)
cv2.createTrackbar('size','img',100,500,func)
cv2.createTrackbar('gap','img',1,500,func)
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('sudoku.jpg')
    mini=cv2.getTrackbarPos('mini','img')
    maxi=cv2.getTrackbarPos('maxi','img')
    p=cv2.getTrackbarPos('p','img')
    t=cv2.getTrackbarPos('t','img')
    thresh=cv2.getTrackbarPos('thresh','img')
    size=cv2.getTrackbarPos('size','img')
    gap=cv2.getTrackbarPos('gap','img')
    if size<1:
        size=1
    if gap<1:
        gap=1
    if t<1:
        t=1
    if p<1:
        p=1
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(gray,mini,maxi)
##    lines=cv2.HoughLinesP(edges,p,t/180,thresh,size,gap)
##    if lines is not None:
##        for i in lines:
##            for x1,y1,x2,y2 in i:
##                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    
    lines=cv2.HoughLines(edges,p,t/180,thresh)
    for i in lines:
        for rho,theta in i:
            a1 = np.cos(theta)
            b1 = np.sin(theta)
            x0 = a1*rho
            y0 = b1*rho
            x1 = int(x0 + 1000*(-b1))
            y1 = int(y0 + 1000*(a1))
            x2 = int(x0 - 1000*(-b1))
            y2 = int(y0 - 1000*(a1))
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.imshow('image',img)
    cv2.imshow('other',edges)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print(len(lines))
cv2.destroyAllWindows()
if a==1:
    cap.release()
    
