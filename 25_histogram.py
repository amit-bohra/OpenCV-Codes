import cv2
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    pass
a=0
a=int(input('Enter 1 for VideoCam else 0 '))
if a==1:
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,img=cap.read()
    else:
        ret=False
else:
    img=cv2.imread('a.jpg')
while True:
    if a==1:
        ret,img=cap.read()
    else:
        img=cv2.imread('a.jpg')
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    nphist,bins=np.histogram(img[:,:,0].ravel(),256,[0,256])
    nphistgray,bins=np.histogram(img1.ravel(),256,[0,256])
    plt.plot(nphist,'red')
    plt.plot(nphistgray,'gray')

    bincounthist=np.bincount(img.ravel(),minlength=256)
    bincounthistgray=np.bincount(img1.ravel(),minlength=256)
    plt.plot(bincounthist,'red')
    plt.plot(bincounthistgray,'gray')

    
##    histgray=cv2.calcHist([img1],[0],None,[256],[0,256])
##    histb=cv2.calcHist([img],[0],None,[256],[0,256])
##    histg=cv2.calcHist([img],[1], None,[256],[0,256])
##    histr=cv2.calcHist([img],[2],None,[256],[0,256])
##    plt.hist(histgray,bins=256)
##    plt.plot(histgray,'gray')
##    plt.plot(histb,'blue')
##    plt.plot(histg,'green')
##    plt.plot(histr,'red')
    plt.xlim([0,256])
    plt.show()
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print()
cv2.destroyAllWindows()
if a==1:
    cap.release()
