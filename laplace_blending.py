import cv2
import numpy as np
import sys

a=cv2.imread("woman_blonde.tif")
b=cv2.imread("woman_darkhair.tif")

A=[a]
B=[b]


tempa=a.copy()
tempb=b.copy()
for i in range(6):
    tempa=cv2.pyrDown(tempa)
    A.append(tempa)

for i in range(6):
    tempb=cv2.pyrDown(tempb)
    B.append(tempb)


lapa=[]
lapb=[]
for i in range(1,7):
    ta=cv2.pyrUp(A[i])
    ta=A[i-1]-ta
    lapa.append(ta)

for i in range(1,7):
    tb=cv2.pyrUp(B[i])
    tb=B[i-1]-tb
    lapb.append(tb)


Ls=[]
for i,j in zip(lapa,lapb):
    r,c,l=i.shape
    ls=np.hstack((i[:,0:c//2],j[:,c//2:]))
    Ls.append(ls)

Ls.reverse()


ls=Ls[0]
for i in range(1,6):
    ls=cv2.pyrUp(ls)
    ls=ls+Ls[i]
'''Ts=[]
for i,j in zip(A,B):
    r,c,l=i.shape
    ls=np.hstack((i[:,0:c//2],j[:,c//2:]))
    Ts.append(ls)


Ts.reverse()

for i in range(5):
    temp=cv2.pyrUp(Ls[i])
    temp=temp+Ts[i+2]'''

cv2.imshow("original",ls)
cv2.waitKey(0)
