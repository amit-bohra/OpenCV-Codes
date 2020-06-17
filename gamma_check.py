import cv2
import numpy as np
import pandas as pd


while True:
    frame = cv2.imread('a.jpg')
    x = float(input())
    invGamma = 1.0 / x
    table = [((i/255.0)**invGamma)*255 for i in range(0,256)]
    table = np.array(table)
    table = np.uint8(table)
    frame = cv2.LUT(frame, table)
    cv2.imshow('one',frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
