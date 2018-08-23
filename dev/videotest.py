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

cap = cv2.VideoCapture(2)


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
    gray = cv2.cvtColor(flipped.copy(), cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, 70, 255, cv2.AGAST_FEATURE_DETECTOR_THRESHOLD)


    cv2.imshow("1", gray)


    cv2.waitKey(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
