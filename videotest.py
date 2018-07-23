import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    blur2 = cv2.medianBlur(blur, 5)
    bi_filter = cv2.bilateralFilter(blur2, 11, 17, 17)
    ret, thresh1 = cv2.threshold(bi_filter, 120, 255, cv2.THRESH_BINARY_INV)
    blur3 =  cv2.medianBlur(thresh1, 5)
    # Display the resulting frame
    cv2.imshow('frame',blur3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()