import cv2
import numpy as np

if __name__ == '__main__' :

    # Read image
    im = cv2.imread("green_alarmradio_test.png")

    # Select ROI
    r = cv2.selectROI(im)

    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    print(r)
    print(str(r[1]) + ":" + str(r[1]+r[3]) + " " + str(r[0]) + ":" + str(r[0] + r[2]))

    # Display cropped image
    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)

    # beurerscale 145:448 23:620