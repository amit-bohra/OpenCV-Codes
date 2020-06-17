import cv2
#cv2.namedWindow('lena',cv2.WINDOW_AUTOSIZE)
img=cv2.imread('D:\Programming\OpenCV\standard_test_images\lena_color_512.tif',-1)
img2=cv2.imread('D:\Programming\OpenCV\standard_test_images\lena_color_512.tif',1)
print(img)
print('aaa')
#tmg=img[:,:,::-1]
#print(tmg)
print('bbb')
print(img[:,1,:])
print('ccc')
print(img[1,1:3,1])

#cv2.imshow('dena',img2)

#cv2.imshow('lena',tmg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.destroyWindow('lena')
#cv2.imwrite('D:\Programming\OpenCV\standard_test_images\lena_color_updated.png',img)
