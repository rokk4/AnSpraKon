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
import cv2
import subprocess


# Execute ssocr , encode cv2-MAT to .png and pipe it to STDIN, then receive the result from STDOUT.
def call_ssocr(ssocr_args, img):
    try:
        return_val = ""
        # add "ssocr" as the first argument of the list.
        ssocr_args.insert(0, "ssocr") if ssocr_args[0] != "ssocr" else ssocr_args[0]
        # append "-" as last argument of the list, it makes ssocr expect the image from STDIN
        ssocr_args.append("-") if ssocr_args[-1] != "-" else ssocr_args[-1]

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


def multicall_ssocr(rois, ssocr_args_list):
    ocr_results = []
    for ocr_roi in rois:
        ocr_results.append(call_ssocr(ssocr_args_list, ocr_roi))

    return ocr_results
