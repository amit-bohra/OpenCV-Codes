import cv2
import numpy as np
from math import copysign
from math import log10

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
    img=cv2.imread('hand.jpg')
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('blur','image',12,200,func)
cv2.createTrackbar('thresh','image',2,3,func)
cv2.createTrackbar('block','image',255,255,func)
cv2.createTrackbar('constant','image',7,255,func)
cv2.createTrackbar('dilate_k','image',4,200,func)
cv2.createTrackbar('dilate_iter','image',1,200,func)
cv2.createTrackbar('erode_k','image',6,200,func)
cv2.createTrackbar('erode_iter','image',1,200,func)
cv2.createTrackbar('epsilon','image',1,100,func)
dk=3
di=1
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('hand.jpg')
        img=cv2.resize(img,(512,512))
    blur=cv2.getTrackbarPos('blur','image')
    thresh_val=cv2.getTrackbarPos('thresh','image')
    block=cv2.getTrackbarPos('block','image')
    constant=cv2.getTrackbarPos('constant','image')
    dk=cv2.getTrackbarPos('dilate_k','image')
    di=cv2.getTrackbarPos('dilate_iter','image')
    ek=cv2.getTrackbarPos('erode_k','image')
    ei=cv2.getTrackbarPos('erode_iter','image')
    epsilon=cv2.getTrackbarPos('epsilon','image')
    if blur%2==0:
        blur+=1
    if blur<1:
        blur=1
    if block%2==0:
        block+=1
    if block<3:
        block=3
    if dk%2==0:
        dk+=1
    if dk<1:
        dk=1
    if ek%2==0:
        ek+=1
    if ek<1:
        ek=1
    if epsilon<1:
        epsilon=1
    if di<1:
        di=1
    if ei<1:
        ei=1
    ep=epsilon/100
    imgblur=cv2.GaussianBlur(img,(blur,blur),0)
    imggray=cv2.cvtColor(imgblur,cv2.COLOR_BGR2GRAY)
    if thresh_val==0:
         thresh=cv2.adaptiveThreshold(imggray,255,cv2.THRESH_BINARY,cv2.ADAPTIVE_THRESH_MEAN_C,block,constant)
    if thresh_val==1:
         thresh=cv2.adaptiveThreshold(imggray,255,cv2.THRESH_BINARY_INV,cv2.ADAPTIVE_THRESH_MEAN_C,block,constant)
    if thresh_val==2:
         thresh=cv2.adaptiveThreshold(imggray,255,cv2.THRESH_BINARY,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,block,constant)
    if thresh_val==3:
         thresh=cv2.adaptiveThreshold(imggray,255,cv2.THRESH_BINARY_INV,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,block,constant)
    dkernel = np.ones((dk,dk),np.uint8)
    dilate=cv2.dilate(thresh,dkernel,iterations = di)
    ekernel = np.ones((ek,ek),np.uint8)
    erode=cv2.erode(dilate,ekernel,iterations = ei)
    contours,hierarchy=cv2.findContours(erode,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    area=[cv2.contourArea(contours[i]) for i in range(len(contours))]
    if len(area)!=0:
        max_index=area.index(max(area))
        cnt=contours[max_index]
        M=cv2.moments(cnt)
        huMoments = cv2.HuMoments(M)
        for i in range(7):
            huMoments[i]=-1*copysign(1.0,huMoments[i])*log10(abs(huMoments[i]))
            
        if len(M.keys())!=0 and M['m00']!=0:
            centroidx=int(M['m10']/M['m00'])
            centroidy=int(M['m01']/M['m00'])
            cv2.circle(img,(centroidx,centroidy),10,(0,0,255),10)

        rect=cv2.minAreaRect(cnt)
        box=cv2.boxPoints(rect)
        box=np.int0(box)
        #cv2.drawContours(img,[box],0,(0,0,255),5)

        tx,ty,w,h=cv2.boundingRect(cnt)
        #cv2.rectangle(img,(tx,ty),(tx+w,ty+h),(0,255,0),5)
        aspect_ratio=float(w/h)
        cnt_area=cv2.contourArea(cnt)
        rect_area=w*h
        extent=float(cnt_area)/rect_area

        (x,y),radius=cv2.minEnclosingCircle(cnt)
        center=(int(x),int(y))
        radius=int(radius)
        #cv2.circle(img,center,radius,(0,255,0),2)

        ellipse=cv2.fitEllipse(cnt)
        #cv2.ellipse(img,ellipse,(0,255,255),2)

        rows,cols=img.shape[:2]
        [vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
        lefty=int((-x*vy/vx)+y)
        righty=int(((cols-x)*vy/vx)+y)
        #cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

    dist0=cv2.pointPolygonTest(cnt,(0,0),True)
    distFalse0=cv2.pointPolygonTest(cnt,(0,0),False)
    distCent=cv2.pointPolygonTest(cnt,(centroidx,centroidy),True)
    distFalseCent=cv2.pointPolygonTest(cnt,(centroidx,centroidy),False)
    
    epsi=ep*cv2.arcLength(cnt,True)
    approx=cv2.approxPolyDP(cnt,epsi,True)
    cv2.drawContours(img,[approx],-1,(255,255,0),5)
    #cv2.drawContours(img,approx,-1,(0,255,200),10)

    (x,y),(Ma,ma),angle=cv2.fitEllipse(cnt)
    
    hull=cv2.convexHull(cnt)
    hull_area=cv2.contourArea(hull)
    solidity=float(cnt_area)/hull_area
    
    hull2=cv2.convexHull(cnt,returnPoints=False)
    defects=cv2.convexityDefects(cnt,hull2)
    for i in range(defects.shape[0]):
        s,e,f,d=defects[i,0]
        start=tuple(cnt[s][0])
        end=tuple(cnt[e][0])
        far=tuple(cnt[f][0])
        cv2.line(img,start,end,[0,255,0],3)
        cv2.circle(img,far,10,[0,0,255],-1)
    

    equi_diameter=np.sqrt(4*cnt_area/np.pi)

    mask=np.zeros(imggray.shape,np.uint8)

    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(imggray,mask=mask)
    mean_val=cv2.mean(imggray,mask=mask)

    leftmost=tuple(cnt[cnt[:,:,0].argmin()][0])
    rightmost=tuple(cnt[cnt[:,:,0].argmax()][0])
    topmost=tuple(cnt[cnt[:,:,1].argmin()][0])
    bottommost=tuple(cnt[cnt[:,:,1].argmax()][0])
    
    cv2.drawContours(mask,[cnt],0,mean_val,-1)
    pixelpoints=mask.nonzero()

    matrix=cv2.matchShapes(cnt,cnt,1,0.0)
    
    img1=cv2.bitwise_and(img,img,mask=mask)
    #cv2.drawContours(img,[hull],-1,(255,0,0),10)
    #cv2.drawContours(img,cnt,-1,(0,0,255),10)
    cv2.imshow('image_mask',img1)
    cv2.imshow('image',img)
    cv2.imshow('image1',img)
    cv2.imshow('thresh',erode)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print('huMoments',huMoments)
        print("shape match",matrix)
        print(dist0,distFalse0,distCent,distFalseCent)
        print(cv2.isContourConvex(cnt))
        print('aspect_ratio w/h',aspect_ratio)
        print('extent cnt_area/rect_area/',extent)
        print('solidity cnt_area/hull_area',solidity)
        print('equivalent diameter',equi_diameter)
        print('orientation',angle)
        print('min_val',min_val)
        print('max_val',max_val)
        print('min_loc',min_loc)
        print('max_loc',max_loc)
        print('mean_value',mean_val)
        print('leftmost',leftmost)
        print('rightmost',rightmost)
        print('topmost',topmost)
        print('bottommost',bottommost)
cv2.destroyAllWindows()
if a==1:
    cap.release()











    
