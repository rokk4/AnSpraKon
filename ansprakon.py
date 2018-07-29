# coding=utf-8
# AnSpraKon, reads 7-Segment-Displays and reads the result out loud.
# Copyright (C) 2018  Matthias Axel Kröll ansprakon@makroell.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>
import image_preprocessor
import ssocr
import roi_cutter
import result_processor
import feat_detector
import opencv_webcam_multithread
import call_nanotts
import cv2
import argparse
import gc
import sdnotify

gc.set_threshold(300, 5, 5)

license_info = """
    AnSpraKon  Copyright (C) 2018  Matthias Axel Kröll
    This program comes with ABSOLUTELY NO WARRANTY; 
    for details use optional argument `--show-w'.
    This is free software, and you are welcome to redistribute it under certain conditions; 
    for details use optional argument `--show-c' .
    """.encode('utf-8').rstrip()
print(license_info)


class Ansprakon:
    def __init__(self, args):
        self._device_id = args.device
        self._sdnotify = sdnotify.SystemdNotifier()
        self._nanotts_options = ["-v", args.language,
                                 "--speed", args.speed,
                                 "--pitch", args.pitch,
                                 "--volume", args.volume]
        self._speak_on_button = args.button
        self._cam = opencv_webcam_multithread.WebcamVideoStream(src=args.cam).start()
        self._grabbed_image = None
        self._preprocessed_image = None
        self._rois_cut = None
        self._rois_processed = None
        self._results_processed = None
        self._result_buffer = [[], []]
        self._on_pi = args.rpi
        self._gpio_pin = args.gpiopin
        if self._on_pi:
            # noinspection PyPep8Naming
            import RPi.GPIO as gpio
            gpio.setmode(gpio.BOARD)
            gpio.setwarnings(False)
            gpio.setup(self._gpio_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
            gpio.add_event_detect(self._gpio_pin, gpio.RISING, callback=self.gpio_callback)
        self._sdnotify.notify("READY=1")

    @property
    def sdnotify(self):
        return self._sdnotify

    def gpio_callback(self, channel):
        if len(self._result_buffer) > 2:
            call_nanotts.call_nanotts(self._nanotts_options, self._result_buffer[-1])

    def get_frame(self):
        try:
            self._grabbed_image = self._cam.read()
        except cv2.error as e:
            print(e)
            self.get_frame()

    def preprocess_image(self):
        """
    Processes an Image with the methods defined for the device in image_preprocessor.py
        :param self: image to process as cv2 MAT format
        :return: processed image
        """
        self._preprocessed_image = getattr(image_preprocessor, "image_device_" + self._device_id)(self._grabbed_image)

    def cut_rois(self):
        """
    Cuts out Rois and returns ocr-rois and feat-rois as
        :param self:
        :return: list of list [[ocr_rois],[feat_rois]]
        """
        self._rois_cut = getattr(roi_cutter, "roi_device_" + self._device_id)(self._preprocessed_image)

    def run_ssocr(self):
        """
    Sets the ssocr flags matching to the given device id
        :param self:
        """
        self._rois_processed = getattr(ssocr, "ssocr_device_" + self._device_id)(self._rois_cut)
        self._rois_cut[0] = self._rois_processed[0]

    def detect_feat(self):
        """
    Detect feat in the
        :param self:
        :return:
        """
        self._rois_processed = getattr(feat_detector, "feat_detect_device_" + self._device_id)(self._rois_cut)

    def process_result(self):
        """
    
        :param self:
        :return:
        """
        self._results_processed = getattr(result_processor,
                                          "process_results_device_" + self._device_id)(self._rois_processed)
        self._result_buffer.append(self._results_processed)
        if len(self._result_buffer) > 7:
            self._result_buffer = self._result_buffer[-4:]
        print(self._results_processed)

    def speak_result(self):
        if not self._speak_on_button:
            if self._results_processed not in self._result_buffer[-3:-1]:
                call_nanotts.call_nanotts(self._nanotts_options, self._results_processed)

        else:
            print("Did not Speak.")


def main():
    parser = argparse.ArgumentParser(description="read 7-segment displays and read out the result")
    parser.add_argument("device", help="enter the ID of the device to use")
    parser.add_argument("-b", "--button", help="speak on button press", action="store_true")
    parser.add_argument("-r", "--rpi", help="run on rpi", action="store_true")
    parser.add_argument("-g", "--gpiopin", help="set the GPIO pin", default=11, type=int)
    parser.add_argument("-c", "--cam", help="set the device index of the cam to use", default=0, type=int)
    parser.add_argument("-s", "--speed", help="set speed of the voice", default="1.5", metavar="<0.2-5.0>")
    parser.add_argument("-p", "--pitch", help="set the pitch of the voice", default="0.8", metavar="<0.5-2.0>")
    parser.add_argument("-v", "--volume", help="set the volume of the voice", default="1", metavar="<0.0-5.0>")
    parser.add_argument("-l", "--language", help="set the language of the voice", default="de-DE",
                        choices=["en-US", "en-GB", "de-DE", "es-ES", "fr-FR", "it-IT"])
    parser.add_argument("--version", action="version", version="%(AnSpraKon)s 2.0")
    parser.add_argument("--show-w", help="Show warranty details of the GPL", action="store_true")
    parser.add_argument("--show-c", help="Show redistribution conditions of the GPL", action="store_true")

    #parser.parse_args()
    args = parser.parse_args()

    ansprakon = Ansprakon(args)

    while True:
        ansprakon.get_frame()
        ansprakon.preprocess_image()
        ansprakon.cut_rois()
        ansprakon.run_ssocr()
        ansprakon.detect_feat()
        ansprakon.process_result()
        ansprakon.speak_result()
        ansprakon.sdnotify.notify("WATCHDOG=1")


if __name__ == "__main__":
    main()
