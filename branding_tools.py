import cv2
import numpy as np

# =====================================
# CUSTOM TEXT BRANDING USING OPENCV
# =====================================

def add_text_branding(video_path, text, output):

    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(
        output,
        fourcc,
        fps,
        (width, height)
    )

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        overlay = frame.copy()

        # TEXT SETTINGS
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 3
        thickness = 5

        # GET TEXT SIZE
        text_size = cv2.getTextSize(
            text,
            font,
            font_scale,
            thickness
        )[0]

        # CENTER TEXT
        x = (width - text_size[0]) // 2
        y = height // 2

        # DRAW TEXT
        cv2.putText(
            overlay,
            text,
            (x, y),
            font,
            font_scale,
            (255, 255, 255),
            thickness,
            cv2.LINE_AA
        )

        # TRANSPARENCY
        alpha = 0.2

        frame = cv2.addWeighted(
            overlay,
            alpha,
            frame,
            1 - alpha,
            0
        )

        out.write(frame)

    cap.release()
    out.release()
