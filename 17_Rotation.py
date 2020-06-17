import cv2
import numpy as np


def func(x):
    pass

print('If you want to rotate by a specific position, click on that position\n then change the slider')

def draw(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        global r1,r2
        r1=x
        r2=y
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
    img=cv2.imread('a.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('name1','image',0,360,func)
cv2.setMouseCallback('image',draw)
r1=img.shape[1]
r2=img.shape[0]
r1=r1//2
r2=r2//2
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('a.jpg',0)
    x=cv2.getTrackbarPos('name1','image')
    M=cv2.getRotationMatrix2D((r1,r2),x,1)
    img=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
