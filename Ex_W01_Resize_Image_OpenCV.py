import numpy as np
import cv2 as cv

# Load an image in grayscale

img=cv.imread('E:\WORKING\Big Data\Deep Learning and Computer Vision\Ex\W1\Xucxac.png',1)

print (img.shape)
print (img.size)

img2=cv.resize(img,(256,256))

#print (img2.shape)
#print (img2.size)

cv.imshow('image',img2)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('E:\WORKING\Big Data\Deep Learning and Computer Vision\Ex\W1\Xucxac_256.png',img2)

img3=cv.imread('E:\WORKING\Big Data\Deep Learning and Computer Vision\Ex\W1\Xucxac_GrayColor.png',0)
img3=cv.resize(img3,(256,256))

cv.imshow('image',img3)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('E:\WORKING\Big Data\Deep Learning and Computer Vision\Ex\W1\Xucxac_GrayColor_256.png',img3)