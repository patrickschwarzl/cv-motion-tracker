import cv2 as cv
import sys
from pathlib import Path

VIDEO = "2026-08-13 22-22-15.mp4"


def main():
    base_dir = Path(__file__).resolve().parent
    video_path = base_dir / "example_videos" / VIDEO

    cap = cv.VideoCapture(video_path)

    if not cap.isOpened():
        print("Failed to open file")
        sys.exit(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Terminating...")
            sys.exit(0)

        cv.imshow("Frame", frame)

        key = cv.waitKey(10)
        if key == ord("q") or key == 27:
            print("Terminating...")
            sys.exit(0)


if __name__ == "__main__":
    main()
