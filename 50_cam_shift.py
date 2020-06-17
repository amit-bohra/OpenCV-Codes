import cv2
import numpy as np


def func(x):
    pass

cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
        
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('in11','image',172,180,func)
cv2.createTrackbar('in12','image',161,255,func)
cv2.createTrackbar('in13','image',91,255,func)
cv2.createTrackbar('in21','image',31,180,func)
cv2.createTrackbar('in22','image',112,255,func)
cv2.createTrackbar('in23','image',136,255,func)
cv2.createTrackbar('iter','image',62,100,func)
cv2.createTrackbar('point','image',1,100,func)
cv2.createTrackbar('kern1','image',13,255,func)
cv2.createTrackbar('val1','image',2,2,func)
cv2.createTrackbar('kern2','image',5,255,func)
cv2.createTrackbar('val2','image',0,2,func)
#cv2.createTrackbar('it','image',0,255,func)
roi=cv2.selectROI(frame,False)
c,r,w,h=roi
track_window=(c,r,w,h)
roi=frame[r:r+h,c:c+w]
hsv_roi=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
while True:
    a=cv2.getTrackbarPos('in11','image')
    b=cv2.getTrackbarPos('in12','image')
    c=cv2.getTrackbarPos('in13','image')
    d=cv2.getTrackbarPos('in21','image')
    e=cv2.getTrackbarPos('in22','image')
    f=cv2.getTrackbarPos('in23','image')
    g=cv2.getTrackbarPos('iter','image')
    h=cv2.getTrackbarPos('point','image')
    k1=cv2.getTrackbarPos('kern1','image')
    v1=cv2.getTrackbarPos('val1','image')
    k2=cv2.getTrackbarPos('kern2','image')
    v2=cv2.getTrackbarPos('val2','image')
    #it=cv2.getTrackbarPos('it','image')
    if k1<1:
        k1=1
    if k1%2==0:
        k1+=1
    if k2<1:
        k2=1
    if k2%2==0:
        k2+=1
    kernel1=cv2.getStructuringElement(v1,(k1,k1))
    kernel2=cv2.getStructuringElement(v2,(k2,k2))
    lower=np.array([a,b,c]) 
    higher=np.array([a+d,b+e,c+f])
    mask=cv2.inRange(frame,lower,higher)
    roi_hist=cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
    cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
    term_crit=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,g,h)
    ret,img=cap.read()
    if ret==True:
        img=cv2.flip(img,1)
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        dst=cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        dst=cv2.morphologyEx(dst,cv2.MORPH_CLOSE,kernel1)
        dst=cv2.morphologyEx(dst,cv2.MORPH_OPEN,kernel2)
        dst=cv2.GaussianBlur(dst,(5,5),0)
        ret,track_window=cv2.CamShift(dst,track_window,term_crit)
        pts=cv2.boxPoints(ret)
        pts=np.int0(pts)
        cv2.polylines(img,[pts],True,255,2)
        cv2.imshow('image1',img)
        cv2.imshow('dst',dst)
        if cv2.waitKey(1)==27:
            break
        if cv2.waitKey(1)==ord('p'):
            print()
    else:
        break
cv2.destroyAllWindows()
cap.release()
