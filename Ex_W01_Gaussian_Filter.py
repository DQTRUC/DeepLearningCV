import cv2 as cv

# Load an image in grayscale

img=cv.imread('E:\WORKING\Big Data\Deep Learning and Computer Vision\Ex\W1\Xucxac.png',1)

#Gaussian Blurring
gausBlur = cv.GaussianBlur(img, (5,5),0) #Again, you can change the kernel size

cv.imshow('image',gausBlur)
cv.waitKey(0)
cv.destroyAllWindows()

#Gaussian Blurring
gausBlur = cv.GaussianBlur(img, (5,5),10) #Again, you can change the kernel size

cv.imshow('image',gausBlur)
cv.waitKey(0)
cv.destroyAllWindows()

#Gaussian Blurring
gausBlur = cv.GaussianBlur(img, (25,25),50) #Again, you can change the kernel size

cv.imshow('image',gausBlur)
cv.waitKey(0)
cv.destroyAllWindows()
