import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    median = cv2.medianBlur(frame,5)
    lur = cv2.GaussianBlur(median,(5,5),0)
    bi_filter = cv2.bilateralFilter(lur, 11, 17, 17)
    ret, thresh1 = cv2.threshold(bi_filter, 80, 255, cv2.THRESH_BINARY)

    # Display the resulting frame
    cv2.imshow('frame',cv2.rotate(frame,cv2.ROTATE_180))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()