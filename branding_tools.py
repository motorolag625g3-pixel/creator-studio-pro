from moviepy.editor import *
import cv2
import numpy as np

# =====================================
# FULL SCREEN LOGO WATERMARK
# =====================================

def add_logo_fullscreen(video_path, logo_path, output, opacity=0.2):

    # LOAD MAIN VIDEO
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

def add_text_branding(video_path, text, output):

    temp_output = "temp/temp_branding.mp4"

    # LOAD VIDEO
    cap = cv2.VideoCapture(video_path)

    # VIDEO SETTINGS
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # VIDEO WRITER
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(
        temp_output,
        fourcc,
        fps,
        (width, height)
    )

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # COPY FRAME
        overlay = frame.copy()

        # FONT SETTINGS
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 3
        thickness = 5

        # TEXT SIZE
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

        # TEXT TRANSPARENCY
        alpha = 0.4

        # BLEND TEXT + VIDEO
        frame = cv2.addWeighted(
            overlay,
            alpha,
            frame,
            1 - alpha,
            0
        )

        # WRITE FRAME
        out.write(frame)

    # RELEASE VIDEO
    cap.release()
    out.release()

    # RE-ENCODE FOR BROWSER PLAYBACK
    final_clip = VideoFileClip(temp_output)

    final_clip.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )


# =====================================
# ADD INTRO VIDEO
# =====================================

def add_intro_video(intro_path, main_video_path, output):

    # LOAD VIDEOS
    intro = VideoFileClip(intro_path)
    main_video = VideoFileClip(main_video_path)

    # MATCH RESOLUTION
    intro = intro.resize(main_video.size)

    # MATCH FPS
    intro = intro.set_fps(main_video.fps)

    # COMBINE VIDEOS
    final_video = concatenate_videoclips(
        [intro, main_video],
        method="compose"
    )

    # EXPORT FINAL VIDEO
    final_video.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac",
        fps=main_video.fps
    )


# =====================================
# REPLACE VIDEO AUDIO
# =====================================

def replace_video_audio(video_path, new_audio_path, output):

    # LOAD VIDEO
    video = VideoFileClip(video_path)

    # REMOVE OLD AUDIO
    video = video.without_audio()

    # LOAD NEW AUDIO
    new_audio = AudioFileClip(new_audio_path)

    # MATCH AUDIO LENGTH
    new_audio = new_audio.set_duration(video.duration)

    # ADD NEW AUDIO
    final_video = video.set_audio(new_audio)

    # EXPORT VIDEO
    final_video.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )


# =====================================
# TRIM VIDEO
# =====================================

def trim_video(video_path, start_time, end_time, output):

    # LOAD VIDEO
    video = VideoFileClip(video_path)

    # TRIM VIDEO
    trimmed = video.subclip(start_time, end_time)

    # REMOVE AUDIO TO AVOID STREAMLIT ERRORS
    trimmed = trimmed.without_audio()

    # EXPORT VIDEO
    trimmed.write_videofile(
        output,
        codec="libx264",
        audio=False
    )
    # =====================================
# INSERT MID-ROLL ADVERTISEMENTS
# =====================================

def insert_advertisements(
    main_video_path,
    ad_video_path,
    ad_count,
    output
):

    # LOAD MAIN VIDEO
    main_video = VideoFileClip(main_video_path)

    # LOAD AD VIDEO
    ad_video = VideoFileClip(ad_video_path)

    # MAIN VIDEO DURATION
    duration = main_video.duration

    # SPLIT POINTS
    split_points = []

    for i in range(1, ad_count + 1):

        point = (duration / (ad_count + 1)) * i

        split_points.append(point)

    # CREATE VIDEO PARTS
    clips = []

    previous = 0

    for point in split_points:

        # MAIN VIDEO PART
        part = main_video.subclip(previous, point)

        clips.append(part)

        # ADD AD VIDEO
        ad_resized = ad_video.resize(main_video.size)
        ad_resized = ad_resized.set_fps(main_video.fps)

        clips.append(ad_resized)

        previous = point

    # LAST PART OF VIDEO
    last_part = main_video.subclip(previous)

    clips.append(last_part)

    # COMBINE ALL CLIPS
    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    # EXPORT VIDEO
    final_video.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac",
        fps=main_video.fps
    )
