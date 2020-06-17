import cv2
classifier=cv2.CascadeClassifier('haarcascade_smile.xml')
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
while ret:
    ret,frame=cap.read()
    face_rect=classifier.detectMultiScale(frame,2.0,15)
    for x,y,w,h in face_rect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),3)
    cv2.imshow('img',frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
