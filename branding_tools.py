from moviepy.editor import *

# =====================================
# FULL SCREEN LOGO WATERMARK
# =====================================

def add_logo_fullscreen(video_path, logo_path, output, opacity=0.2):

    # LOAD VIDEO
    video = VideoFileClip(video_path)

    # LOAD LOGO
    logo = (
        ImageClip(logo_path)
        .set_duration(video.duration)
        .resize((video.w, video.h))
        .set_position(("center", "center"))
        .set_opacity(opacity)
    )

    # COMBINE VIDEO + LOGO
    final = CompositeVideoClip([video, logo])

    # EXPORT VIDEO
    final.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )


# =====================================
# CUSTOM TEXT BRANDING
# =====================================

import cv2
import numpy as np

# =====================================
# CUSTOM TEXT BRANDING USING OPENCV
# =====================================

def add_text_branding(video_path, text, output):

    # LOAD VIDEO
    cap = cv2.VideoCapture(video_path)

    # GET VIDEO SETTINGS
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

        # CREATE OVERLAY
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

        # CENTER POSITION
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

        # WRITE FRAME
        out.write(frame)

    cap.release()
    out.release()

    # LOAD VIDEO
    video = VideoFileClip(video_path)

    # CREATE TEXT
    txt = (
        TextClip(
            text,
            fontsize=80,
            color='white',
            stroke_color='black',
            stroke_width=2,
            method='caption',
            size=(video.w, None)
        )
        .set_duration(video.duration)
        .set_position(("center", "center"))
        .set_opacity(0.2)
    )

    # COMBINE VIDEO + TEXT
    final = CompositeVideoClip([video, txt])

    # EXPORT VIDEO
    final.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )
