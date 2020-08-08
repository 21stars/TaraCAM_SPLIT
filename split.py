import numpy as np
import cv2

#camera open
cap = cv2.VideoCapture(0)
#configure Tara camera
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' '))
cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH , 752)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#create left & right frame image
lefty = np.zeros((480,752),np.uint8)
righty = np.zeros((480,752),np.uint8)

while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
    frame = frame.reshape((480,1504))

    #even columns = lefty, odd columns = righty
    lefty = np.array(frame)[:,0::2]
    righty = np.array(frame)[:,1::2]

    cv2.imshow("lefty", lefty)
    cv2.imshow("righty", righty)
    #press q to finish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#release camera and exit
cap.release()
cv2.destroyAllWindows()
exit(0)
