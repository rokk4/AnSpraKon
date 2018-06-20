# coding=utf-8
import call_ssocr


def ssocr_device_0(rois):
    """
SSOCR device speciefic function, to define the ssocr arguments
    :param rois: array of Images in CV2-MAT format
    :return: call of call_ssocr with the ssocr arguments matching the device
    """

    example_ocr = [
        "-D",
        "-d", "-1",
        "-i", "5",
        "-n", "20",
        "-r", "4",
    ]  # write the ssocr arguments in this array

    ssocr_args_list = [example_ocr]

    return [call_ssocr.multicall_ssocr(rois[0], ssocr_args_list), rois[1]]


def ssocr_device_1(rois):
    """
BASETech Room temperatur sensor
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    temperatur = [
        "-d", "-1",
        "-i", "5",
        "-n", "10"
              "-r", "4"

    ]

    ssocr_args_list = [temperatur]
    return [call_ssocr.multicall_ssocr(rois[0], ssocr_args_list), rois[1]]
