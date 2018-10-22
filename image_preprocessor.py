# coding=utf-8
# This file is part of AnSpraKon.
#
#     AnSpraKon is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     AnSpraKon is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with AnSpraKon.  If not, see <http://www.gnu.org/licenses/>.
import cv2
import numpy as np


# import preprocess_tools


# Device ID 0
def image_device_0(img):
    """
This is an example method of processor.
    :param img: the image to process
    :return: the processed img
    """
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
    blur2 = cv2.medianBlur(blur, 5)
    ret, th1 = cv2.threshold(blur2, 115, 255, cv2.THRESH_BINARY_INV)
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
    frame = cv2.rotate(img[52:314, 144:534], cv2.ROTATE_180)
    gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)

    # compute median
    # sigma = 0.33
    # v = np.median(gray)
    #
    # # apply automatic Canny edge detection using the computed median
    # # noinspection PyTypeChecker
    # lower = int(max(0, (1.0 - sigma) * v))
    # # noinspection PyTypeChecker
    # upper = int(min(255, (1.0 + sigma) * v))
    # edged = cv2.Canny(gray, lower, upper)

    # find contours
    # edged2, contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # global screenCnt, box
    # screenCnt = None
    # box = None

    # for c in contours:
    #     x, y, w, h = cv2.boundingRect(c)
    #     # hook into counter that has the expected size of the display
    #     if w > 200 and h > 150:
    #         # get extreme points of display contour
    #         ext_left, ext_right, ext_top, ext_bot = preprocess_tools.ext_from_hull(cv2.convexHull(c))
    #
    #         tl = (ext_left[0], ext_top[1] + 20)
    #         tr = (ext_right[0], ext_top[1])
    #         br = (ext_right[0], ext_bot[1] - 20)
    #         bl = (ext_left[0] + 20, ext_bot[1])
    #
    #         warped = preprocess_tools.four_point_transform(gray, tl, tr, br, bl)
    #         cv2.imshow("warped", warped)
    #         cv2.waitKey(1)
    #
    # ret, thresh1 = cv2.threshold(warped, 80, 255, cv2.THRESH_BINARY)
    # th3 = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
    #                            cv2.THRESH_BINARY, 11, 2)

    # Copy the thresholded image.
    ret, thresh1 = cv2.threshold(gray.copy(), 80, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
    im_floodfill = thresh1.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = thresh1.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)
    #
    # # Invert floodfilled image
    # im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    #
    # # Combine the two images to get the foreground.
    # im_out = thresh1 | im_floodfill_inv

    floodfilled_height, floodfilled_width = im_floodfill.shape
    pts1 = np.float32([[14, 6], [350, 14], [10, 240], [350, 240]])
    pts2 = np.float32(
        [[0, 0], [floodfilled_width, 0], [0, floodfilled_height], [floodfilled_width, floodfilled_height]])
    m = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(im_floodfill, m, (floodfilled_width, floodfilled_height))

    border_size = 10
    bordered = cv2.copyMakeBorder(dst, top=border_size, bottom=border_size,
                                  left=border_size,
                                  right=border_size,
                                  borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])

    kernel_1 = np.ones((4, 4), np.uint8)
    thresh1_dilated = cv2.dilate(thresh1, kernel_1, iterations=2)

    # # Display images
    # cv2.imshow("Thresholded Image", thresh1)
    # cv2.imshow("Thres Dilated", thresh1_dilated)
    # # cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
    # cv2.imshow("Foreground", bordered)
    # cv2.waitKey(1)

    return thresh1_dilated


# Device ID 2
def image_device_2(img):
    """
ADE-Germany Human Scale
    :param img:
    """
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(frame, 180, 255, cv2.THRESH_BINARY_INV)
    flip_180 = cv2.rotate(thresh1.copy(), cv2.ROTATE_180)
    im_floodfill = flip_180.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = thresh1.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)

    floodfilled = im_floodfill[72:414, 83:439].copy()

    floodfilled_height, floodfilled_width = floodfilled.shape
    pts1 = np.float32([[28, 12], [339, 9], [25, 325], [348, 317]])
    pts2 = np.float32(
        [[0, 0], [floodfilled_width, 0], [0, floodfilled_height], [floodfilled_width, floodfilled_height]])
    m = cv2.getPerspectiveTransform(pts1, pts2)
    preprocessed_image = cv2.warpPerspective(floodfilled, m, (floodfilled_width, floodfilled_height))

    border_size = 10
    bordered = cv2.copyMakeBorder(preprocessed_image, top=border_size, bottom=border_size,
                                  left=border_size,
                                  right=border_size,
                                  borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])

    # cv2.imshow("uncropped", im_floodfill)
    # cv2.imshow("preprocessed", bordered)
    # cv2.waitKey(1)

    return bordered


# Device ID 3
def image_device_3(img):
    """
BEURER Human Scale
    :param img:
    """

    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    flip_180 = cv2.rotate(frame.copy(), cv2.ROTATE_180)
    ret, thresh1 = cv2.threshold(flip_180[162:449, 20:629], 80, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

    im_floodfill = thresh1.copy()
    # cv2.imshow("flipped", thresh1)
    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = thresh1.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    # cv2.floodFill(im_floodfill, mask, (0, 0), 255)
    # cv2.imshow("flood", im_floodfill)

    floodfilled_height, floodfilled_width = im_floodfill.shape
    pts1 = np.float32([[58, 24], [588, 33], [22, 264], [550, 273]])
    pts2 = np.float32(
        [[0, 0], [floodfilled_width, 0], [0, floodfilled_height], [floodfilled_width, floodfilled_height]])
    m = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(im_floodfill, m, (floodfilled_width, floodfilled_height))

    border_size = 10
    bordered = cv2.copyMakeBorder(dst, top=border_size, bottom=border_size,
                                  left=border_size,
                                  right=border_size,
                                  borderType=cv2.BORDER_CONSTANT, value=[255, 255, ])

    kernel = np.ones((4, 4), np.uint8)

    bordered_dilated = cv2.dilate(bordered, kernel, iterations=1)

    # cv2.imshow("trans", bordered_dilated)
    # cv2.waitKey(1)
    return bordered_dilated.copy()


def image_device_4(img):
    """
NONAME indoor/outdoor thermometer
    :param img:
    """

    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(frame, 145, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
    flip_180 = cv2.rotate(thresh1, cv2.ROTATE_180)
    # im_floodfill = flip_180.copy()

    # # Mask used to flood filling.
    # # Notice the size needs to be 2 pixels than the image.
    # h, w = thresh1.shape[:2]
    # mask = np.zeros((h + 2, w + 2), np.uint8)

    # # Floodfill from point (0, 0)
    # cv2.floodFill(im_floodfill, mask, (0, 0), 255)

    # cv2.imshow("flood", im_floodfill)
    # cv2.waitKey(1)

    return flip_180


def image_device_5(img):
    """
GREEN radio alarm
    :param img:
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    blur2 = cv2.medianBlur(blur, 5)
    bi_filter = cv2.bilateralFilter(blur2, 11, 17, 17)
    ret, thresh1 = cv2.threshold(bi_filter, 120, 255, cv2.THRESH_BINARY_INV)
    blur3 = cv2.medianBlur(thresh1, 5)
    # Display the resulting frame
    # cv2.imshow('frame', blur3)
    # cv2.waitKey(1)

    return blur3.copy()


# Device ID 0
def image_device_6(img):
    """
NONAME thermo-hygro
    :param img: the image to process
    :return: the proccesd img
    """

    flip_180 = cv2.rotate(img.copy(), cv2.ROTATE_180)
    gray = cv2.cvtColor(flip_180[124:447, 49:495].copy(), cv2.COLOR_BGR2GRAY)
    # bi_filter = cv2.bilateralFilter(gray.copy(), 11, 17, 17)
    ret, thresh1 = cv2.threshold(gray.copy(), 90, 255, cv2.ADAPTIVE_THRESH_MEAN_C)

    im_floodfill = thresh1.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = thresh1.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)

    kernel = np.ones((1, 2), np.uint8)
    closing = cv2.morphologyEx(im_floodfill, cv2.MORPH_ERODE, kernel)
    closing2 = cv2.morphologyEx(closing, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("closing2",closing2)
    # cv2.waitKey(1)

    return closing2


# Device ID 7
def image_device_7(img):
    """
CASIO calculator MS-20UC
    :param img: the image to process
    :return: the processed img
    """

    flip_180 = cv2.rotate(img, cv2.ROTATE_180)
    gray = cv2.cvtColor(flip_180[41:245, 13:607], cv2.COLOR_BGR2GRAY)

    return gray.copy()


# Device ID 8
def image_device_8(img):
    """
IDF radio-alarm
    :param img: the image to process
    :return: the processed img
    """
    gray = cv2.cvtColor(img[241:401, 27:622].copy(), cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, 115, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    height, width = thresh1.shape
    pts1 = np.float32([[119, 20], [524, 20], [84, 150], [520, 150]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = cv2.getPerspectiveTransform(pts1, pts2)
    warped = cv2.warpPerspective(thresh1, m, (width, height))

    kernel_1 = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(warped, kernel_1, iterations=1)

    processed = [thresh1, dilated]

    return processed


# Device ID 0
def image_device_9(img):
    """
Schneider Mikrowelle
    :param img: the image to process
    :return: the processed img
    """
    flipped = cv2.rotate(img, cv2.ROTATE_180)
    gray = cv2.cvtColor(flipped.copy(), cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray[109:287, 19:626].copy(), 80, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = thresh1.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    im_floodfill = thresh1.copy()
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)

    shape_height, shape_width = im_floodfill.shape
    shape_pts1 = np.float32([[39, 14], [591, 15], [10, 173], [570, 171]])
    shape_pts2 = np.float32([[0, 0], [shape_width, 0], [0, shape_height], [shape_width, shape_height]])
    shape_m = cv2.getPerspectiveTransform(shape_pts1, shape_pts2)
    shape_dst = cv2.warpPerspective(im_floodfill, shape_m, (shape_width, shape_height))

    kernel = np.ones((4, 4), np.uint8)

    shape_dilated = cv2.dilate(shape_dst, kernel, iterations=1)

    border_size = 10
    white = [255, 255, 255]
    shape_bordered = cv2.copyMakeBorder(shape_dilated, top=border_size, bottom=border_size, left=border_size,
                                        right=border_size,
                                        borderType=cv2.BORDER_CONSTANT, value=white)

    # cv2.imshow("1", shape_bordered)
    # cv2.waitKey(1)

    return shape_bordered


# Device ID 10
def image_device_10(img):
    """
TECHNO-ONE Thermometer
    :param img: the image to process
    :return: the processed img
    """
    flipped = cv2.rotate(img, cv2.ROTATE_180)
    gray = cv2.cvtColor(flipped[24:175, 198:425].copy(), cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 100, 255, cv2.ADAPTIVE_THRESH_MEAN_C)

    # kernel = np.ones((4, 4), np.uint8)
    # thresh1_dilated = cv2.dilate(thresh1, kernel, iterations=1)
    #
    # cv2.imshow("1",thresh1)
    # # cv2.imshow("2",thresh1_dilated)
    # cv2.waitKey(1)

    return thresh1


# Device ID 11
def image_device_11(img):
    """
SEVERIN Microwave
    :param img: the image to process
    :return: the processed img
    """
    flipped = cv2.rotate(img, cv2.ROTATE_180)
    gray = cv2.cvtColor(flipped[182:385, 0:639].copy(), cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    height, width = thresh1.shape
    pts1 = np.float32([[65, 13], [630, 15], [35, 169], [603, 186]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = cv2.getPerspectiveTransform(pts1, pts2)
    warped = cv2.warpPerspective(thresh1, m, (width, height))

    return warped


# Device ID 12
def image_device_12(img):
    """
Bloodpressure
    :param img: the image to process
    :return: the processed img
    """
    flipped = cv2.rotate(img.copy(), cv2.ROTATE_90_CLOCKWISE)
    gray = cv2.cvtColor(flipped.copy(), cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray[213:564, 59:389], 127, 255, cv2.ADAPTIVE_THRESH_MEAN_C)

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

    return bordered


# Device ID 0
def image_device_13(img):
    """
BASETECH piggybank
    :param img: the image to process
    :return: the processed img
    """
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

    height, width = gray.shape
    pts1 = np.float32([[258, 45], [618, 47], [237, 197], [606, 206]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = cv2.getPerspectiveTransform(pts1, pts2)
    warped = cv2.warpPerspective(gray, m, (width, height))
    ret, thresh1 = cv2.threshold(warped, 55, 255, cv2.ADAPTIVE_THRESH_MEAN_C)

    cv2.imshow("warped", warped)
    cv2.imshow("thresh", thresh1)

    cv2.waitKey(1)

    return thresh1
