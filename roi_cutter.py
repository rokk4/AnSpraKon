import cv2

def roi_device_0(img):
    ocr_rois = [img]
    feat_detect_rois = []
    return [ocr_rois, feat_detect_rois]


def roi_device_1(img):
    temperature = img
    # try:
    #     cv2.imshow('warped', temperature)
    #     cv2.waitKey(1)
    # except cv2.error as e:
    #     print(e)



    ocr_rois = [temperature]
    return [ocr_rois, []]


def roi_device_2(img):
    program = img
    salt = img
    time = img
    play = img
    pause = img
    fast = img
    traywash = img

    ocr_rois = [program, time]
    feat_detect_rois = [salt,
                        play,
                        pause,
                        fast,
                        traywash]

    return [ocr_rois, feat_detect_rois]


