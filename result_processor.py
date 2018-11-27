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
import re


def process_results_device_0(rois_processed):
    """
Dummy Device
    :param rois_processed:
    :return:
    """
    return rois_processed


def process_results_device_1(rois_processed):
    """
BASETECH Thermometer
    :param rois_processed:
    :return:
    """
    temp_result_pattern = re.compile("\d?\d?\d")
    regex_result = temp_result_pattern.search(rois_processed[0][0].rstrip())
    results_processed = None
    if regex_result is not None:
        results_processed = temp_result_pattern.search(rois_processed[0][0]).group(0)
        results_processed = "Temperatur " + results_processed[:-1] + "." + results_processed[-1] + "°C"
    else:
        print("Dropping bad result.")

    return results_processed


def process_results_device_2(rois_processed):
    """
ADE humanscale
    :param rois_processed:
    :return:
    """
    results_processed = rois_processed[0][0].rstrip()
    weight_result_pattern = re.compile("\d?\d?\d\d")
    regex_result = weight_result_pattern.search(results_processed)
    if regex_result is None:
        results_processed = None
    else:
        results_processed = regex_result.group(0)

    if results_processed is not None:
        if len(results_processed) >= 2:
            results_processed = results_processed[:-1] + "," + results_processed[-1] + " Kilogramm."

    return results_processed


def process_results_device_3(rois_processed):
    """
Beurer humanscale
    :param rois_processed:
    :return:
    """

    print(rois_processed[0][0].rstrip())
    results_processed = rois_processed[0][0].rstrip()
    results_processed = re.sub('[^0-9]', '', results_processed)

    if results_processed is not None:
        if len(results_processed) >= 2:
            results_processed = results_processed[:-1] + "," + results_processed[-1] + " Kilogramm."

    return results_processed


def process_results_device_4(rois_processed):
    """
NONAME indoor/outdoor thermometer
    :param rois_processed:
    :return:
    """
    temp_result_pattern = re.compile("\d?\d\d")

    indoor_temp_result = temp_result_pattern.search(rois_processed[0][0].rstrip())
    outdoor_temp_result = temp_result_pattern.search(rois_processed[0][1].rstrip())
    print(rois_processed[0][0], rois_processed[0][1])

    if indoor_temp_result is not None and outdoor_temp_result is not None:
        regex_indoor_temp_result = temp_result_pattern.search(rois_processed[0][0]).group(0)
        regex_outdoor_temp_result = temp_result_pattern.search(rois_processed[0][1]).group(0)
        print(regex_indoor_temp_result)
        print(regex_outdoor_temp_result)

        rois_processed[0][0] = regex_indoor_temp_result[:-1] + "." + regex_indoor_temp_result[-1] + "°C"
        rois_processed[0][1] = regex_outdoor_temp_result[:-1] + "." + regex_outdoor_temp_result[-1] + "°C"

    else:
        results_processed = None
        return results_processed
        print("Dropping bad result.")

    if rois_processed[1][0] and rois_processed[1][1] and not rois_processed[1][2] and not rois_processed[1][3]:
        rois_processed[0][0] += " Innentemperatur."
        rois_processed[0][1] += " Außentemperatur."

    if rois_processed[1][0] and not rois_processed[1][1] and rois_processed[1][2] and rois_processed[1][3]:
        rois_processed[0][0] += " Maximal Innentemperatur."
        rois_processed[0][1] += " Minimal Innentemperatur."

    if not rois_processed[1][0] and rois_processed[1][1] and rois_processed[1][2] and rois_processed[1][3]:
        rois_processed[0][0] += " Maximal Außentemperatur."
        rois_processed[0][1] += " Minimal Außentemperatur."

    results_processed = rois_processed[0][0] + " " + rois_processed[0][1]

    return results_processed


def process_results_device_5(rois_processed):
    """
GREEN alarmclock
    :param rois_processed:
    :return:
    """
    # for ocr_results in _rois_processed[0]:
    #     print(filter(ocr_results.isdigit, ocr_results)[0])

    return rois_processed


def process_results_device_6(rois_processed):
    """
NONAME thermo-hygro meter
    :param rois_processed:
    :return string of the text to speak
    """

    rois_processed[0][0] = "Temperatur " + rois_processed[0][0].rstrip() + "." + rois_processed[0][1].rstrip() + "°C."
    rois_processed[0][1] = "Luftfeuchtigkeit " + rois_processed[0][2].rstrip() + "%."

    if rois_processed[1][2]:
        rois_processed[0][0] = "Minimal " + rois_processed[0][0]

    if rois_processed[1][3]:
        rois_processed[0][0] = "Maximal " + rois_processed[0][0]

    if rois_processed[1][4]:
        rois_processed[0][1] = "Minimal " + rois_processed[0][1]

    if rois_processed[1][5]:
        rois_processed[0][1] = "Maximal " + rois_processed[0][1]

    results_processed = rois_processed[0][0] + " " + rois_processed[0][1]

    if rois_processed[1][0] and not (rois_processed[1][2]
                                     or rois_processed[1][3]
                                     or rois_processed[1][4]
                                     or rois_processed[1][5]):
        results_processed = "Trocken. " + results_processed

    if rois_processed[1][1] and not (rois_processed[1][2]
                                     or rois_processed[1][3]
                                     or rois_processed[1][4]
                                     or rois_processed[1][5]):
        results_processed = "Feucht. " + results_processed

    return results_processed


def process_results_device_7(rois_processed):
    """
CASIO calculator MS-20UC
    :param rois_processed:
    :return:
    """
    print(rois_processed)
    return rois_processed


def process_results_device_8(rois_processed):
    """
IDR radio alarm
    :param rois_processed:
    :return:
    """
    for result in rois_processed[0]:
        print(result)

    results_processed = None

    first_digits = re.sub("[^0-9]", "", str(rois_processed[0][0]).rstrip())
    second_digits = re.sub("[^0-9]", "", str(rois_processed[0][1]).rstrip())

    if rois_processed[1][0]:
        results_processed = first_digits + ":" + second_digits + " Uhr"

    if rois_processed[1][3] or rois_processed[1][4]:
        results_processed = str(results_processed) + " Alarm 1 an."

    if rois_processed[1][5] or rois_processed[1][6]:
        results_processed = str(results_processed) + " Alarm 2 an."

    if rois_processed[1][2]:
        results_processed = first_digits + second_digits[0] + "." + second_digits[1] + " Mhz"

    return results_processed


def process_results_device_9(rois_processed):
    """
SCHNEIDER Microwave
    :param rois_processed:
    :return:
    """
    results_processed = None

    defrost_pattern = re.compile('^d\d?')
    power_pattern = re.compile('\d?\d\dp')
    time_pattern = re.compile('\d?\d\d\d')
    read_result = rois_processed[0][0].rstrip() + rois_processed[0][1].rstrip()

    print(read_result)

    if defrost_pattern.match(read_result):
        if read_result == "d1":
            results_processed = "Entfrosten Programm 1."
            return results_processed
        if read_result == "d2":
            results_processed = "Entfrosten Programm 2."
            return results_processed
        if read_result == "d3":
            results_processed = "Entfrosten Programm 3."
            return results_processed

    if power_pattern.match(read_result):
        if read_result == "100p":
            results_processed = "Leistung 100"
            return results_processed
        if read_result == "80p":
            results_processed = "Leistung 80"
            return results_processed
        if read_result == "60p":
            results_processed = "Leistung 60"
            return results_processed
        if read_result == "40p":
            results_processed = "Leistung 40"
            return results_processed
        if read_result == "20p":
            results_processed = "Leistung 20"
            return results_processed

    if time_pattern.match(read_result):
        results_processed = "Noch " + read_result[:-2] + " Minuten und " + read_result[-2:] + " Sekunden."
        return results_processed

    return results_processed


def process_results_device_10(rois_processed):
    results_processed = None
    temp_result_pattern = re.compile("\d?\d")
    temp_deci_result_pattern = re.compile("\d")

    temp_result = temp_result_pattern.search(rois_processed[0][0].rstrip())
    temp_deci_result = temp_deci_result_pattern.search(rois_processed[0][1].rstrip())

    if temp_result is not None:
        rois_processed[0][0] = temp_result.group(0)
        results_processed = "Temperatur " + rois_processed[0][0]
        if temp_deci_result is not None:
            rois_processed[0][1] = temp_deci_result.group(0)
            results_processed += "." + rois_processed[0][1]

    if results_processed is not None:
        results_processed += "°C."

    return results_processed


def process_results_device_11(rois_processed):
    """
SEVERIN Microwave
    :param rois_processed:
    :return:
    """
    results_processed = None
    digits_1_2 = rois_processed[0][0].rstrip()
    digits_3_4 = rois_processed[0][1].rstrip()
    double_dot_upper = rois_processed[1][0]
    double_dot_lower = rois_processed[1][1]

    if digits_1_2 + digits_3_4 == "def1":
        return "Entfrosten Programm 1"

    if digits_1_2 + digits_3_4 == "def2":
        return "Entfrosten Programm 2"

    if digits_1_2 + digits_3_4 == "p100":
        return "Programm 100"

    if digits_1_2 == "p":
        return "Programm " + digits_3_4

    if digits_1_2 == "a" or digits_1_2 == "c":
        regex = re.compile('[\W_]+', re.UNICODE)
        return digits_1_2 + regex.sub("", digits_3_4)

    if double_dot_upper and double_dot_lower:
        return "Noch " + digits_1_2 + " Minuten und " + digits_3_4 + " Sekunden."
    #
    # if not double_dot_upper and not double_dot_lower:
    #     return digits_1_2 + ":" + digits_3_4 + " Uhr."

    return results_processed


def process_results_device_12(rois_processed):
    """
Bloodpressure
    :param rois_processed:
    :return:
    """
    results_processed = None

    systolic_digits = re.sub('[^0-9]', '', rois_processed[0][0].rstrip())
    diastolic_digits = re.sub('[^0-9]', '', rois_processed[0][1].rstrip())
    heartrate = re.sub('[^0-9]', '', rois_processed[0][2].rstrip())

    if len(diastolic_digits) > 1:
        results_processed = "Blutdruck " + str(systolic_digits) + " zu " + str(diastolic_digits) + " . " + "Puls: " \
                            + str(heartrate)

    return results_processed


def process_results_device_13(rois_processed):
    """
Dummy Device
    :param rois_processed:
    :return:
    """
    results_processed = None

    digits = re.sub('[^0-9]', '', rois_processed[0][0].rstrip())
    temp_result_pattern = re.compile("\d?\d")

    return results_processed


def process_results_device_XX(rois_processed):
    """

    :param rois_processed:
    :return:
    """
    rois_processed[0][0] = "Programm " + rois_processed[0][0]
    rois_processed[0][1] = "Laufzeit " + rois_processed[0][1]

    rois_processed[1][0] = "Salz leer." if rois_processed[1][0] else None
    rois_processed[1][1] = "Läuft." if rois_processed[1][1] else None
    rois_processed[1][2] = "Pause." if rois_processed[1][2] else None
    rois_processed[1][3] = "Schnell." if rois_processed[1][3] else None
    rois_processed[1][4] = "Traywash." if rois_processed[1][4] else None

    return rois_processed
