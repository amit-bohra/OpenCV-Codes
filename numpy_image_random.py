import numpy as np
import cv2

tarr=np.array((),np.uint8)
for i in range(12000):
    arr=np.random.randint(0,100,50)
    tarr=np.append(tarr,arr,0)

tarr=tarr.reshape((400,500,3))
tarr=np.uint8(tarr)

cv2.imshow('original',tarr)
cv2.waitKey(0)
