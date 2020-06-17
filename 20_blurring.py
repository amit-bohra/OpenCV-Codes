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
    img=cv2.imread('taj.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('name1','image',3,25,func)
cv2.createTrackbar('name2','image',50,200,func)
x=3
y=50
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('taj.jpg')
    x=cv2.getTrackbarPos('name1','image')
    y=cv2.getTrackbarPos('name2','image')
    if x<2:
        x=3
    if x%2==0:
        x+=1
    if y<50:
        y=50
    kernel=(np.ones((x,x),np.float32))/(x**2)
    img1=cv2.filter2D(img,-1,kernel)
    img2=cv2.blur(img,(x,x))
    img3=cv2.boxFilter(img,-1,(x,x))
    img4=cv2.bilateralFilter(img,x,y,y)
    img5=cv2.GaussianBlur(img,(x,x),0)
    kern=cv2.getGaussianKernel((x*x),0)
    kern=kern.reshape((x,x))
    img6=cv2.medianBlur(img,x)
    img7=cv2.boxFilter(img,-1,(x,x),normalize=False)
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
        print('kernel size',x)
        print('bilateral y',y)
        print('gaussian kernel', kern)
cv2.destroyAllWindows()
if a==1:
    cap.release()
