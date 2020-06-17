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

cv2.createTrackbar('blur','img',1,255,func)
cv2.createTrackbar('a1','img',5,255,func)
cv2.createTrackbar('b1','img',100,255,func)
cv2.createTrackbar('c1','img',50,255,func)
cv2.createTrackbar('d1','img',30,360,func)
cv2.createTrackbar('rad','img',0,255,func)
cv2.createTrackbar('mrad','img',100,500,func)

while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('sudoku.jpg')
    blur=cv2.getTrackbarPos('blur','img')
    a1=cv2.getTrackbarPos('a1','img')
    b1=cv2.getTrackbarPos('b1','img')
    c1=cv2.getTrackbarPos('c1','img')
    d1=cv2.getTrackbarPos('d1','img')
    rad=cv2.getTrackbarPos('rad','img')
    mrad=cv2.getTrackbarPos('mrad','img')
    if blur<1:
        blur=1
    if blur%2==0:
        blur+=1
    if a1<1:
        a1=1
    if b1<1:
        b1=1
    if c1<1:
        c1=1
    if d1<1:
        d1=1
    blur=cv2.GaussianBlur(img,(blur,blur),0)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,a1,b1,param1=c1,param2=d1,minRadius=rad,maxRadius=mrad)
    if circles is not None:
        circles=np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print(len(circles))
cv2.destroyAllWindows()
if a==1:
    cap.release()
    
