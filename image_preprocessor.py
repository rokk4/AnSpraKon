# coding=utf-8
import cv2
import numpy as np

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

def four_point_transform(image, tl, tr, br, bl):
    rect = np.zeros((4, 2), dtype = "float32")
    rect[0] = tl
    rect[1] = tr
    rect[2] = br
    rect[3] = bl
    (tl, tr, br, bl) = rect


    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # compute the perspective transform matrix and then apply it
    m = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, m, (maxWidth, maxHeight))

    # return the warped image
    return warped


# Device ID 0
def image_device_0(img):
    """
This is an example method of processor.
    :param img: the image to process
    :return: the proccesd img
    """
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
    blur2 = cv2.medianBlur(blur, 5)
    ret, th1 = cv2.threshold(blur2, 123, 255, cv2.THRESH_BINARY_INV)
    rotated_180 = cv2.rotate(th1, cv2.ROTATE_180)
    img = rotated_180[30:405, 0:520]
    return img


# Device ID 1
def image_device_1(img):
    """
This is another example method of processor.
    :param img: the image to process
    :return: the processed img
    """
    frame = img[120:430, 20:600]
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bi_filter = cv2.bilateralFilter(gray, 11, 17, 17)
    sigma = 0.33
    v = np.median(gray)

    # ---- apply automatic Canny edge detection using the computed median----
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(gray, lower, upper)
    # edged2 = cv2.Canny(gray, lower, upper)

    # minLineLength = 200
    # maxLineGap = 1
    # lines1 = cv2.HoughLinesP(edged2,1,np.pi/180,200,minLineLength,maxLineGap)
    # qlines2 = cv2.HoughLines(edged1,1,np.pi/180,200)

    #    for x1,y1,x2,y2 in lines1[0]:
    #       cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

    edged2, contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    global screenCnt, box
    screenCnt = None
    box = None

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w > 200 and h > 100:
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            screenCnt = c
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            rect = cv2.minAreaRect(screenCnt)
            # rect2 = cv2.minAreaRect(approx)
            box = cv2.boxPoints(rect)
            #hull = cv2.convexHull(c)
            # x, y, w, h = cv2.boundingRect(hull)
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 1)
            # print(box)
            # qprint(len(hull))
            box = np.int0(box)
            # cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
            # cv2.drawContours(frame, [screenCnt], 0, (255, 0, 0), 5)
            # cv2.drawContours(frame, [approx], 0, (0, 255, 0), 5)
            # cv2.drawContours(frame, [hull], 0, (0, 255, 255), 2)

            extLeft = tuple(c[c[:, :, 0].argmin()][0])
            extRight = tuple(c[c[:, :, 0].argmax()][0])
            extTop = tuple(c[c[:, :, 1].argmin()][0])
            extBot = tuple(c[c[:, :, 1].argmax()][0])

            #print(extBot, extTop, extRight, extLeft)
            # tl, tr, br, bl
            tl = (extLeft[0] + 80, extTop[1])
            tr = (extRight[0] - 90, extTop[1])
            br = (extRight[0] - 85, extBot[1] - 10)
            bl = (extLeft[0] + 80, extBot[1] - 10)
          #  global warped
            warped = four_point_transform(frame, tl, tr, br, bl)
            return warped
            #return warped
            #print(tl, tr, br, bl)


