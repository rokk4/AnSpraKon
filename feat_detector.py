def feat_detect_device_0(rois):
    """
    Dummy Device
    :param rois:
    :return:
    """
    counter = 0
    for _ in rois[1]:
        rois[1][counter] = True
        counter += 1
    return rois


def feat_detect_device_1(rois):
    """
BASETECH thermometer
    :param rois:
    :return:
    """
    return rois


def feat_detect_device_2(rois):
    """
ADE humanscale
    :param rois:
    :return:
    """
    return rois

def feat_detect_device_3(rois):
    """
beurer humanscale
    :param rois:
    :return:
    """
    return rois

def feat_detect_device_4(rois):
    """
NONAME indoor/outdoor thermometer
    :param rois:
    :return:
    """
    return rois

def feat_detect_device_5(rois):
    """
GREEN alarm/radio
    :param rois:
    :return:
    """
    return rois
