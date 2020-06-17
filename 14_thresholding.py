import cv2
import numpy as np

a=0
a=int(input("Enter 1 for Videocam else 0 "))


def func(x):
    pass

if a==1:
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,img=cap.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        ret=False
else:
    img=cv2.imread('a.jpg',0)
    
img=cv2.resize(img,(300,300))    
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('name','image',127,255,func)
cv2.createTrackbar('name1','image',11,299,func)
cv2.createTrackbar('name2','image',2,100,func)


thresh_val=127
neighbour=11
cval=2
while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    thresh_val=cv2.getTrackbarPos('name','image')
    ret1,thresh1=cv2.threshold(img,thresh_val,255,cv2.THRESH_BINARY)
    ret2,thresh2=cv2.threshold(img,thresh_val,255,cv2.THRESH_BINARY_INV)
    ret3,thresh3=cv2.threshold(img,thresh_val,255,cv2.THRESH_TOZERO)
    ret4,thresh4=cv2.threshold(img,thresh_val,255,cv2.THRESH_TOZERO_INV)
    ret5,thresh5=cv2.threshold(img,thresh_val,255,cv2.THRESH_TRUNC)
    ret6,thresh6=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    neighbour=cv2.getTrackbarPos('name1','image')
    if neighbour%2==0:
        neighbour+=1
    if neighbour<2:
        neighbour=3
    cval=cv2.getTrackbarPos('name2','image')
    thresh7=cv2.adaptiveThreshold(img,255,cv2.THRESH_BINARY,cv2.ADAPTIVE_THRESH_MEAN_C,neighbour,cval)
    thresh8=cv2.adaptiveThreshold(img,255,cv2.THRESH_BINARY,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,neighbour,cval)
    img1=np.hstack((thresh1,thresh2))
    img2=np.hstack((thresh3,thresh4))
    img3=np.hstack((thresh5,thresh6))
    img4=np.hstack((thresh7,thresh8))
    img5=np.vstack((img1,img2,))
    img6=np.vstack((img3,img4))
    img7=np.vstack((img5,img6))
    cv2.imshow('image',img7)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print('binary',ret1)
        print('binary_inv',ret2)
        print('thresh_zero',ret3)
        print('thresh_zero_inv',ret4)
        print('thresh_trunc',ret5)
        print('otsu',ret6)
        print('neighbour block size',neighbour)
        print('constant value',cval)
cv2.destroyAllWindows()
if a==1:
    cap.release()
