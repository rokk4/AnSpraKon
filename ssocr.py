# coding=utf-8
import subprocess

import cv2


# Execute ssocr , encode cv2-MAT to .png and pipe it to STDIN, then receive the result from STDOUT.
def call_ssocr(ssocr_args, img):
    try:
        return_val = ""
        ssocr_args.insert(0, "ssocr")  # add "ssocr" as the first argument of the list.
        ssocr_args.append("-")  # append "-" as last argument of the list, it makes ssocr expect the image from STDIN
        if img is not None:
            img_as_png = cv2.imencode(".png", img)[1].tostring()  # encode image as .png and convert to byte-string.
            p = subprocess.Popen(ssocr_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate(img_as_png)  # send img as .png to ssocr and receive result in "out".
            # print(err) # print stderr for debugging
            # print(ssocr_args)
            return_val = out.decode("utf-8")
        return return_val
    except subprocess.CalledProcessError as e:
        print("Error code {} during ssocr call, output: {}".format(e.returncode, e.output))


def multicall_ssocr(ocr_rois, roi_ssocr_args):
    ocr_results = []
    device_arg_counter = 0
    for ocr_roi in ocr_rois:
        ocr_results.append(call_ssocr(roi_ssocr_args[device_arg_counter], ocr_roi))
        device_arg_counter += 1
    return ocr_results


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

    return [multicall_ssocr(rois[0], ssocr_args_list), rois[1]]


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
    return [multicall_ssocr(rois[0], ssocr_args_list), rois[1]]
