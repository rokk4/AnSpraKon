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
    temp_result_pattern = re.compile("\d\d?\.\d")
    regex_result = temp_result_pattern.search(rois_processed[0][0].rstrip())
    if regex_result is not None:
        rois_processed[0][0] = temp_result_pattern.search(rois_processed[0][0]).group(0) + "°C"
    else:
        print("Dropping bad result.")
        print(rois_processed[0][0])
        del rois_processed[0][0]

    return rois_processed


def process_results_device_2(rois_processed):
    """
ADE humanscale
    :param rois_processed:
    :return:
    """
    weight_result_pattern = re.compile("\d\d?\d?\.\d")
    regex_result = weight_result_pattern.search(rois_processed[0][0].rstrip())
    if regex_result is not None:
        rois_processed[0][0] = weight_result_pattern.search(rois_processed[0][0]).group(0) + " " + "Kilogramm"
    else:
        print("Dropping bad result.")
        print(rois_processed[0][0])
        del rois_processed[0][0]

    return rois_processed


def process_results_device_3(rois_processed):
    """
Beurer humanscale
    :param rois_processed:
    :return:
    """
    weight_result_pattern = re.compile("\d\d?\d?\.\d")
    regex_result = weight_result_pattern.search(rois_processed[0][0].rstrip())
    if regex_result is not None:
        rois_processed[0][0] = weight_result_pattern.search(rois_processed[0][0]).group(0) + " " + "Kilogramm"
    else:
        print("Dropping bad result.")
        print(rois_processed[0][0])
        del rois_processed[0][0]

    return rois_processed


def process_results_device_4(rois_processed):
    """
NONAME indoor/outdoor thermometer
    :param rois_processed:
    :return:
    """
    temp_result_pattern = re.compile("\d?\d?\.?\d")

    indoor_temp_result = temp_result_pattern.search(rois_processed[0][0].rstrip())
    outdoor_temp_result = temp_result_pattern.search(rois_processed[0][1].rstrip())

    if indoor_temp_result is not None and outdoor_temp_result is not None:
        regex_indoor_temp_result = temp_result_pattern.search(rois_processed[0][0]).group(0)
        regex_outdoor_temp_result = temp_result_pattern.search(rois_processed[0][1]).group(0)
        print(regex_indoor_temp_result)
        print(regex_outdoor_temp_result)

        # _rois_processed[0][0] = regex_indoor_temp_result[:-1] + "." + regex_indoor_temp_result[-1:] + "°C"
        # _rois_processed[0][1] = regex_outdoor_temp_result[:-1] + "." + regex_outdoor_temp_result[-1:] + "°C"
        rois_processed[0][0] = regex_indoor_temp_result + " °C"
        rois_processed[0][1] = regex_outdoor_temp_result + " °C"
    else:
        print("Dropping bad result.")
        print(rois_processed[0][0])
        print(rois_processed[0][1])

    if rois_processed[1][0] and rois_processed[1][1] and not rois_processed[1][2] and not rois_processed[1][3]:
        rois_processed[0][0] += " Innentemperatur"
        rois_processed[0][1] += " Außentemperatur"

    if rois_processed[1][0] and not rois_processed[1][1] and rois_processed[1][2] and rois_processed[1][3]:
        rois_processed[0][0] += " Maximal Innentemperatur"
        rois_processed[0][1] += " Minimal Innentemperatur"

    if not rois_processed[1][0] and rois_processed[1][1] and rois_processed[1][2] and rois_processed[1][3]:
        rois_processed[0][0] += " Maximal Außentemperatur"
        rois_processed[0][1] += " Minimal Außentemperatur"

    print(rois_processed[0])
    return rois_processed


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
GREEN alarmclock
    :param rois_processed:
    :return:
    """

    rois_processed[0][0] = "Temperatur " + rois_processed[0][0].rstrip() + "." + rois_processed[0][1].rstrip() + " °C"
    rois_processed[0][1] = "Luftfeuchtigkeit " + rois_processed[0][2].rstrip() + " %"
    del rois_processed[0][2]

    rois_processed[1][0] = "Trocken" if rois_processed[1][0] else None
    rois_processed[1][1] = "Feucht" if rois_processed[1][1] else None
    rois_processed[1][2] = "Minimal" if rois_processed[1][2] else None
    rois_processed[1][3] = "Maximal" if rois_processed[1][3] else None
    rois_processed[1][4] = "Minimal" if rois_processed[1][4] else None
    rois_processed[1][5] = "Maximal" if rois_processed[1][5] else None

    print(rois_processed)

    return rois_processed


def process_results_device_7(rois_processed):
    """
CASIO calculator MS-20UC
    :param rois_processed:
    :return:
    """
    print(rois_processed)
    return rois_processed


def process_results_device_10(rois_processed):
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
