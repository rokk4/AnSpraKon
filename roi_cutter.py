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
    # indoor = img
    # outdoor = img
    weight = img
    ocr_rois = [weight]
    return [ocr_rois, []]


def roi_device_5(img):
    """
GREEN alarm radio
    :param img:
    :return:
    """
    digits_1 = img[51:224, 35:310].copy()
    digits_2 = img[45:217,321:574].copy()
    ocr_rois = [digits_1, digits_2]


    alarm_1 = img[195:222, 12:42].copy()
    alarm_2 = img[199:226, 587:612].copy()
    freq_shown = img[123:145,582:606].copy()

    feat_rois = [alarm_1, alarm_2, freq_shown]
    cv2.imshow("digits1", digits_1)
    cv2.imshow("digits2",digits_2)
    cv2.waitKey(60)
    return [ocr_rois, [feat_rois]]


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
