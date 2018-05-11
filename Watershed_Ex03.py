import cv2 as cv
import numpy as np

img = cv.imread('E:\WORKING\Big Data\Deep Learning and Computer Vision\Pics\coin_overlap.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

#Foreground region
fg = cv.erode(thresh,None,iterations = 2)

#Background region

bgt = cv.dilate(thresh,None,iterations = 3)
ret,bg = cv.threshold(bgt,1,128,1)

#Combine Forefround and background
marker = cv.add(fg,bg)

marker32 = np.int32(marker)

marker32=cv.watershed(img,marker32)

img[marker32 == -1] = [255,0,0]

cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()