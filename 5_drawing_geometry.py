import cv2
import numpy as np







x=0
while True:
    img=np.zeros((512,512,3),np.uint8)
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
    cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
    cv2.circle(img,(447,63),63,(0,0,255),-1)
    output=cv2.ellipse(img,(255,255),(100,50),x,0,360,(255,255,255),-1)
    pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
    #pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(0,255,255),5)
    cv2.putText(img,'Ballu',(x,x),cv2.FONT_HERSHEY_SIMPLEX,x//50,(255,255,255),10,cv2.LINE_AA)
    cv2.imshow('img',output)
    if cv2.waitKey(1)==27:
        break
    x+=1
    if x==361:
        x=0
cv2.destroyAllWindows()

