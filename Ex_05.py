
# Exercise 05: Preparing Image for edge detection

import cv2 as cv
import numpy as np

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

img = cv.imread(path + "\\Coins.png")
imgResized = cv.resize(img, (200, 300))

kernel = np.ones((5,5), "uint8")

imgGray = cv.cvtColor(imgResized, cv.COLOR_BGR2GRAY)

blurImg = cv.GaussianBlur(imgGray, (5,5), 0)

cannyImge = cv.Canny(blurImg, 10, 150)

imgDilation = cv.dilate(cannyImge, kernel, iterations=1)

contours, hierarchy = cv.findContours(imgDilation, 
    cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

print(len(contours))

cv.drawContours(imgResized, contours, -1, (0, 255, 0), 3)

result = np.hstack((imgGray, blurImg, cannyImge, imgDilation))

cv.imshow("image", imgResized)
cv.imshow("output", result)

cv.waitKey()
cv.destroyAllWindows()