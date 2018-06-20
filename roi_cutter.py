import cv2


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
    try:
        cv2.imshow('webcam', temperature)
        cv2.waitKey(1)
    except cv2.error as e:
        print(e)

    return [ocr_rois, []]


def roi_device_2(img):
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
