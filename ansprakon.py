# coding=utf-8
import subprocess
import cv2
import processor
import ssocr

# check if running on an RPi by trying to import the RPi.GPIO libary. If this fails, we are usually not on an RPi.
try:
    import RPi.GPIO as GPIO

    run_on_pi = True
except ImportError:
    run_on_pi = False

# ID of the device to read.
device_id = 1

video_src = 0 # index of the video source

# PicoSpeaker Options
pico_lang = "de-DE"
pico_volume = 0
pico_rate = 0  # speed of the reading
pico_pitch = 0


def speak_text(text="Ansprakon bereit."):
    """
Calls picospeaker in an subprocess. Picospeaker parses text to pico.
-l de-DE flag sets the language to german.
Volume & Speed & Pitch control with flags is possible, see man picospeaker
    :param text: this is the String from the ocr
    """
    try:
        subprocess.call(["picospeaker", "-l", pico_lang, text], stdout=subprocess.PIPE)
        print(text)
    except subprocess.CalledProcessError as e:
        print("Error code {} while speaking, output: {}".format(e.returncode, e.output))





def grab_image(src=0):
    """
Creates new cv VideoCapture object. Reads a frame and releases the VideoCapture Device.
    :param src:  Kernel Address of the Videosource: default 0 should be fine e.g: /dev/video0
    :return: The frame which was read as cv2 MAT format.
    """
    cam = cv2.VideoCapture(src)  # create Caputure-Object
    retval, im = cam.read()
    cam.release()

    return im


def process_image(img):
    """
Procceses an Image with the methods defined for the device in processor.py
    :param img: image to process as cv2 MAT format
    :param device_id: device_id of the device, affects which methods of processor.py are used
    :return: processed image
    """
    if device_id == 0:
        return processor.example_device_0(img)
    elif device_id == 1:
        return processor.basetech_thermometer(img)


def ssocr_read(img):
    """
Sets the ssocr flags matching to the given device id
    :param img: processed image
    :param device_id: # of the device, affects which ssocr flags are set
    """
    if device_id == 0:
        return ssocr.ssocr_device_0(img)
    elif device_id == 1:
        return ssocr.ssocr_device_1(img)


# boolean to hold the speaking again flag
speak_again = False
# variable to store last ocr string
last_ocr = ""


def ocr_and_speak():
    """
Read ssocr call into "new_ocr" and determine if the same text was read as in the last iteration.
Also speak the last text again if if "speak_again = True" was set.
    """
    global last_ocr, speak_again, new_ocr
    new_ocr = ssocr_read(process_image(grab_image()))

    if new_ocr is not last_ocr or speak_again or last_ocr is "":             # catch edgecase at firstrun, when last_ocr is empty
        speak_again = False
        last_ocr = new_ocr
        return speak_text(last_ocr)


# Say "Ansprakon bereit" 1x time, to get audio feedback that the pi booted and AnSpraKon is running.
# speak_text()

while True:
    try:
        ocr_and_speak()
    except KeyboardInterrupt:
        speak_again = True
        ocr_and_speak()
