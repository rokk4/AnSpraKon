# coding=utf-8
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
    weight_result_pattern = re.compile("\d\d\d")
    results_processed = rois_processed[0][0].rstrip()
    regex_result = weight_result_pattern.search(results_processed)
    if regex_result is None:
        results_processed = None
    else:
        results_processed = regex_result.group(0)

    if results_processed == "1" \
            or results_processed == "11" \
            or results_processed == "111" \
            or results_processed == "1111" \
            or results_processed == "118" \
            or results_processed == "18" \
            or results_processed == "181":
        results_processed = None

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
    print(rois_processed)
    results_processed = None

    return results_processed


def process_results_device_9(rois_processed):
    # TODO: Process results
    """
SCHNEIDER Microwave
    :param rois_processed:
    :return:
    """
    results_processed = None

    for result in rois_processed[0]:
        print(result)

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
