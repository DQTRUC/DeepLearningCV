import numpy as np
import cv2 as cv

# Load an image in grayscale

img=cv.imread('E:\WORKING\Big Data\Deep Learning and Computer Vision\Ex\W1\Xucxac.png',1)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()

img=cv.imread('E:\WORKING\Big Data\Deep Learning and Computer Vision\Ex\W1\Xucxac.png',0)
cv.imwrite('E:\WORKING\Big Data\Deep Learning and Computer Vision\Ex\W1\Xucxac_GrayColor.png',img)

img=cv.imread('E:\WORKING\Big Data\Deep Learning and Computer Vision\Ex\W1\Xucxac_GrayColor.png',0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()

