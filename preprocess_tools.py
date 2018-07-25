import cv2
import numpy as np


def rotate_bound(image, angle):
    """

    :param image:
    :param angle:
    :return:
    """
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    m = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(m[0, 0])
    sin = np.abs(m[0, 1])

    # compute the new bounding dimensions of the image
    n_w = int((h * sin) + (w * cos))
    n_h = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    m[0, 2] += (n_w / 2) - cX
    m[1, 2] += (n_h / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, m, (n_w, n_h))


def four_point_transform(image, tl, tr, br, bl):
    """

    :param image:
    :param tl:
    :param tr:
    :param br:
    :param bl:
    :return:
    """
    rect = np.zeros((4, 2), dtype="float32")
    rect[0] = tl
    rect[1] = tr
    rect[2] = br
    rect[3] = bl
    (tl, tr, br, bl) = rect

    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordinates or the top-right and top-left x-coordinates
    width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    max_width = max(int(width_a), int(width_b))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    max_height = max(int(height_a), int(height_b))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]], dtype="float32")

    # compute the perspective transform matrix and then apply it
    m = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, m, (max_width, max_height))

    # return the warped image
    return warped


def ext_from_hull(hull):
    """
    :return: The 4 extreme points of the hull contour.
    :type hull: openCV contour
    """
    ext_left = tuple(hull[hull[:, :, 0].argmin()][0])
    ext_right = tuple(hull[hull[:, :, 0].argmax()][0])
    ext_top = tuple(hull[hull[:, :, 1].argmin()][0])
    ext_bot = tuple(hull[hull[:, :, 1].argmax()][0])
    return ext_left, ext_right, ext_top, ext_bot

