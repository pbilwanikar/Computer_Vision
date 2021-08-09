import cv2 as cv



img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Park', img)

# BGR --> GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR --> HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR --> LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)



cv.waitKey(0)