import cv2
import numpy as np
import matplotlib.pyplot as plt

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
cv2.createTrackbar('name1','image',2,255,func)
cv2.createTrackbar('clip','image',8,255,func)
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('a.jpg')
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    x=cv2.getTrackbarPos('name1','image')
    y=cv2.getTrackbarPos('clip','image')
    equ=cv2.equalizeHist(img1)
    if x<1:
        x=1
    clahe=cv2.createCLAHE(clipLimit=y,tileGridSize=(x,x))
    cl1=clahe.apply(img1)
    cv2.imshow('image',cl1)
    cv2.imshow('image1',equ)
    cv2.imshow('image2',img1)
    hist1=cv2.calcHist([img1],[0],None,[256],[0,256])
    hist2=cv2.calcHist([equ],[0],None,[256],[0,256])
    hist3=cv2.calcHist([cl1],[0],None,[256],[0,256])
    #plt.plot(hist1,'red')
    #plt.plot(hist2,'blue')
    plt.plot(hist3,'green')
    plt.show(block=False)
    plt.pause(1)
    plt.close()
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
