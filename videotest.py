import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    flip_180 = cv2.rotate(frame.copy(), cv2.ROTATE_180)
    gray = cv2.cvtColor(flip_180[124:447, 49:495].copy(), cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    blur2 = cv2.medianBlur(gray, 5)
    bi_filter = cv2.bilateralFilter(gray, 11, 17, 17)
    ret, thresh1 = cv2.threshold(bi_filter.copy(), 90, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
    blur3 =  cv2.medianBlur(thresh1, 5)
    im_floodfill = thresh1.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = thresh1.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)

    kernel = np.ones((1,2),np.uint8)
    closing = cv2.morphologyEx(im_floodfill, cv2.MORPH_ERODE, kernel)
    closing2 = cv2.morphologyEx(closing, cv2.MORPH_CLOSE, kernel)






    cv2.imshow("closing", closing2)
    #cv2.imshow("flood", im_floodfill)
    # Display the resulting frame
    #cv2.imshow('frame',thresh1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()