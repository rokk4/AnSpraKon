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
        r = cv2.selectROI(warped)
        print("[" + str(r[1]) + ":" + str(r[1] + r[3]) + ", " + str(r[0]) + ":" + str(r[0] + r[2]) + "]")


while True:
    cv2.namedWindow("1", cv2.WINDOW_GUI_EXPANDED)

    cv2.setMouseCallback("1", print_mouse_coords)

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # frame = cv2.imread("/home/r0x/Development/ansprakon-v2/test_images/medisana_bloodsugar_test.png")
        flipped = cv2.rotate(frame, cv2.ROTATE_180)
        gray = cv2.cvtColor(flipped[182:385, 0:639].copy(), cv2.COLOR_BGR2GRAY)

        ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
        height, width = thresh1.shape
        pts1 = np.float32([[65, 13], [630, 15], [35, 169], [603, 186]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        m = cv2.getPerspectiveTransform(pts1, pts2)
        warped = cv2.warpPerspective(thresh1, m, (width, height))

        double_dot_upper = warped[45:72, 315:344].copy()
        double_dot_lower = warped[133:164, 317:348].copy()

        digits_1_2 = warped[0:200, 0:306].copy()
        digits_3_4 = warped[0:202, 354:639].copy()


        #
        # kernel_1 = np.ones((3, 3), np.uint8)
        # warped_dilated = cv2.dilate(warped, kernel_1, iterations=3)
        #
        # digits_1_2 = warped_dilated[0:154, 0:238].copy()
        # digits_3_4 = warped_dilated[1:160, 311:595].copy()
        #
        # left_points = thresh1[14:160, 13:74].copy()
        # right_points = thresh1[20:160, 530:595].copy()
        #
        # left_points_dilated = cv2.dilate(left_points, kernel_1, iterations=2)
        #
        # left_point_1 = None
        # left_point_2 = left_points_dilated[62:78, 8:33].copy()
        # left_point_3 = left_points_dilated[97:124, 8:33].copy()
        #
        # right_points_dilted = cv2.dilate(right_points, kernel_1, iterations=2)
        #
        # right_point_1 = right_points_dilted[20:38, 13:36].copy()
        # right_point_2 = right_points_dilted[56:74, 21:41].copy()
        # right_point_3 = right_points_dilted[95:112, 25:49].copy()
        #
        # double_dot_lower = thresh1[99:126, 275:307].copy()
        # double_dot_upper = thresh1[40:65, 284:309].copy()
        #
        # border_size = 10
        # bordered = cv2.copyMakeBorder(warped_dilated,
        #                               top=border_size,
        #                               bottom=border_size,
        #                               left=border_size,
        #                               right=border_size,
        #                               borderType=cv2.BORDER_CONSTANT,
        #                               value=[255, 255, 255])
        #
        # systolic_digits = bordered[22:162, 40:327].copy()
        # diastolic_digits = bordered[162:304, 100:314].copy()
        # heartrate = bordered[307:354, 225:311].copy()
        #
        # kernel_1 = np.ones((5, 5), np.uint8)
        # systolic_digits_dil = cv2.dilate(systolic_digits, kernel_1, iterations=1)
        # diastolic_digits_dil = cv2.dilate(diastolic_digits, kernel_1, iterations=1)
        #
        # kernel_2 = np.ones((3, 3), np.uint8)
        # heartrate_dil = cv2.dilate(heartrate, kernel_2, iterations=1)
        #
        # systolic_digits_dil_bordered = cv2.copyMakeBorder(systolic_digits_dil,
        #                                                   top=border_size,
        #                                                   bottom=border_size,
        #                                                   left=border_size,
        #                                                   right=border_size,
        #                                                   borderType=cv2.BORDER_CONSTANT,
        #                                                   value=[255, 255, 255])
        #
        # diastolic_digits_dil_bordered = cv2.copyMakeBorder(diastolic_digits_dil,
        #                                                    top=border_size,
        #                                                    bottom=border_size,
        #                                                    left=border_size,
        #                                                    right=border_size,
        #                                                    borderType=cv2.BORDER_CONSTANT,
        #                                                    value=[255, 255, 255])
        #
        # heartrate_dil_bordered = cv2.copyMakeBorder(heartrate_dil,
        #                                             top=border_size,
        #                                             bottom=border_size,
        #                                             left=border_size,
        #                                             right=border_size,
        #                                             borderType=cv2.BORDER_CONSTANT,
        #                                             value=[255, 255, 255])

        # feat_detect_rois = [double_dot_lower, double_dot_upper,
        #                     left_point_2, left_point_3,
        #                     right_point_1, right_point_2, right_point_3]

        #cv2.imshow("1", double_dot_lower)
        #cv2.imshow("2", double_dot_upper)
        # cv2.imshow("1", warped_dilated)
        cv2.imshow("1", warped)
        #cv2.imshow("5", double_dot_upper)

        cv2.waitKey(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
