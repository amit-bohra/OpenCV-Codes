import cv2
import numpy as np
cap=cv2.VideoCapture(0)
ret,frame1=cap.read()
frame1=cv2.flip(frame1,1)
prvsImg=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv_mask=np.zeros_like(frame1)
hsv_mask[:,:,1]=255

while True:
    ret,frame2=cap.read()
    frame2=cv2.flip(frame2,1)
    nextImg=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    flow=cv2.calcOpticalFlowFarneback(prvsImg,nextImg,None,0.5,3,15,3,5,1.2,0)
    mag,angle=cv2.cartToPolar(flow[:,:,0],flow[:,:,1],angleInDegrees=True)
    hsv_mask[:,:,0]=angle/2
    hsv_mask[:,:,2]=cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    bgr=cv2.cvtColor(hsv_mask,cv2.COLOR_HSV2BGR)
    cv2.imshow('image',bgr)
    if cv2.waitKey(1)==27:
        break
    prvsImg=nextImg
cv2.destroyAllWindows()
cap.release()

    
