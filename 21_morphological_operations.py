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
    img=cv2.imread('plate.jpg',0)
    img=cv2.resize(img,(300,300))
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('name1','image',3,255,func)
cv2.createTrackbar('name2','image',0,2,func)
cv2.createTrackbar('name3','image',1,50,func)
cv2.createTrackbar('name4','image',3,100,func)
#cv2.createTrackbar('name5','image',2,100,func)
u=11
v=2
while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        img=cv2.imread('plate.jpg',0)
        img=cv2.resize(img,(300,300))
    u=cv2.getTrackbarPos('name4','image')
    x=cv2.getTrackbarPos('name1','image')
    y=cv2.getTrackbarPos('name2','image')
    z=cv2.getTrackbarPos('name3','image')
    #v=cv2.getTrackbarPos('name5','image')
    if u<2:
        u=2
    if u%2==0:
        u+=1
    if z<1:
        z=1
    if x<2:
        x=2
    if x%2==0:
        x+=1
    if y==0:
        kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(x,x))
        r='Rectangle'
    if y==1:
        kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(x,x))
        r='Ellipse'
    if y==2:
        kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(x,x))
        r='cross'
    img=cv2.adaptiveThreshold(img,255,cv2.THRESH_BINARY,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,u,v)
    img1=cv2.erode(img,kernel,iterations=z)
    img2=cv2.dilate(img,kernel,iterations=z)
    img3=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    img4=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
    img5=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
    img6=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
    img7=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
    img8=np.hstack((img1,img2))
    img9=np.hstack((img3,img4))
    img10=np.hstack((img5,img6))
    img11=np.hstack((img7,img))
    img12=np.vstack((img8,img9))
    img13=np.vstack((img10,img11))
    img14=np.vstack((img12,img13)) 
    cv2.imshow('image',img14)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print('kernelsize',k)
        print('structuring_element',r)
cv2.destroyAllWindows()
if a==1:
    cap.release()
