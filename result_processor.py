import re


def process_results_device_0(rois_processed):
    return rois_processed


def process_results_device_1(rois_processed):
    temp_result_pattern = re.compile("\d\d?\.\d")
    regex_result = temp_result_pattern.search(rois_processed[0][0].rstrip())
    if regex_result != None:
        rois_processed[0][0] = temp_result_pattern.search(rois_processed[0][0]).group(0) + "°C"
    else:
        print("Shit read, dropped")
        del rois_processed[0][0]

    return rois_processed

def process_results_device_2(rois_processed):
    rois_processed[0][0] = "Programm " + rois_processed[0][0]
    rois_processed[0][1] = "Laufzeit " + rois_processed[0][1]

    rois_processed[1][0] = "Salz leer." if rois_processed[1][0] else ""
    rois_processed[1][1] = "Läuft." if rois_processed[1][1] else ""
    rois_processed[1][2] = "Pause." if rois_processed[1][2] else ""
    rois_processed[1][3] = "Schnell." if rois_processed[1][3] else ""
    rois_processed[1][4] = "Traywash." if rois_processed[1][3] else ""

    return rois_processed
