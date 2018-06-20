# coding=utf-8
import cv2
import numpy as np
import preprocess_tools


# Device ID 0
def image_device_0(img):
    """
This is an example method of processor.
    :param img: the image to process
    :return: the proccesd img
    """
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
    blur2 = cv2.medianBlur(blur, 5)
    ret, th1 = cv2.threshold(blur2, 123, 255, cv2.THRESH_BINARY_INV)
    rotated_180 = cv2.rotate(th1, cv2.ROTATE_180)
    img = rotated_180[30:405, 0:520]
    return img


# Device ID 1
def image_device_1(img):
    """
The BASE-TECH Thermometer
    :param img: the image to preprocess
    :return: the preprocessed img
    """
    # crop, rotate and convert to Greyscale
    frame = img[120:430, 20:600].copy()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # compute median
    sigma = 0.33
    v = np.median(gray)

    # apply automatic Canny edge detection using the computed median
    # noinspection PyTypeChecker
    lower = int(max(0, (1.0 - sigma) * v))
    # noinspection PyTypeChecker
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(gray, lower, upper)

    # find contours
    edged2, contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    global screenCnt, box
    screenCnt = None
    box = None

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        # hook into counter that has the expected size of the display
        if w > 230 and h > 150:
            # get extreme points of display contour
            ext_left, ext_right, ext_top, ext_bot = preprocess_tools.ext_from_hull(cv2.convexHull(c))

            tl = (ext_left[0], ext_top[1] + 20)
            tr = (ext_right[0], ext_top[1])
            br = (ext_right[0], ext_bot[1] - 20)
            bl = (ext_left[0] + 20, ext_bot[1])

            warped = preprocess_tools.four_point_transform(gray, tl, tr, br, bl)
            ret, thresh1 = cv2.threshold(warped, 70, 255, cv2.THRESH_BINARY)

            return thresh1
