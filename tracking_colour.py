from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import pygame_renderer

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())

yellowLower = (62, 94, 121)
yellowUpper = (100, 180, 255)

pts = deque(maxlen=args["buffer"])

camera = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = camera.read()

    if args.get("video") and not grabbed:
        break

    frame = imutils.resize(frame, width=600)
    blur_frame = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, yellowLower, yellowUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)


    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    center = None

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        pts.appendleft((x + w/2, y + h/2))

    for i in xrange(1, len(pts)):
        if pts[i-1] is None or pts[i] is None:
            continue

        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 1.5)
        cv2.line(frame, pts[i-1], pts[i], (0, 255, 0), thickness)

    frame = cv2.flip(frame, flipCode=1)

    cv2.imwrite("/home/encipherer/Desktop/temp.jpg", frame)

    try:
        pygame_renderer.image_load("/home/encipherer/Desktop/temp.jpg")
    except SystemExit:
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()