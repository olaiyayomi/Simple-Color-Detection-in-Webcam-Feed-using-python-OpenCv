import cv2 as cv
import numpy as np
import sys

video = cv.VideoCapture(0)

if not video.isOpened():
    sys.exit("no camera")

while True:
    ret, frame = video.read()
    
    if not ret:
        print("not all frame captured")
    
    cvt = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lower_blue = np.array([110, 50, 50])
    high_blue = np.array([130, 255, 255])
    
    new = cv.inRange(cvt, lower_blue, high_blue)
    
    kervel = np.ones((5,5), np.uint8)
    reduce = cv.morphologyEx(new, cv.MORPH_OPEN, kervel)
    
    cv.imshow("reduce", reduce)
    cv.imshow("frame", frame)
    
    key = cv.waitKey(1)
    
    if key == ord("q"):
        break
cv.destroyAllWindows()
video.release()
