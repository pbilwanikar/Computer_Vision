import cv2 as cv

img = cv.imread('Resources/Photos/cat_large.jpg') # reading of image

cv.imshow('cat',img) #showing the image in new window

cv.waitKey(0)