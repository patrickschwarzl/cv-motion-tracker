import cv2 as cv
import sys
from pathlib import Path

VIDEO = "2026-08-13 22-22-15.mp4"
TRACKER = "MIL"

def main():
    base_dir = Path(__file__).resolve().parent
    video_path = base_dir / "example_videos" / VIDEO

    # available tracker models
    tracker_dict = {
        "MIL": cv.TrackerMIL_create,
        "DaSiamRPN": cv.TrackerDaSiamRPN_create,
        "Nano": cv.TrackerNano_create,
        "ViT": cv.TrackerVit_create,
    }

    tracker = tracker_dict[TRACKER]()

    cap = cv.VideoCapture(video_path)

    if not cap.isOpened():
        print("Failed to open file")
        sys.exit(0)

    # read and display first frame
    ret, frame = cap.read()

    if not ret:
        print("Exiting early...")
        sys.exit(0)

    cv.imshow("Frame", frame)

    # create bounding box
    bounding_box = cv.selectROI("Frame", frame)

    # initialize tracker
    tracker.init(frame, bounding_box)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Terminating...")
            sys.exit(0)

        success, box = tracker.update(frame)

        if success:
            x, y, w, h = [
                int(a) for a in box
            ]  # coordinates of our bounding box top left corner
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)

        cv.imshow("Frame", frame)

        key = cv.waitKey(10)
        if key == ord("q") or key == 27:
            print("Terminating...")
            sys.exit(0)

if __name__ == "__main__":
    main()
