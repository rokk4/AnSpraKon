# coding=utf-8
import subprocess
import cv2


def ssocr_device_0(img):
    """
SSOCR device speciefic function, to define the ssocr arguments
    :param img: img in CV2-MAT format
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
    ]    # write the ssocr arguments in this array
    return call_ssocr(device_ssocr_args, img)

def ssocr_device_1(img):
    """
BASETech Room temperatur sensor
    :param img: img in CV2-MAT format
    :return: call of call_ssocr with the ssocr arguments matching the device
    """
    device_ssocr_args = [
    "-d -1"
    ]    # write the ssocr arguments in this array
    return call_ssocr(device_ssocr_args, img)





# Execute ssocr , encode cv2-MAT to .png and pipe it to STDIN, then receive the result from STDOUT.
def call_ssocr(ssocr_args, img):
    try:
        ssocr_args.insert(0, "ssocr")  # add "ssocr" as the first argument of the list.
        ssocr_args.append("-")  # append "-" as last argument of the list, it makes ssocr expect the image from STDIN
        img_as_png = cv2.imencode(".png", img)[1].tostring()  # encode image as .png and convert to byte-string.
        p = subprocess.Popen(ssocr_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate(img_as_png)  # send img as .png to ssocr and receive result in "out".
        print(err) # print stderr for debugging
        return_val = out.decode("utf-8")
        return return_val
    except subprocess.CalledProcessError as e:
        print("Error code {} during ssocr call, output: {}".format(e.returncode, e.output))
