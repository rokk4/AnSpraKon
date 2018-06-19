def feat_detect_device_0(rois):
    counter = 0
    for feat_roi in rois[1]:
        rois[1][counter] = True
        counter += 1
    return rois


def feat_detect_device_1(rois):
    return rois


def feat_detect_device_2(rois):
    counter = 0
    for feat_roi in rois[1]:
        rois[1][counter] = True
        counter += 1
    return rois
