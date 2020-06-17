import cv2
import numpy as np
import sys

A=cv2.imread("lena_color_512.tif")
B=cv2.imread("woman_darkhair.tif")

G=A.copy()
gpA=[G]
for i in range(6):
    G=cv2.pyrDown(G)
    gpA.append(G)

G=B.copy()
gpB=[G]
for i in range(6):
    G=cv2.pyrDown(G)
    gpB.append(G)

lpA=[gpA[6]]
for i in range(-1,-7,-1):
    G=cv2.pyrUp(gpA[i])
    L=cv2.subtract(gpA[i-1],G)
    lpA.append(L)

lpB=[gpB[6]]
for i in range(-1,-7,-1):
    G=cv2.pyrUp(gpB[i])
    L=cv2.subtract(gpB[i-1],G)
    lpB.append(L)

LS=[]
for la,lb in zip(lpA,lpB):
   rows,cols,dpt = la.shape
   ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
   LS.append(ls)

ls_ = LS[0]
for i in range(1,7):
   ls_ = cv2.pyrUp(ls_)
   ls_ = cv2.add(ls_, LS[i])

r,cols,l=A.shape
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))

cv2.imshow('fale',ls_)
cv2.imshow('real',real)
cv2.waitKey(0)
