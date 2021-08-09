import cv2 as cv


def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

''' This function only works on live Video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
'''


capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# capturing video

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleframe(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

    capture.release()
    cv.destroyAllWindows()
