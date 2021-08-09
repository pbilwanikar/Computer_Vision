import numpy as np
import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Image',img)

# Translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, 100)
cv.imshow('translate', translated)

#rotation

def rotate(img, angle, rotPoint= None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated_img = rotate(img, 45)
cv.imshow("RTotated image", rotated_img)

# Flipping image
#0 --> flip image vertically over x axis
#1 --> flip imaghe horzontally over y axis
#-1 --> flip on both vertically and horizontally

flip =cv.flip(img, 1)
cv.imshow('Flipped', flip)




cv.waitKey(0)