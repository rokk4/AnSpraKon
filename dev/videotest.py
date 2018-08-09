import cv2
import numpy as np

cap = cv2.VideoCapture(0`)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray.copy(), 140, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    im_floodfill = thresh1.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = thresh1.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)

    cv2.imshow("digit 1 2", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
