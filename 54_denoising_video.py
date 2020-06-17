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
        img=cv2.flip(img,1)
    else:
        ret=False
else:
    img=cv2.imread('a.jpg')
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('h','image',35,255,func)
cv2.createTrackbar('t','image',7,255,func)
cv2.createTrackbar('s','image',21,255,func)
count=0
imglist=[]
noise=np.random.randn(*img[1].shape)*10
while True:
    count+=1
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('a.jpg')
    h=cv2.getTrackbarPos('h','image')
    t=cv2.getTrackbarPos('t','image')
    s=cv2.getTrackbarPos('s','image')
    if t<1:
        t=1
    if s<1:
        s=1
    if t%2==0:
        t+=1
    if s%2==0:
        s+=1
    if count<5:
        float64=np.float64(img)
        float64=float64+noise
        noised=np.uint8(np.clip(float64,0,255))
        imglist.append(noised)
        continue
    else:
        count=0
        dst=cv2.fastNlMeansDenoisingColoredMulti(imglist,2,3,None,t,s,h)
        img3=np.hstack((img,dst))
        cv2.imshow('image',img3)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
