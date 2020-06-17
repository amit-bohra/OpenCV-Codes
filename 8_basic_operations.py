import cv2
import numpy as np

img=cv2.imread('a.jpg')
ball=img[100:,100:,:]
img[0:412,0:412,:]=ball
cv2.imshow('img',img)

b,g,r=cv2.split(img)
b=0
img=cv2.merge((b,g,r))
cv2.waitKey(0)
