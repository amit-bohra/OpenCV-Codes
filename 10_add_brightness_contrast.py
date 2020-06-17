import cv2
import numpy as np
from copy import deepcopy as dp
import time

img=cv2.imread('a.jpg')
tmg=dp(img)

cmg=cv2.add(img,tmg)
#dmg=(img+tmg)

new_image=dp(img)
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            new_image[y,x,c] = np.clip(2.0*img[y,x,c] + 100, 0, 255)


while True:
    time.sleep(1)
    cv2.imshow('img',new_image)
    cv2.imshow('cmg',cmg)
    #cv2.imshow('dmg',dmg)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
