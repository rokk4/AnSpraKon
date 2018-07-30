import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame[249:390, 24:616].copy(), cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray.copy(), 90, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    im_floodfill = thresh1.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = thresh1.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)
    # find all your connected components (white blobs in your image)
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(im_floodfill, connectivity=8)
    # connectedComponentswithStats yields every seperated component with information on each of them, such as size
    # the following part is just taking out the background which is also considered a component, but most of the time
    #  we don't want that.
    sizes = stats[0:, -1];
    nb_components = nb_components

    # minimum size of particles we want to keep (number of pixels)
    # here, it's a fixed value, but you can set it as you want, eg the mean of the sizes or whatever
    min_size = 300

    # your answer image
    img2 = np.zeros(output.shape)
    # for every component in the image, you keep it only if it's above min_size
    for i in range(0, nb_components):
        if sizes[i] >= min_size:
            img2[output == i + 1] = 255

    cv2.imshow("frame", img2)

    digit_1_2 = img2[2:127, 70:295].copy()
    digit_3_4 = img2[3:135, 320:552].copy()

    double_dot_upper = img2[18:44, 301:332].copy()
    double_dot_lower = img2[77:104, 295:321].copy()

    double_dot_upper_gray = gray[20:44, 302:332].copy()
    double_dot_lower_gray = gray[78:104, 293:321].copy()

    sleep_dot = img2[89:116, 565:592].copy()

    dot_digit_3_4 = digit_3_4[100:127, 103:132].copy()

    alarm_1_buzz = img2[50:73, 36:65].copy()
    alarm_1_music = img2[51:79, 565:590].copy()
    alarm_2_buzz = img2[12:44, 557:589].copy()
    alarm_2_music = img2[86:112, 33:62].copy()
    cv2.imshow("digit 1 2", digit_1_2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
