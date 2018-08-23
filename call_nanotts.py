# coding=utf-8
# This file is part of AnSpraKon.
# 
#     AnSpraKon is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     AnSpraKon is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with AnSpraKon.  If not, see <http://www.gnu.org/licenses/>.

import subprocess


def call_nanotts(nanotts_options, text="Ansprakon bereit."):
    """
Calls nanoTTS in an subprocess. nanoTTS parses text to pico.
-v de-DE flag sets the language to german.
Volume & Speed & Pitch control with flags is possible, see man nanoTTS
    :param nanotts_options:
    :param text: this is the String to speak
    """
    nanotts_flags = ["nanotts-git"] + nanotts_options + ['"' + text + '"']
    # print(nanotts_flags)
    # print(nanotts_options)
    try:
        subprocess.call(nanotts_flags, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        nanotts_error = "Error code {} while speaking, output: {}".format(e.returncode, e.output)
        print(nanotts_error)
        pass
