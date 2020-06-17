import cv2
import numpy
from copy import deepcopy as dp

start_row=0
end_row=1
start_col=0
end_col=1
flag=0
mask=0
select_flag=0
a=0

def func(x):
    pass
def masked(event,x,y,flags,param):
    global a,start_row,start_col,end_row,end_col,flag,mask,select_flag,img
    if event==cv2.EVENT_LBUTTONDOWN:
        start_row=y
        start_col=x
        select_flag=1
    if event==cv2.EVENT_MOUSEMOVE:
        if select_flag==1:
            end_row=y+1
            end_col=x+1
            min_row=min(start_row,end_row)
            max_row=max(start_row,end_row)
            min_col=min(start_col,end_col)
            max_col=max(start_col,end_col)
            mask=tmg[min_row:max_row,min_col:max_col]
            b=(str(min_row)+':'+str(max_row)+','+str(min_col)+':'+str(max_col))
            if a!=b:
                a=b
            flag=1
            cv2.rectangle(img,(start_col,start_row),(end_col-1,end_row-1),(0,0,255),-1)
    if event==cv2.EVENT_LBUTTONUP:
        select_flag=0
        img=dp(tmg)
        
inp=0
inp=int(input('Enter 1 for VideoCam else 0 '))
if inp==1:
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,img=cap.read()
    else:
        ret=False
else:
    img=cv2.imread('a.jpg')
tmg=dp(img)
roi=dp(img)
cv2.namedWindow('image')
cv2.namedWindow('mask')
cv2.setMouseCallback('image',masked)
cv2.createTrackbar('blur','image',0,255,func)
cv2.createTrackbar('ellipse','image',1,255,func)
cv2.createTrackbar('block','image',3,255,func)
cv2.createTrackbar('constant','image',1,255,func)
cv2.createTrackbar('kernel','image',1,255,func)
while True:
    k=cv2.getTrackbarPos('kernel','image')
    if k<1:
        k=1
    if k%2==0:
        k+=1
    kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(k,k))
    blur=cv2.getTrackbarPos('blur','image')
    if blur%2==0:
        blur+=1
    block=cv2.getTrackbarPos('block','image')
    if block<3:
        block=3
    if block%2==0:
        block+=1
    constant=cv2.getTrackbarPos('constant','image')
    if constant<1:
        constant=1
    x=cv2.getTrackbarPos('ellipse','image')
    if x%2==0:
        x+=1
    if x<1:
        x=1
    if inp==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('a.jpg')
    img=cv2.GaussianBlur(img,(blur,blur),0)
    roi=dp(img)
    tmg=dp(img)
    target=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    if a!=0 :
        try:
            needed=cv2.cvtColor(mask,cv2.COLOR_BGR2HSV)
        except cv2.error:
            pass
        neededhist=cv2.calcHist([needed],[0,1],None,[180,256],[0,180,0,256])

        cv2.normalize(neededhist,neededhist,0,255,cv2.NORM_MINMAX)
        back=cv2.calcBackProject([target],[0,1],neededhist,[0,180,0,256],1)

        disc=cv2.getStructuringElement(cv2.MORPH_RECT,(x,x))
        cv2.filter2D(back,-1,disc,back)

        thresh=cv2.adaptiveThreshold(back,255,cv2.THRESH_BINARY,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,block,constant)
        thresh=cv2.merge((thresh,thresh,thresh))
        output=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
        res=cv2.bitwise_and(target,thresh)
    cv2.imshow('image',img)
    if flag==1:
        try:
            cv2.imshow('res',res)
            cv2.imshow('thresh',output)
            cv2.imshow('mask',mask)
        except cv2.error:
            pass
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print(a)
cv2.destroyAllWindows()
if inp==1:
    cap.release()
