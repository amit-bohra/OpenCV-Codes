import cv2
import numpy

img1=cv2.imread('a.jpg')
img2=cv2.imread('b.tif')

cv2.namedWindow('one')

def func(one):
    global x,y,z
    x=one/100
    y=1-x

x=0
y=1
z=0
cv2.createTrackbar('kuch_bhi_naam','one',0,100,func)
while True:
    img=cv2.addWeighted(img1,x,img2,y,z)
    cv2.imshow('one',img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
