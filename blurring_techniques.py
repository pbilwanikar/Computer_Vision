import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Image', img)

#Averaging Method
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#Gausssian Method
gaussian_average = cv.GaussianBlur(img, (7,7), sigmaX=0)
cv.imshow('Gaussian Blur', gaussian_average)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#Bilateral Blurring
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)