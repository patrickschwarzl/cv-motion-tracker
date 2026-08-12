import sys
import cv2 as cv
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

VIDEO_PATH = BASE_DIR / "example_videos" / "2025-04-19 11-15-35.mp4"

cap = cv.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Failed to access camera")
    sys.exit(0)

print("Success")
