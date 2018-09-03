import numpy as np
import cv2


def print_mouse_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("[" + str(x) + ", " + str(y) + "]")

    if event == cv2.EVENT_RBUTTONDBLCLK:
        r = cv2.selectROI(thresh1)
        print("[" + str(r[1]) + ":" + str(r[1] + r[3]) + ", " + str(r[0]) + ":" + str(r[0] + r[2]) + "]")


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('lighting.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    cv2.namedWindow("1", cv2.WINDOW_GUI_EXPANDED)
    cv2.setMouseCallback("1", print_mouse_coords)
    ret, frame = cap.read()
    if ret:
        flipped = cv2.rotate(frame, cv2.ROTATE_180)
        gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)
        cropped = gray[2:480, 161:470].copy()



        height, width = cropped.shape
        pts1 = np.float32([[7, 8], [312, 11], [13, 467], [311, 463]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        m = cv2.getPerspectiveTransform(pts1, pts2)
        warped = cv2.warpPerspective(cropped, m, (width, height))



        out.write(frame)



        cv2.imshow('1', frame)
        cv2.imshow('warped', warped)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
