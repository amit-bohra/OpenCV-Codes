import cv2
import numpy as np



e1=cv2.getTickCount()

img=cv2.imread('a.jpg')
cv2.imshow('one',img)
cv2.waitKey(0)

e2=cv2.getTickCount()
time=(e2-e1)/cv2.getTickFrequency()

print(time)
print(cv2.useOptimized())
