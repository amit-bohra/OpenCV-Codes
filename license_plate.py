import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('plate.jpg')
image=img.copy()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh=cv2.GaussianBlur(gray,(17,17),0)

#ret,thresh=cv2.threshold(blur,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

median=np.median(thresh)
low=int(max(0,0.7*median))
high=int(max(0,1.3*median))
canny_edge=cv2.Canny(thresh,low,high+30,L2gradient=False)

k=cv2.getStructuringElement(cv2.MORPH_RECT,(13,13))
dilate=cv2.dilate(canny_edge,k,iterations=1)
erode=cv2.erode(dilate,k,iterations=1)


contours,hierarchy =cv2.findContours(canny_edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(hierarchy)
for i in range(len(contours)):
    if hierarchy[0][i][3]!=-1:
        cnt=contours[i]
        x,y,w,h=cv2.boundingRect(cnt)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)


cv2.imshow('g',image)
cv2.waitKey(0)
