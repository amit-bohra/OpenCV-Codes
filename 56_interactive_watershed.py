import cv2
import numpy as np
from copy import deepcopy as dp

aqua=(255,255,0)
marine=(116,139,69)
banana=(87,207,277)
blue=(255,0,0)
almond=(205,235,255)
brown=(64,64,255)
blue1=(255,245,152)
green=(0,100,0)
orange=(0,140,255)
orchid=(139,34,104)
pink=(147,20,255)
gold=(0,215,255)
gray=(127,127,127)
indigo=(130,0,75)

colors=[aqua,marine,banana,blue,almond,brown,blue1,green,orange,orchid,
        pink,gold,gray,indigo]



size=0
color=0

def draw(event,x,y,flags,param):
    global color,colors,img,marker,segment,tmg,size
    mark=color+1
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker,(x,y),size,mark,-1)
        cv2.circle(tmg,(x,y),size,colors[color],-1)
        marker_copy=dp(marker)
        cv2.watershed(img,marker_copy)
        segment=np.zeros(img.shape,np.uint8)
        for i in range(1,len(colors)+1):
            segment[marker_copy==i]=colors[i-1]

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
img=cv2.GaussianBlur(img,(1,1),0)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('color','image',0,len(colors)-1,func)
cv2.createTrackbar('size','image',10,200,func)
cv2.setMouseCallback('image',draw)
marker=np.zeros(img.shape[:2],np.int32)
segment=np.zeros(img.shape,np.uint8)
tmg=dp(img)
if a==1:
    cap.release()
while True:
    color=cv2.getTrackbarPos('color','image')
    size=cv2.getTrackbarPos('size','image')
    cv2.imshow('image',tmg)
    cv2.imshow('segment',segment)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
    if cv2.waitKey(1)==ord('c'):
        tmg=dp(img)
        marker=np.zeros(img.shape[:2],np.int32)
        segment=np.zeros(img.shape,np.uint8)
        color=0
cv2.destroyAllWindows()

