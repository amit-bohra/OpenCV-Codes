import numpy as np
import cv2
import matplotlib.pyplot as plt

a=0
a=int(input('Enter 1 for VideoCam else 0 '))
if a==1:
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,img=cap.read()
    else:
        ret=False
else:
    img=cv2.imread('lena_color_512.tif',1)

cv2.namedWindow('color',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('gray_NORMAL_RESIZABLE',cv2.WINDOW_NORMAL)

while True:
    if a==1:
        ret,img=cap.read()
        img=cv2.flip(img,1)
    else:
        img=cv2.imread('lena_color_512.tif',1)
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    cv2.imshow('color',img)
    cv2.imshow('gray_NORMAL_RESIZABLE',imggray)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        cv2.imwrite('color.png',img)
        cv2.imwrite('gray.png',imggray)
        print('image saved')
cv2.destroyAllWindows()
if a==1:
    cap.release()
