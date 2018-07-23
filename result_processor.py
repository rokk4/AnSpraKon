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
        rois_processed[0][0] = weight_result_pattern.search(rois_processed[0][0]).group(0) + " " +"Kilogramm"
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
        rois_processed[0][0] = weight_result_pattern.search(rois_processed[0][0]).group(0) + " " +"Kilogramm"
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
    weight_result_pattern = re.compile("\d\d?\d?\.\d")
    regex_result = weight_result_pattern.search(rois_processed[0][0].rstrip())
    if regex_result is not None:
        rois_processed[0][0] = weight_result_pattern.search(rois_processed[0][0]).group(0) + " " +"Kilogramm"
    else:
        print("Dropping bad result.")
        print(rois_processed[0][0])
        del rois_processed[0][0]

    return rois_processed

def process_results_device_5(rois_processed):
    """
GREEN alarmclock
    :param rois_processed:
    :return:
    """
    for str in rois_processed[0]:
        print(filter(str.isdigit, str)[0])

    return rois_processed




def process_results_device_10(rois_processed):
    """

    :param rois_processed:
    :return:
    """
    rois_processed[0][0] = "Programm " + rois_processed[0][0]
    rois_processed[0][1] = "Laufzeit " + rois_processed[0][1]

    rois_processed[1][0] = "Salz leer." if rois_processed[1][0] else ""
    rois_processed[1][1] = "Läuft." if rois_processed[1][1] else ""
    rois_processed[1][2] = "Pause." if rois_processed[1][2] else ""
    rois_processed[1][3] = "Schnell." if rois_processed[1][3] else ""
    rois_processed[1][4] = "Traywash." if rois_processed[1][4] else ""

    return rois_processed
