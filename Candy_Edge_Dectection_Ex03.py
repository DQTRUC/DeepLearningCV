import numpy as np
import cv2 as cv

# Load an image in grayscale

def nothing(x):
    pass
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('Threshold01','image',0,1000,nothing)
cv.createTrackbar('Threshold02','image',0,1000,nothing)

img = cv.imread('E:\WORKING\Big Data\Deep Learning and Computer Vision\Pics\strawberry.jpg', 0)
cv.imwrite("strawberry_canny.jpg", cv.Canny(img, 200, 300))
img=cv.imread("strawberry_canny.jpg")
cv.imshow('image', img)

while(1):

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    Th01 = cv.getTrackbarPos('Threshold01','image')
    Th02 = cv.getTrackbarPos('Threshold02','image')

    img = cv.imread('E:\WORKING\Big Data\Deep Learning and Computer Vision\Pics\strawberry.jpg', 0)
    cv.imwrite("strawberry_canny.jpg", cv.Canny(img, Th01, Th02))
    img=cv.imread("strawberry_canny.jpg")
    cv.imshow('image', img)

cv.destroyAllWindows()



