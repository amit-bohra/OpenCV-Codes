import cv2
import numpy

cap=cv2.VideoCapture(0)
width=cap.get(3)
height=cap.get(4)
#cap.set(3,320)
#cap.set(4,240)

fourcc=cv2.VideoWriter_fourcc(*'WMV2')
wmv2=cv2.VideoWriter('output_wmv2.avi',fourcc,60,(int(cap.get(3)),int(cap.get(4))))
fourcc=cv2.VideoWriter_fourcc(*'WMV1')
wmv1=cv2.VideoWriter('output_wmv1.avi',fourcc,60,(int(cap.get(3)),int(cap.get(4))))
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
mjpg=cv2.VideoWriter('output_mjpg.avi',fourcc,60,(int(cap.get(3)),int(cap.get(4))))
fourcc=cv2.VideoWriter_fourcc(*'DIVX')
divx=cv2.VideoWriter('output_divx.avi',fourcc,60,(int(cap.get(3)),int(cap.get(4))))
fourcc=cv2.VideoWriter_fourcc(*'XVID')
xvid=cv2.VideoWriter('output_xvid.avi',fourcc,60,(int(cap.get(3)),int(cap.get(4))))
fourcc=cv2.VideoWriter_fourcc(*'MP4V')
mp4v=cv2.VideoWriter('output_mp4v.avi',fourcc,60,(int(cap.get(3)),int(cap.get(4))))

if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
while ret:
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    wmv2.write(frame)
    wmv1.write(frame)
    mjpg.write(frame)
    divx.write(frame)
    xvid.write(frame)
    mp4v.write(frame)
    if cv2.waitKey(1)==27:
        break

cap.release()
wmv2.release()
wmv1.release()
mjpg.release()
divx.release()
xvid.release()
mp4v.release()
cv2.destroyAllWindows()    
