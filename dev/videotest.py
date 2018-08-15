import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def print_mouse_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("[" + str(x) + ", " + str(y) + "]")

    if event == cv2.EVENT_RBUTTONDBLCLK:
        r = cv2.selectROI(thresh1)
        print("[" + str(r[1]) + ":" + str(r[1] + r[3]) + ", " + str(r[0]) + ":" + str(r[0] + r[2]) + "]")


while True:
    cv2.namedWindow("1", cv2.WINDOW_GUI_EXPANDED)

    cv2.setMouseCallback("1", print_mouse_coords)

    # Capture frame-by-frame
    ret, frame = cap.read()
    flipped = cv2.rotate(frame, cv2.ROTATE_180)
    gray = cv2.cvtColor(flipped[24:175, 198:425].copy(), cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.ADAPTIVE_THRESH_MEAN_C)

    digit_1_2 = thresh1[2:151, 5:171].copy()
    digit_decimal = thresh1[80:151, 182:227].copy()
    cv2.imshow("1", thresh1)
    cv2.imshow("digits", digit_1_2)
    cv2.imshow("decimal", digit_decimal)

    cv2.waitKey(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
