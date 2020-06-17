import cv2
import numpy as np
import matplotlib.pyplot as plt


cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
while ret:
    ret,frame=cap.read()
    k=np.array(([0,-1,0],[-1,5,-1],[0,-1,0]),np.float32)
    output=cv2.filter2D(frame,-1,k)
    t=np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),np.float32)
    output=cv2.filter2D(output,-1,t)
    output=np.hstack((output,frame))
    cv2.imshow('output_kernel',output)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
