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
        "-d", "-1",
        "-i", "3",
        "-n", "10",
        "-C"

    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_2(rois):
    """
ADE-Germany Humanscale
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-d", "-1",
        "-i", "3",
        "-n", "15",
        "-r", "4",
        "-C"
    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_3(rois):
    """
Beurer Humanscale
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-d", "-1",
        "-i", "3",
        "-n", "5",
        "-r", "800",
        "-C"
    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_4(rois):
    """
NONAME indoor/outdoor thermometer
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-d", "-1",
        "-i", "1",
        "-n", "2",
        "-C"

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
        "-d", "-1",
        "-i", "5",
        "-n", "10",
        "-C"
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


def ssocr_device_8(rois):
    """
IDR alarm-clock    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-d", "-1",
        "-i", "3",
        "-n", "10",
        "-C"

    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_9(rois):
    """
Schneider Microwave
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-D",
        "-d", "-1",
        "-i", "3",
        "-n", "10",
        # "-r", "7"
        "-C",
        "remove_isolated"
    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_9(rois):
    """
Schneider Microwave
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-d", "-1",
        "-i", "3",
        "-n", "5",
        "-C"

    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]


def ssocr_device_11(rois):
    """
SEVERIN Microwave
    :param rois:
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
        "-D",
        "-d", "-1",
        # "-i", "4",
        # "-n", "10",
        "-m 4",
        "-C"

    ]

    return [call_ssocr.multicall_ssocr(rois[0], device_ssocr_args), rois[1]]
