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
    del img

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

    #    cv2.imshow("indoor warp", indoor_temp_dst)
    #    cv2.imshow("outdoor warp", outdoor_temp_dst)

    border_size = 10

    indoor_warped_bordered = cv2.copyMakeBorder(indoor_temp_dst, top=border_size, bottom=border_size, left=border_size,
                                                right=border_size,
                                                borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])
    cv2.imshow("bordered warp indoor", indoor_warped_bordered)

    outdoor_warped_bordered = cv2.copyMakeBorder(outdoor_temp_dst, top=border_size, bottom=border_size,
                                                 left=border_size,
                                                 right=border_size,
                                                 borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])
    cv2.imshow("bordered warp outdoor", outdoor_warped_bordered)

    cv2.waitKey(1)

    ocr_rois = [indoor_warped_bordered.copy(), outdoor_warped_bordered.copy()]
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
    ocr_rois = [img]
    feat_detect_rois = []
    return [ocr_rois, feat_detect_rois]


def roi_device_10(img):
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
