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
# import numpy as np

if __name__ == '__main__':
    # Read image
    im = cv2.imread("radio_alarm_test_sleep_dot.png")

    # Select ROI
    # noinspection PyArgumentList
    r = cv2.selectROI(im)

    # Crop image
    imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    print(r)
    print("[" + str(r[1]) + ":" + str(r[1] + r[3]) + ", " + str(r[0]) + ":" + str(r[0] + r[2]) + "]")

    # Display cropped image
    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)

    #
    # beurerscale 145:448 23:620
