import cv2
import numpy as np

a=0
a=int(input('Enter 1 for Videocam else 0 '))

if a==1:
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,img=cap.read()
    else:
        ret=False
else:
    img=cv2.imread('a.jpg',0)

def func(x):
    pass

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
if a==1:
    w=int(cap.get(3))
    h=int(cap.get(4))
else:
    h,w=img.shape
cv2.createTrackbar('name1','image',w,w,func)
cv2.createTrackbar('name2','image',h,h,func)
tx=0
ty=0

while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        img=cv2.imread('a.jpg',0)
    r,c=img.shape
    x=cv2.getTrackbarPos('name1','image')
    y=cv2.getTrackbarPos('name2','image')
    tx=x-w
    ty=y-h
    p=np.float32([[1,0,tx],[0,1,ty]])
    img=cv2.warpAffine(img,p,(c,r))
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print(p)
cv2.destroyAllWindows()
if a==1:
    cap.release()
   
