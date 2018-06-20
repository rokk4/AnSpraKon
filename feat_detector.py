def feat_detect_device_0(rois):
    """

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

    :param rois:
    :return:
    """
    return rois


def feat_detect_device_2(rois):
    """

    :param rois:
    :return:
    """
    counter = 0
    for _ in rois[1]:
        rois[1][counter] = True
        counter += 1
    return rois
