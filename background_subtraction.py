import sys
import cv2 as cv
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

VIDEO_PATH = BASE_DIR / "example_videos" / "2026-08-13 22-22-15.mp4"

# create background subtractor model
back_sub = cv.createBackgroundSubtractorKNN()

cap = cv.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Failed to access camera")
    sys.exit(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        break # define it's endpoint

    # update background model
    fg_mask = back_sub.apply(frame)

    # get and display current frame number
    cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv.putText(frame, str(cap.get(cv.CAP_PROP_POS_FRAMES)), (15, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fg_mask)

    keyboard = cv.waitKey(30)
    if keyboard == ord('q') or keyboard == 27: # ESC Key
        sys.exit(0)
