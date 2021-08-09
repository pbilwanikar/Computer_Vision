import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# Coverting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# cv.waitKey(0)

# Blurring the image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT )
cv.imshow('Blur', blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded',eroded)

# Resize
resized = cv.resize(img, (500, 500))
cv.imshow('Resize', resized)


cv.waitKey(0)


