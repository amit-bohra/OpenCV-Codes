import cv2
import numpy as np






green    =  (0,255,0,20)
aqua     =  (0, 255, 255)
black    =  (0, 0, 0)
blue     =  (255, 0, 0)
fuchsia  =  (255, 0, 255)
gray     =  (128, 128, 128)
lgray    =  (150,150,150,150)
greeny   =  (0, 128, 0)
lime     =  (0, 255, 0)
maroon   =  (128, 0, 0)
navyblue =  (0, 0, 128)
olive    =  (128, 128, 0)
purple   =  (128, 0, 128)
silver   =  (192, 192, 192)
teal     =  (0, 128, 128)
yellow   =  (255, 255, 0)
colors   =  [green,aqua,blue,fuchsia,greeny,
             lime,maroon,navyblue,olive,purple,silver,teal,yellow]

color=colors[0]



flag1=0
flag2=0
flag3=0
flag4=0
flag5=0
flag6=1
flag7=0
flag8=1
flag9=0
flag10=0
flag11=0
flag12=0
flag13=0
drawflag=0
ix=0
iy=0
radius=0
listy=[]
drawpoly=0
thick=2
fillflag=2
color_ind=0

def draw(event,x,y,flags,param):
    global flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9,flag10,flag11,flag12,flag13,colors,color,color_ind,drawflag,ix,iy,fillflag,radius,thick,listy,drawpoly,img
    if x in range(510,690) and y in range(10,490):
        if event==cv2.EVENT_LBUTTONDOWN:
            if x in range(510,591) and y in range(10,51):
                flag1=1
                flag2=0
                flag3=0
                flag4=0
                flag11=0
            if x in range(600,681) and y in range(10,51):
                flag1=0
                flag2=1
                flag3=0
                flag4=0
                flag11=0
            if x in range(510,591) and y in range(60,101):
                flag1=0
                flag2=0
                flag3=1
                flag4=0
                flag11=0
            if x in range(600,681) and y in range(60,101):
                flag1=0
                flag2=0
                flag3=0
                flag4=1
                flag11=0
            if x in range(510,591) and y in range(110,151):
                flag5=1
                flag6=0
                fillflag=2
            if x in range(600,681) and y in range(110,151):
                flag6=1
                flag5=0
                fillflag=-1
            if x in range(510,591) and y in range(160,201):
                flag7=1
                flag8=0
            if x in range(600,681) and y in range(160,201):
                flag8=1
                flag7=0
            if x in range(510,591) and y in range(210,251):
                flag9=1
                flag10=0
                thick+=1
            if x in range(600,681) and y in range(210,251):
                flag10=1
                flag9=0
                thick-=1
                if thick<0:
                    thick=0
            if x in range(510,681) and y in range(260,301):
                flag11=1
                flag1=0
                flag2=0
                flag3=0
                flag4=0
            if x in range(510,591) and y in range(310,351):
                flag12=1
                flag13=0
            if x in range(600,681) and y in range(310,351):
                flag13=1
                flag12=0
    if x in range(10,490) and y in range(10,490):
        if event==cv2.EVENT_RBUTTONDOWN:
            if flag4==1:
                listy.append([x,y])
                if len(listy)>=2:
                    drawpoly=1
        if event==cv2.EVENT_LBUTTONDOWN:
            if flag1==1:
                ix=x
                iy=y
                drawflag=1
                if flag7==1:
                    flag8=0
                    cv2.rectangle(img,(x,y),(x+(5*thick)+40,y+thick+40),color,fillflag)
            if flag2==1:
                ix=x
                iy=y
                drawflag=1
                if flag7==1:
                    flag8=0
                    cv2.circle(img,(x,y),(5*thick)+20,color,fillflag)
            if flag3==1:
                ix=x
                iy=y
                drawflag=1
            if drawpoly==1:
                pts=np.array(listy,np.int32)
                cv2.polylines(img,[pts],True,color,thick)
                listy.clear()
            if flag11==1:
                ix=x
                iy=y
                drawflag=1
            if flag12==1:
                flag12=0
                color_ind+=1
                if color_ind>=len(colors):
                    color_ind=0
                color=colors[color_ind]
            if flag13==1:
                flag13=0
                color_ind-=1
                if color_ind<0:
                    color_ind=0
                color=colors[color_ind]
        if event==cv2.EVENT_MOUSEMOVE:
            if flag1==1 and drawflag==1 and flag8==1:
                cv2.rectangle(img,(ix,iy),(x,y),color,2)
            if flag2==1 and drawflag==1 and flag8==1:
                if x>=ix and y>=iy:
                    radius+=1
                else:
                    radius-=1
                if radius<0:
                    radius=0
                cv2.circle(img,(ix,iy),radius,color,-1)
            if flag3==1 and drawflag==1:
                cv2.circle(img,(x,y),thick,color,-1)
            if flag11==1 and drawflag==1:
                cv2.circle(img,(x,y),thick+20,(255,255,255),-1)
        if event==cv2.EVENT_LBUTTONUP:
            drawflag=0
            radius=0

img=np.zeros((500,700,3),np.uint8)
img[::]=[255,255,255]
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)

while True:
    cv2.rectangle(img,(500,0),(700,500),(255,255,255),-1)    
    pts=np.array([[5,5],[5,495],[495,495],[495,5]],np.int32)
    cv2.polylines(img,[pts],True,(0,0,255),10)
    cv2.rectangle(img,(510,10),(590,50),(255,0,0),-1)
    cv2.rectangle(img,(600,10),(680,50),(255,0,0),-1)
    cv2.rectangle(img,(510,60),(590,100),(255,0,0),-1)
    cv2.rectangle(img,(600,60),(680,100),(255,0,0),-1)
    cv2.rectangle(img,(510,110),(590,150),(255,0,0),-1)
    cv2.rectangle(img,(600,110),(680,150),(255,0,0),-1)
    cv2.rectangle(img,(510,160),(590,200),(255,0,0),-1)
    cv2.rectangle(img,(600,160),(680,200),(255,0,0),-1)
    cv2.rectangle(img,(510,210),(590,250),(255,0,0),-1)
    cv2.rectangle(img,(600,210),(680,250),(255,0,0),-1)
    cv2.rectangle(img,(510,260),(680,300),(255,0,0),-1)
    cv2.rectangle(img,(510,310),(590,350),(255,0,0),-1)
    cv2.rectangle(img,(600,310),(680,350),(255,0,0),-1)
    

    cv2.putText(img,'SQUARE',(515,40),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'CIRCLE',(605,40),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'LINE',(515,90),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'POLY',(605,90),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'HOLLOW',(515,140),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'FILLED',(605,140),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'FIXED',(515,190),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'RANDOM',(603,190),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'SIZE +',(515,240),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'SIZE -',(603,240),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'ERASE',(545,290),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'COLOR >',(515,340),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'COLOR <',(603,340),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
    img2=img.copy()
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()




