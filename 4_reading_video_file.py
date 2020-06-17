import cv2
import time

cap=cv2.VideoCapture('output_xvid.mp4')
ret,frame=cap.read()
while ret:
    time.sleep(0.01)
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
