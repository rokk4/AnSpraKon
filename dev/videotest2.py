import numpy as np
import cv2

vidcap = cv2.VideoCapture("/home/r0x/Development/ansprakon-v2/dev/output.avi")

success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("frame%d.png" % count, image)  # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
