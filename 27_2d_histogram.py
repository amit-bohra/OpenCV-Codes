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
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v=cv2.split(img1)
    x=cv2.getTrackbarPos('name1','image')
    y=cv2.getTrackbarPos('clip','image')
    hist1=cv2.calcHist([img1],[0,1],None,[180,256],[0,180,0,256])
    nphist,xbins,ybins=np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]]) 
    plt.imshow(hist1,interpolation='nearest')
    plt.imshow(nphist,interpolation='nearest')
    plt.show()
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
