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

license_info = """
    AnSpraKon  Copyright (C) 2018  Matthias Axel Kröll
    This program comes with ABSOLUTELY NO WARRANTY; 
    for details use optional argument `--show-w'.
    This is free software, and you are welcome to redistribute it under certain conditions; 
    for details use optional argument `--show-c' .
    """
print(license_info)


class Ansprakon:
    def __init__(self, args):
        self.device_id = args.device
        self.nanotts_options = ["-v", args.language,
                                "--speed", args.speed,
                                "--pitch", args.pitch,
                                "--volume", args.volume]
        self.speak_on_button = args.button
        self.cam = opencv_webcam_multithread.WebcamVideoStream(src=0).start()
        self.grabbed_image = None
        self.preprocessed_image = None
        self.rois_cut = None
        self.rois_processed = None
        self.results_processed = None
        self.result_buffer = []

    def get_frame(self):
        try:
            self.grabbed_image = self.cam.read()
        except cv2.error as e:
            print(e)
            self.get_frame()

    def preprocess_image(self):
        """
    Processes an Image with the methods defined for the device in image_preprocessor.py
        :param self: image to process as cv2 MAT format
        :return: processed image
        """
        self.preprocessed_image = getattr(image_preprocessor, "image_device_" + self.device_id)(self.grabbed_image)

    def cut_rois(self):
        """
    Cuts out Rois and returns ocr-rois and feat-rois as
        :param self:
        :return: list of list [[ocr_rois],[feat_rois]]
        """
        self.rois_cut = getattr(roi_cutter, "roi_device_" + self.device_id)(self.preprocessed_image)

    def run_ssocr(self):
        """
    Sets the ssocr flags matching to the given device id
        :param self:
        """
        self.rois_processed = getattr(ssocr, "ssocr_device_" + self.device_id)(self.rois_cut)
        self.rois_cut[0] = self.rois_processed[0]

    def detect_feat(self):
        """
    Detect feat in the
        :param self:
        :return:
        """
        self.rois_processed = getattr(feat_detector, "feat_detect_device_" + self.device_id)(self.rois_cut)

    def process_result(self):
        """
    
        :param self:
        :return:
        """
        self.results_processed = getattr(result_processor,
                                         "process_results_device_" + self.device_id)(self.rois_processed)

        self.result_buffer.append(self.results_processed)

    def speak(self):
        if self.device_id in self.speak_on_change_devices and self.results_processed not in self.result_buffer[:-3]:
            self.result_buffer.append(self.results_processed)


def main():
    parser = argparse.ArgumentParser(description="read 7-segment displays and read out the result")
    parser.add_argument("device", help="enter the ID of the device to use")
    parser.add_argument("-b", "--button", help="speak on button press", action="store_true")
    parser.add_argument("-s", "--speed", help="set speed of the voice", default=1.5, type=float, metavar="<0.2-5.0>")
    parser.add_argument("-p", "--pitch", help="set the pitch of the voice", default=0.8, type=float,
                        metavar="<0.5-2.0>")
    parser.add_argument("-v", "--volume",
                        help="set the volume of the voice", default=1, type=float, metavar="<0.0-5.0>")
    parser.add_argument("-l", "--language", help="set the language of the voice", default="de-DE",
                        choices=["en-US", "en-GB", "de-DE", "es-ES", "fr-FR", "it-IT"])
    parser.add_argument("--version", action="version", version="%(AnSpraKon)s 2.0")
    parser.add_argument("--show-w", help="Show warranty details of the GPL", action="store_true")
    parser.add_argument("--show-c", help="Show redistribution conditions of the GPL", action="store_true")

    parser.parse_args()
    args = parser.parse_args()

    ansprakon = Ansprakon(args)
    while True:
        ansprakon.get_frame()
        ansprakon.preprocess_image()
        ansprakon.cut_rois()
        ansprakon.run_ssocr()
        ansprakon.detect_feat()
        ansprakon.process_result()


if __name__ == "__main__":
    main()
