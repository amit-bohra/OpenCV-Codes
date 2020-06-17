import cv2

def func(a):
    print(a)
    global img
    img+=a

cv2.namedWindow('image')
img=cv2.imread('lena_color_512.jpg',1)
cv2.createTrackbar('name','image',1,255,func)
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
