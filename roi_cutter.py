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


def roi_device_0(img):
    """

    :param img:
    :return:
    """
    ocr_rois = [img]
    feat_detect_rois = []
    return [ocr_rois, feat_detect_rois]


def roi_device_1(img):
    """
BASETECH-Thermometer
    :param img:
    :return:
    """
    temperature = img
    ocr_rois = [temperature]
    return [ocr_rois, []]


def roi_device_2(img):
    """
ADE-Germany Human Scale
    :param img:
    :return:
    """
    weight = img
    ocr_rois = [weight]
    return [ocr_rois, []]


def roi_device_3(img):
    """
Beurer Human Scale
    :param img:
    :return:
    """
    weight = img
    ocr_rois = [weight]
    return [ocr_rois, []]


def roi_device_4(img):
    """
NONAME indoor/outdoor thermometer
    :param img:
    :return:
    """
    # ocr
    indoor_temp = img[32:245, 117:517].copy()
    outdoor_temp = img[260:480, 97:517].copy()

    # feat
    indoor_indicator = img[28:73, 522:570].copy()
    outdoor_indicator = img[258:301, 516:588].copy()
    max_indicator = img[28:72, 24:111].copy()
    min_indicator = img[256:303, 18:101].copy()

    # cv2.imshow("img", img)
    # cv2.imshow("indoor_temp", indoor_temp)
    # cv2.imshow("outdoor_temp", outdoor_temp)

    indoor_temp_pts1 = np.float32([[31, 5], [394, 6], [5, 205], [371, 208]])
    indoor_temp_pts2 = np.float32([[0, 0], [400, 0], [0, 212], [400, 212]])
    indoor_temp_m = cv2.getPerspectiveTransform(indoor_temp_pts1, indoor_temp_pts2)
    indoor_temp_dst = cv2.warpPerspective(indoor_temp, indoor_temp_m, (400, 212))

    outdoor_temp_pts1 = np.float32([[31, 5], [415, 6], [5, 205], [395, 208]])
    outdoor_temp_pts2 = np.float32([[0, 0], [420, 0], [0, 220], [420, 220]])
    outdoor_temp__m = cv2.getPerspectiveTransform(outdoor_temp_pts1, outdoor_temp_pts2)
    outdoor_temp_dst = cv2.warpPerspective(outdoor_temp, outdoor_temp__m, (420, 220))

    # cv2.imshow("indoor warp", indoor_temp_dst)
    # cv2.imshow("outdoor warp", outdoor_temp_dst)

    border_size = 10

    indoor_warped_bordered = cv2.copyMakeBorder(indoor_temp_dst, top=border_size, bottom=border_size, left=border_size,
                                                right=border_size,
                                                borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])
    # cv2.imshow("bordered warp indoor", indoor_warped_bordered)

    outdoor_warped_bordered = cv2.copyMakeBorder(outdoor_temp_dst, top=border_size, bottom=border_size,
                                                 left=border_size,
                                                 right=border_size,
                                                 borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])
    # cv2.imshow("bordered warp outdoor", outdoor_warped_bordered)


    kernel_2 = np.ones((3, 3), np.uint8)
    indoor_warped_bordered_dilated = cv2.dilate(indoor_warped_bordered, kernel_2, iterations=1)
    outdoor_warped_bordered_dilated = cv2.dilate(outdoor_warped_bordered, kernel_2, iterations=1)

    # cv2.imshow("bordered warp indoor dil", indoor_warped_bordered_dilated)
    # cv2.imshow("bordered warp outdoor dil", outdoor_warped_bordered_dilated)





    # cv2.waitKey(1)

    ocr_rois = [indoor_warped_bordered_dilated.copy(), outdoor_warped_bordered_dilated.copy()]
    feat_rois = [indoor_indicator, outdoor_indicator, min_indicator, max_indicator]

    return [ocr_rois, feat_rois]


def roi_device_5(img):
    """
GREEN alarm radio
    :param img:
    :return:
    """
    digits_1 = img[51:224, 35:310].copy()
    digits_2 = img[45:217, 321:574].copy()
    ocr_rois = [digits_1, digits_2]

    alarm_1 = img[195:222, 12:42].copy()
    alarm_2 = img[199:226, 587:612].copy()
    freq_shown = img[123:145, 582:606].copy()

    feat_rois = [alarm_1, alarm_2, freq_shown]
    # cv2.imshow("digits1", digits_1)
    # cv2.imshow("digits2", digits_2)
    # cv2.waitKey(60)
    return [ocr_rois, [feat_rois]]


def roi_device_6(img):
    """
NONAME thermo-hygro
    :param img:
    :return:
    """

    temp = img[3:155, 35:280].copy()
    temp_decimal = img[33:151, 281:377].copy()
    humidity = img[175:303, 111:312].copy()

    dry = img[276:305, 2:56].copy()
    wet = img[80:112, 374:440].copy()
    min_1 = img[89:121, 373:437].copy()
    min_2 = img[269:300, 337:396].copy()
    max_1 = img[114:143, 376:439].copy()
    max_2 = img[271:296, 394:446].copy()
    # cv2.imshow("uncut", img)
    # cv2.imshow("temp", temp)
    # cv2.imshow("temp_deci", temp_decimal)
    # cv2.imshow("humidity", humidity)
    # cv2.imshow("1",min_1)
    # cv2.imshow("2",max_1)
    # cv2.imshow("3",min_2)
    # cv2.imshow("4",max_2)
    # cv2.waitKey(1)
    border_size = 10
    temp_height, temp_width = temp.shape

    temp_pts1 = np.float32([[33, 8], [239, 6], [24, 141], [228, 140]])
    temp_pts2 = np.float32([[0, 0], [temp_width, 0], [0, temp_height], [temp_width, temp_height]])
    temp_m = cv2.getPerspectiveTransform(temp_pts1, temp_pts2)
    temp_dst = cv2.warpPerspective(temp, temp_m, (temp_width, temp_height))

    temp_bordered = cv2.copyMakeBorder(temp_dst, top=border_size, bottom=border_size, left=border_size,
                                       right=border_size,
                                       borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])

    temp_decimal_height, temp_decimal_width = temp_decimal.shape
    temp_decimal_pts1 = np.float32([[14, 7], [81, 5], [10, 110], [77, 106]])
    temp_decimal_pts2 = np.float32([[0, 0], [temp_decimal_width, 0],
                                    [0, temp_decimal_height], [temp_decimal_width, temp_decimal_height]])

    temp_decimal__m = cv2.getPerspectiveTransform(temp_decimal_pts1, temp_decimal_pts2)
    temp_decimal_dst = cv2.warpPerspective(temp_decimal, temp_decimal__m, (temp_decimal_width, temp_decimal_height))

    temp_decimal_bordered = cv2.copyMakeBorder(temp_decimal_dst, top=border_size, bottom=border_size,
                                               left=border_size,
                                               right=border_size,
                                               borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])
    # cv2.imshow("bordered warp temp_decimal", temp_decimal_bordered)

    humidity_height, humidity_width = humidity.shape

    humidity_pts1 = np.float32([[27, 6], [186, 8], [14, 116], [182, 117]])
    humidity_pts2 = np.float32([[0, 0], [humidity_width, 0], [0, humidity_height], [humidity_width, humidity_height]])
    humidity__m = cv2.getPerspectiveTransform(humidity_pts1, humidity_pts2)
    humidity_dst = cv2.warpPerspective(humidity, humidity__m, (humidity_width, humidity_height))

    humidity_bordered = cv2.copyMakeBorder(humidity_dst, top=border_size, bottom=border_size,
                                           left=border_size,
                                           right=border_size,
                                           borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])
    # cv2.imshow("bordered warp humidity", humidity_bordered)

    kernel_1 = np.ones((5, 5), np.uint8)
    temp_bordered_dilated = cv2.dilate(temp_bordered, kernel_1, iterations=2)
    humidity_bordered_dilated = cv2.dilate(humidity_bordered, kernel_1, iterations=2)


    # cv2.imshow("temp dilated", temp_bordered_dilated)
    # cv2.imshow("humidity dilated", humidity_bordered_dilated)
    #
    #
    #
    #
    #
    #
    # cv2.waitKey(1)

    ocr_rois = [temp_bordered_dilated, temp_decimal_bordered, humidity_bordered]
    feat_detect_rois = [dry, wet, min_1, max_1, min_2, max_2]
    return [ocr_rois, feat_detect_rois]


def roi_device_7(display):
    """
CASIO calculator MS-20UC
    :param img:
    :return:
    """
    # cv2.equalizeHist(display, display)
    border_size = 10
    white = [255, 255, 255]
    display_pts1 = np.float32([[36, 58], [569, 58], [31, 175], [558, 179]])
    display_pts2 = np.float32([[0, 0], [570, 0], [0, 180], [570, 180]])
    display__m = cv2.getPerspectiveTransform(display_pts1, display_pts2)
    display_dst = cv2.warpPerspective(display, display__m, (570, 180))

    display_bordered = cv2.copyMakeBorder(display_dst, top=border_size, bottom=border_size,
                                          left=border_size,
                                          right=border_size,
                                          borderType=cv2.BORDER_CONSTANT, value=white)
    # cv2.imshow("bordered warp display", display_bordered)
    # cv2.imshow("display", display)

    digits_10_13 = display_bordered[0:200, 0:149]
    digits_10_13_bordered = cv2.copyMakeBorder(digits_10_13, top=0, bottom=0, left=0, right=border_size,
                                               borderType=cv2.BORDER_CONSTANT, value=white)

    digits_7_9 = display_bordered[0:200, 155:297]
    digits_7_9_bordered = cv2.copyMakeBorder(digits_7_9, top=0, bottom=0, left=border_size, right=border_size,
                                             borderType=cv2.BORDER_CONSTANT, value=white)

    digits_3_6 = display_bordered[0:200, 302:443]
    digits_3_6_bordered = cv2.copyMakeBorder(digits_3_6, top=0, bottom=0, left=border_size, right=border_size,
                                             borderType=cv2.BORDER_CONSTANT, value=white)
    digits_1_3 = display_bordered[0:200, 445:590]
    digits_1_3_bordered = cv2.copyMakeBorder(digits_1_3, top=0, bottom=0, left=border_size, right=0,
                                             borderType=cv2.BORDER_CONSTANT, value=white)

    ret, digits_10_13_bordered = cv2.threshold(digits_10_13_bordered.copy(), 50, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    ret, digits_7_9_bordered = cv2.threshold(digits_7_9_bordered.copy(), 90, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
    ret, digits_3_6_bordered = cv2.threshold(digits_3_6_bordered.copy(), 90, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
    ret, digits_1_3_bordered = cv2.threshold(digits_1_3_bordered.copy(), 70, 255, cv2.THRESH_BINARY)
    im_floodfill = digits_1_3_bordered.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = digits_1_3_bordered.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)

    # cv2.imshow("1-3", digits_1_3_bordered)
    # cv2.imshow("4-6", digits_3_6_bordered)
    # cv2.imshow("7-9", digits_7_9_bordered)
    #
    # cv2.imshow("10-13", digits_10_13_bordered)
    #
    # cv2.imshow("eq", display)

    ocr_rois = [digits_1_3_bordered, digits_3_6_bordered, digits_7_9_bordered, digits_10_13_bordered]
    feat_detect_rois = []
    # cv2.waitKey(1)
    return [ocr_rois, feat_detect_rois]


def roi_device_8(img):
    """
IDR radio alarmclock
    :param imgs:
    :return:
    """

    kernel_1 = np.ones((3, 3), np.uint8)

    digits_1_2 = img[1][0:154, 0:238].copy()
    digits_3_4 = img[1][1:160, 311:595].copy()

    double_dot_lower = img[1][99:126, 275:307].copy()
    double_dot_upper = img[1][36:68, 284:317].copy()

    decimal_dot = img[1][127:158, 437:479].copy()

    left_points = img[0][14:160, 13:74].copy()
    left_points_dilated = cv2.dilate(left_points, kernel_1, iterations=2)
    # left_point_1 = None
    left_point_2 = left_points_dilated[62:78, 8:33].copy()
    left_point_3 = left_points_dilated[97:124, 8:33].copy()

    right_points = img[0][20:160, 530:595].copy()
    right_points_dilted = cv2.dilate(right_points, kernel_1, iterations=2)
    right_point_1 = right_points_dilted[20:38, 13:36].copy()
    right_point_2 = right_points_dilted[56:74, 21:41].copy()
    right_point_3 = right_points_dilted[95:112, 25:49].copy()

    ocr_rois = [digits_1_2, digits_3_4]
    feat_detect_rois = [double_dot_lower, double_dot_upper,
                        decimal_dot,
                        left_point_2, left_point_3,
                        right_point_1, right_point_2, right_point_3]

    cv2.imshow("1", digits_1_2)
    cv2.imshow("2", digits_3_4)
    # cv2.imshow("3", right_point_3)
    # cv2.imshow("4", double_dot_upper)
    # cv2.imshow("5", double_dot_lower)
    cv2.waitKey(1)

    return [ocr_rois, feat_detect_rois]


def roi_device_9(img):
    """

    :param img:
    :return:
    """

    digit_1_2 = img[2:192, 1:295].copy()
    digit_3_4 = img[7:198, 324:627].copy()
    double_dot_lower = img[125:146, 299:319].copy()
    double_dot_upper = img[46:75, 298:328].copy()

    ocr_rois = [digit_1_2, digit_3_4]
    feat_detect_rois = [double_dot_lower, double_dot_upper]
    return [ocr_rois, feat_detect_rois]


def roi_device_10(img):
    """
THERMO
    :param img:
    :return:
    """
    digit_1_2 = img[2:151, 5:171].copy()
    digit_decimal = img[80:151, 182:227].copy()

    kernel_1 = np.ones((4, 4), np.uint8)
    digit_1_2_dilated = cv2.dilate(digit_1_2, kernel_1, iterations=1)
    kernel_2 = np.ones((3, 3), np.uint8)
    digit_decimal_dilated = cv2.dilate(digit_decimal, kernel_2, iterations=3)
    # cv2.imshow("decimal", digit_decimal_dilated)
    # cv2.imshow("digits", digit_1_2_dilated)
    # cv2.waitKey(1)

    ocr_rois = [digit_1_2_dilated, digit_decimal]
    feat_detect_rois = []
    return [ocr_rois, feat_detect_rois]


def roi_device_11(img):
    """

    :param img:
    :return:
    """

    double_dot_upper = img[45:72, 315:344].copy()
    double_dot_lower = img[133:164, 317:348].copy()

    digits_1_2 = img[0:200, 0:306].copy()
    digits_3_4 = img[0:202, 354:639].copy()

    ocr_rois = [digits_1_2, digits_3_4]
    feat_detect_rois = [double_dot_upper, double_dot_lower]

    # cv2.imshow("all", img)
    # cv2.imshow("digits_1-2", digits_1_2)
    # cv2.imshow("digits_3-4", digits_3_4)
    # cv2.waitKey(1)

    return [ocr_rois, feat_detect_rois]


# Device ID 12
def roi_device_12(img):
    """
Bloodpressure
    :param img: the image to process
    :return: the processed img
    """
    systolic_digits = img[22:162, 40:327].copy()
    diastolic_digits = img[162:304, 100:314].copy()
    heartrate = img[307:354, 225:311].copy()

    kernel_1 = np.ones((5, 5), np.uint8)
    systolic_digits_dil = cv2.dilate(systolic_digits, kernel_1, iterations=1)
    diastolic_digits_dil = cv2.dilate(diastolic_digits, kernel_1, iterations=1)

    kernel_2 = np.ones((3, 3), np.uint8)
    heartrate_dil = cv2.dilate(heartrate, kernel_2, iterations=1)

    border_size = 10
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

    ocr_rois = [systolic_digits_dil_bordered, diastolic_digits_dil_bordered, heartrate_dil_bordered]
    feat_detect_rois = []

    # cv2.imshow("1", systolic_digits_dil_bordered)
    # cv2.imshow("2", diastolic_digits_dil_bordered)
    # cv2.imshow("3", heartrate_dil_bordered)
    # cv2.waitKey(1)

    return [ocr_rois, feat_detect_rois]


def roi_device_XX(img):
    """
BEKO Dishwasher
    :param img:
    :return:
    """
    program = img
    salt = img
    time = img
    play = img
    pause = img
    fast = img
    traywash = img

    ocr_rois = [program, time]
    feat_detect_rois = [salt,
                        play,
                        pause,
                        fast,
                        traywash]

    return [ocr_rois, feat_detect_rois]


def roi_device_13(img):
    """
BASETECH piggybank
    :param img:
    :return:
    """
    ocr_rois = [img]
    feat_detect_rois = []
    return [ocr_rois, feat_detect_rois]