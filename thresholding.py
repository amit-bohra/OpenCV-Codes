import numpy as np
import cv2
import matplotlib.pyplot as plt
from copy import deepcopy as dp


cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read() 
else:
    ret=False

while ret:
    ret,frame=cap.read()
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    block=11
    constant=2
    #ret,frame1=cv2.threshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,block,constant)
    #ret,frame2=cv2.threshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,block,constant)
    
    
    ret,o1=cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
    #ret,o2=cv2.threshold(frame,127,255,cv2.THRESH_BINARY_INV)
    #ret,o3=cv2.threshold(frame,127,255,cv2.THRESH_TOZERO)
    #ret,o4=cv2.threshold(frame,127,255,cv2.THRESH_TOZERO_INV)
    #ret,o5=cv2.threshold(frame,127,255,cv2.THRESH_TRUNC)
    #ret,o6=cv2.threshold(frame,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #ret,o7=cv2.threshold(frame,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #ret,o8=cv2.threshold(frame,0,255,cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    #ret,o9=cv2.threshold(frame,0,255,cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
    #ret,o0=cv2.threshold(frame,0,255,cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
    
    #output=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #toutput=dp(output)
    #toutput[toutput>=127]=255
    #toutput[toutput<=127]=0
    #output[output>=127]=128
    #output[output<127]=255
    #output[output==128]=0
    #cv2.imshow('gray_original_threshold',toutput)

    cv2.imshow('binary',o1)
    #cv2.imshow('binary_inv',o2)
    #cv2.imshow('zero',o3)
    #cv2.imshow('zero_inv',o4)
    #cv2.imshow('trunc',o5)
    #cv2.imshow('otsu_binary',o6)
    #cv2.imshow('otsu_bin_inv',o7)
    #cv2.imshow('otsu_zero',o8)
    #cv2.imshow('otsu_zero_inv',o9)
    #cv2.imshow('otsu_trunc',o0)

    #cv2.imshow('mean',frame1)
    #cv2.imshow('gaussian',frame2)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
