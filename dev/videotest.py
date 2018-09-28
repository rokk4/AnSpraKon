# coding=utf-8
# This file is part of AnSpraKon.
#
# AnSpraKon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AnSpraKon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AnSpraKon.  If not, see <http://www.gnu.org/licenses/>.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)


# [21:176, 91:337]
# [159:315, 101:321]

def print_mouse_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("[" + str(x) + ", " + str(y) + "]")

    if event == cv2.EVENT_RBUTTONDBLCLK:
        r = cv2.selectROI(bordered)
        print("[" + str(r[1]) + ":" + str(r[1] + r[3]) + ", " + str(r[0]) + ":" + str(r[0] + r[2]) + "]")


while True:
    cv2.namedWindow("1", cv2.WINDOW_GUI_EXPANDED)

    cv2.setMouseCallback("1", print_mouse_coords)

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # frame = cv2.imread("/home/r0x/Development/ansprakon-v2/test_images/medisana_bloodsugar_test.png")
        flipped = cv2.rotate(frame.copy(), cv2.ROTATE_90_CLOCKWISE)
        gray = cv2.cvtColor(flipped.copy(), cv2.COLOR_BGR2GRAY)

        ret, thresh1 = cv2.threshold(gray[213:564, 59:389], 127, 255, cv2.ADAPTIVE_THRESH_MEAN_C)

        blur = cv2.GaussianBlur(thresh1, (3, 3), 0)

        height, width = thresh1.shape
        pts1 = np.float32([[18, 20], [303, 15], [25, 326], [307, 320]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        m = cv2.getPerspectiveTransform(pts1, pts2)
        warped = cv2.warpPerspective(thresh1, m, (width, height))

        border_size = 10
        bordered = cv2.copyMakeBorder(warped,
                                      top=border_size,
                                      bottom=border_size,
                                      left=border_size,
                                      right=border_size,
                                      borderType=cv2.BORDER_CONSTANT,
                                      value=[255, 255, 255])

        systolic_digits = bordered[22:162, 40:327].copy()
        diastolic_digits = bordered[162:304, 100:314].copy()
        heartrate = bordered[307:354, 225:311].copy()

        kernel_1 = np.ones((5, 5), np.uint8)
        systolic_digits_dil = cv2.dilate(systolic_digits, kernel_1, iterations=1)
        diastolic_digits_dil = cv2.dilate(diastolic_digits, kernel_1, iterations=1)

        kernel_2 = np.ones((3, 3), np.uint8)
        heartrate_dil = cv2.dilate(heartrate, kernel_2, iterations=1)

        systolic_digits_dil_bordered = cv2.copyMakeBorder(systolic_digits_dil,
                                                          top=border_size,
                                                          bottom=border_size,
                                                          left=border_size,
                                                          right=border_size,
                                                          borderType=cv2.BORDER_CONSTANT,
                                                          value=[255, 255, 255])

        diastolic_digits_dil_bordered = cv2.copyMakeBorder(diastolic_digits_dil,
                                                           top=border_size,
                                                           bottom=border_size,
                                                           left=border_size,
                                                           right=border_size,
                                                           borderType=cv2.BORDER_CONSTANT,
                                                           value=[255, 255, 255])

        heartrate_dil_bordered = cv2.copyMakeBorder(heartrate_dil,
                                                    top=border_size,
                                                    bottom=border_size,
                                                    left=border_size,
                                                    right=border_size,
                                                    borderType=cv2.BORDER_CONSTANT,
                                                    value=[255, 255, 255])

        cv2.imshow("1", bordered)
        cv2.imshow("2", systolic_digits_dil_bordered)
        cv2.imshow("3", diastolic_digits_dil_bordered)
        cv2.imshow("4", heartrate_dil_bordered)

        cv2.waitKey(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
