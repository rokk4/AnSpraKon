# coding=utf-8
import sys
import subprocess
import cv2
import image_preprocessor
import ssocr
import roi_cutter
import result_processor
import feat_detector

# check if running on an RPi by trying to import the RPi.GPIO libary. If this fails, we are usually not on an RPi.
# ID of the device to read.
device_id = 1

video_src = 0  # index of the video source

# NanoTTS Options
lang = "de-DE"
volume = 0
rate = 0  # speed of the reading
pitch = 0
cam = cv2.VideoCapture(video_src)
def grab_image(src=0):
    """
Creates new cv VideoCapture object. Reads a frame and releases the VideoCapture Device.
    :param src:  Kernel Address of the Videosource: default 0 should be fine e.g: /dev/video0
    :return: The frame which was read as cv2 MAT format.
    """
  # create Caputure-Object
    retval, img = cam.read()

    return img


def process_image(img):
    """
Procceses an Image with the methods defined for the device in image_preprocessor.py
    :param img: image to process as cv2 MAT format
    :return: processed image
    """
    if device_id == 0:
        processed_image = image_preprocessor.image_device_0(img)
    elif device_id == 1:
        processed_image = image_preprocessor.image_device_1(img)
    return processed_image


def cut_roi(img):
    """
Cut out Rois
    :param img:
    :return: list of list [[ocr_rois],[feat_rois]]
    """
    if device_id == 0:
        return roi_cutter.roi_device_0(img)
    elif device_id == 1:
        return roi_cutter.roi_device_1(img)

def detect_feat(rois_cut):
    if device_id == 0:
        return feat_detector.feat_detect_device_0(rois_cut)

    if device_id == 1:
        return feat_detector.feat_detect_device_1(rois_cut)


def ssocr_call(rois):
    """
Sets the ssocr flags matching to the given device id
    :param img: processed image
    """
    if device_id == 0:
        return ssocr.ssocr_device_0(rois)
    elif device_id == 1:
        return ssocr.ssocr_device_1(rois)


def process_result(ocr_results):
    if device_id == 0:
        return result_processor.process_results_device_0(ocr_results)
    if device_id == 1:
        return result_processor.process_results_device_1(ocr_results)


def speak_ocr_results(processed_ocr_results="Ansprakon bereit."):
    """
Calls nanoTTS in an subprocess. nanoTTS parses text to pico.
-l de-DE flag sets the language to german.
Volume & Speed & Pitch control with flags is possible, see man nanoTTS
    :param text: this is the String from the ocr
    """
    global speak
    if speak:
        try:
            subprocess.call(["nanotts-git", "-v", lang, processed_ocr_results], stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print("Error code {} while speaking, output: {}".format(e.returncode, e.output))
    else:
        print("Not Speaking")
        pass







# boolean to hold the speaking again flag
speak = False
# variable to store last ocr string
text = ""
# variable to store new string
new_text = ""
cache = []


def ocr_and_speak():
    """
Read ssocr call into "new_text" and determine if the same text was read as in the last iteration.
Also speak the last text again  if "speak_again = True" was set.
    """
    global text, speak, new_text, cache

    new_text = process_result(
        ssocr_call(
            detect_feat(
                cut_roi(
                    process_image(
                        grab_image(
                            video_src))))))
    flat_list = [item for sublist in new_text for item in sublist]




    print(flat_list)









# Say "Ansprakon bereit" 1x time, to get audio feedback that the pi booted and AnSpraKon is running.
# speak_ocr_results()
start = False
while True:
    if speak:
        speak = True
    ocr_and_speak()
