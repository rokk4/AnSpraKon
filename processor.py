# coding=utf-8
import cv2
import numpy


# Device ID 0
def example_device_0(img):
    """
This is an example method of processor.
    :param img: the image to process
    :return: the proccesd img
    """

    return img


# Device ID 1
def basetech_thermometer(img):
    """
This is another example method of processor.
    :param img: the image to process
    :return: the processed img
    """
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    rotated = cv2.rotate(grey,cv2.ROTATE_180) # rotate by 180 degree
    print(rotated.shape)

    crop_img = rotated[140:420, 120:510]

    ret, thresh1 = cv2.threshold(crop_img, 130, 180, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(thresh1,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY, 11, 2)


    processed_image = thresh1
    cv2.imshow('processd', processed_image)
    cv2.waitKey(10)

    return processed_image
