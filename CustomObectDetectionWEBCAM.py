
# Exercise 05: Preparing Image for edge detection

import cv2 as cv
import numpy as np

def nothing(x):
    pass

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

cv.namedWindow("image")

cv.createTrackbar("lower", "image", 0, 255, nothing)
cv.createTrackbar("upper", "image", 0, 255, nothing)

# img = cv.imread(path + "\\piece05.png")
# imgResized = cv.resize(img, (200, 300))
img = cv.VideoCapture(0)

kernel = np.ones((5,5), "uint8")
while True:

    lo = cv.getTrackbarPos("lower", "image")
    upper = cv.getTrackbarPos("upper", "image")

    success, frame = img.read()

    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurImg = cv.GaussianBlur(imgGray, (5,5), 0)
    cannyImge = cv.Canny(blurImg, lo, upper)
    imgDilation = cv.dilate(cannyImge, kernel, iterations=1)
    contours, hierarchy = cv.findContours(imgDilation, 
        cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    print(len(contours))

    cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

    # result = np.hstack((imgGray, blurImg, cannyImge, imgDilation))

    # cv.imshow("image", imgResized)
    cv.imshow("image", frame)

    k = cv.waitKey(1)

    if k == ord("q"):
        break

cv.destroyAllWindows()