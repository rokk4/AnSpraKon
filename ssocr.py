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
    device_ssocr_args = [
        "-D",
        "-d", "-1",
        "-i", "5",
        "-n", "20"
              "-r", "5"

    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_2(rois):
    """
ADE-Germany Humanscale
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-D",
        "-d", "-1",
        "-i", "10"
              "-n", "70",
        "-r", "4"
    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_3(rois):
    """
Beurer Humanscale
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-D",
        "-d", "-1",
        "-i", "5"
              "-n", "120",
        "-r", "8"
    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_4(rois):
    """
NONAME indoor/outdoor thermometer
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-D",
        "-d", "-1",
        "-i", "1",
        "-n", "2"

    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_5(rois):
    """
GREEN alarm radio
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-D",
        "-d", "-1",
        "-i", "3",
        "-n", "50",
        "-r", "3"
    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_6(rois):
    """
NONAME thermo-hygor
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-D",
        "-d", "-1",
        "-i", "5",
        "-n", "10",
    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_7(rois):
    """
CASIO calculator MS20UC
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-D",
        "-d", "-1",
        "-i", "3",
        "-n", "5",
        "-r", "20",
    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]
