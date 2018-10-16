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
        r = cv2.selectROI(img[1])
        print("[" + str(r[1]) + ":" + str(r[1] + r[3]) + ", " + str(r[0]) + ":" + str(r[0] + r[2]) + "]")


while True:
    cv2.namedWindow("1", cv2.WINDOW_GUI_EXPANDED)

    cv2.setMouseCallback("1", print_mouse_coords)

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # frame = cv2.imread("/home/r0x/Development/ansprakon-v2/test_images/medisana_bloodsugar_test.png")
        gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)

        height, width = gray.shape
        pts1 = np.float32([[258, 45], [618, 47], [237, 197], [606, 206]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        m = cv2.getPerspectiveTransform(pts1, pts2)
        warped = cv2.warpPerspective(gray, m, (width, height))
        ret, thresh1 = cv2.threshold(warped, 55, 255, cv2.ADAPTIVE_THRESH_MEAN_C)

        #
        cv2.imshow("2", warped)
        cv2.imshow("2", thresh1)
        cv2.imshow("1", frame)


        cv2.waitKey(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
