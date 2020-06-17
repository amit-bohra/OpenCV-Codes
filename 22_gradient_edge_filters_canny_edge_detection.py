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
cv2.createTrackbar('name1','image',1,10,func)
cv2.createTrackbar('name2','image',1,100,func)
cv2.createTrackbar('name3','image',1,255,func)
cv2.createTrackbar('name4','image',1,255,func)
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('abc.png',0)
    x=cv2.getTrackbarPos('name1','image')
    b=cv2.getTrackbarPos('name2','image')
    mini=cv2.getTrackbarPos('name3','image')
    maxi=cv2.getTrackbarPos('name4','image')
    maxi=mini+maxi
    b/=100
    if x<1:
        x=1
    if x%2==0:
        x+=1
    img1=cv2.Laplacian(img,-1,cv2.CV_64F,ksize=x,scale=1,delta=0)
    sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=x)
    sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=x)
    scharrx=cv2.Scharr(img,cv2.CV_64F,dx=1,dy=0,scale=1,delta=0)
    scharry=cv2.Scharr(img,cv2.CV_64F,dx=0,dy=1)
    img4=cv2.Canny(img,mini,maxi)
    img3=cv2.addWeighted(scharrx,b,scharrx,1-b,0)
    img2=cv2.addWeighted(sobelx,b,sobely,1-b,0)
    img1=np.absolute(img1)
    img1=np.uint8(img1)
    img2=np.absolute(img2)
    img2=np.uint8(img2)
    img3=np.absolute(img3)
    img3=np.uint8(img3)
##    img5=np.hstack((img1,img2))
##    img6=np.hstack((img3,img4))
##    img7=np.vstack((img5,img6))
    cv2.imshow('image',img4)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
