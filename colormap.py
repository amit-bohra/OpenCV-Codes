import cv2
import matplotlib.pyplot as plt


img=cv2.imread('lena_color_512.tif',0)
tmg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img,cmap='')
plt.show()
