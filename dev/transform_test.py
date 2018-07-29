import numpy as np
import cv2 as cv

img = cv.imread('beurer_scale_test.png')
rows, cols, ch = img.shape
pts1 = np.float32([[80, 165], [610, 173], [20, 420], [580, 440]])
pts2 = np.float32([[0, 0], [640, 0], [0, 480], [640, 480]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (640, 480))

cv.imshow("normal", img)
cv.imshow("transformed", dst)
cv.waitKey(0)
