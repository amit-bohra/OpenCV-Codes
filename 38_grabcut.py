import cv2
import numpy as np
from copy import deepcopy as dp

drawflag=0

def func(x):
    pass

def draw(event,x,y,flags,param):
    global x1,y1,masked,drawflag,color,img,tmg
    if event==cv2.EVENT_LBUTTONDOWN:
        drawflag=1
    if drawflag==1:
        cv2.circle(masked,(x,y),y1,color,-1)
        if x1==2:
            a=y-y1
            b=y+y1
            c=x-x1
            d=x+x1
            if a<0:
                a=0
            if c<0:
                b=0
            if b>img.shape[0]:
                b=img.shape[0]
            if d>img.shape[1]:
                d=img.shape[1]
            img[a:b,c:d]=dp(tmg[a:b,c:d])
        else:
            cv2.circle(tmg,(x,y),y1,(0,255,0),-1)
    if event==cv2.EVENT_LBUTTONUP:
        drawflag=0
        
img=cv2.imread('a.jpg')
tmg=dp(img)
masked=np.zeros(img.shape[:2],np.uint8)
bgd=np.zeros((1,65),np.float64)
fgd=np.zeros((1,65),np.float64)
roi=cv2.selectROI(img,False)
rect=(roi[1],roi[0],roi[3],roi[2])
cv2.grabCut(img,masked,rect,bgd,fgd,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((masked==2)|(masked==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)
cv2.createTrackbar('color','image',0,2,func)
cv2.createTrackbar('size','image',0,200,func)
x1=0
y1=0
while True:
    x1=cv2.getTrackbarPos('color','image')
    y1=cv2.getTrackbarPos('size','image')
    if x1==0:
        color=255
    if x1==1:
        color=127
    if x1==2:
        color=0
    cv2.imshow('image',tmg)
    cv2.imshow('masked',masked)
    cv2.imshow('img',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('r'):
        masked=np.zeros(img.shape[:2],np.uint8)
        img=dp(tmg)
    if cv2.waitKey(1)==ord('s'):
        cv2.imwrite('masked.jpg',masked)
cv2.destroyAllWindows()

bgd=np.zeros((1,65),np.float64)
fgd=np.zeros((1,65),np.float64)
mask=np.zeros(img.shape[:2],np.uint8)
mask[masked==0]=0
mask[masked==255]=1
mask,bgd,fgd=cv2.grabCut(img,mask,None,bgd,fgd,5,cv2.GC_INIT_WITH_MASK)
mask2=np.where((masked==2)|(masked==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]
cv2.imshow('img',img)
cv2.waitKey(1)
