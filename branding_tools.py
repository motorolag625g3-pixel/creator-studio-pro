from moviepy.editor import *
import cv2
import numpy as np
import whisper
import textwrap

# =====================================
# FULL SCREEN LOGO WATERMARK
# =====================================

def add_logo_fullscreen(video_path, logo_path, output, opacity=0.2):

    video = VideoFileClip(video_path)

    logo = (
        ImageClip(logo_path)
        .set_duration(video.duration)
        .resize((video.w, video.h))
        .set_position(("center", "center"))
        .set_opacity(opacity)
    )

    final = CompositeVideoClip([video, logo])

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

    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

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

        overlay = frame.copy()

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 3
        thickness = 5

        text_size = cv2.getTextSize(
            text,
            font,
            font_scale,
            thickness
        )[0]

        x = (width - text_size[0]) // 2
        y = height // 2

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

        alpha = 0.4

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

    intro = VideoFileClip(intro_path)
    main_video = VideoFileClip(main_video_path)

    intro = intro.resize(main_video.size)
    intro = intro.set_fps(main_video.fps)

    final_video = concatenate_videoclips(
        [intro, main_video],
        method="compose"
    )

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

    video = VideoFileClip(video_path)

    video = video.without_audio()

    new_audio = AudioFileClip(new_audio_path)

    new_audio = new_audio.set_duration(video.duration)

    final_video = video.set_audio(new_audio)

    final_video.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )


# =====================================
# TRIM VIDEO
# =====================================

def trim_video(video_path, start_time, end_time, output):

    video = VideoFileClip(video_path)

    trimmed = video.subclip(start_time, end_time)

    trimmed = trimmed.without_audio()

    trimmed.write_videofile(
        output,
        codec="libx264",
        audio=False
    )


# =====================================
# ADJUST VIDEO VOLUME
# =====================================

def adjust_video_volume(video_path, volume_level, output):

    video = VideoFileClip(video_path)

    final_video = video.volumex(volume_level)

    final_video.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
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

    main_video = VideoFileClip(main_video_path)

    ad_video = VideoFileClip(ad_video_path)

    duration = main_video.duration

    split_points = []

    for i in range(1, ad_count + 1):

        point = (duration / (ad_count + 1)) * i

        split_points.append(point)

    clips = []

    previous = 0

    for point in split_points:

        part = main_video.subclip(previous, point)

        clips.append(part)

        ad_resized = ad_video.resize(main_video.size)

        ad_resized = ad_resized.set_fps(main_video.fps)

        clips.append(ad_resized)

        previous = point

    last_part = main_video.subclip(previous)

    clips.append(last_part)

    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    final_video.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac",
        fps=main_video.fps
    )
# =====================================
# AUTO CAPTIONS
# =====================================

def add_auto_captions(video_path, output):

    # LOAD WHISPER MODEL
    model = whisper.load_model("base")

    # LOAD VIDEO
    video = VideoFileClip(video_path)

    # EXTRACT AUDIO
    audio_path = "temp/audio.wav"

    video.audio.write_audiofile(audio_path)

    # TRANSCRIBE AUDIO
    result = model.transcribe(audio_path)

    # OPEN VIDEO USING OPENCV
    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    temp_output = "temp/caption_temp.mp4"

    out = cv2.VideoWriter(
        temp_output,
        fourcc,
        fps,
        (width, height)
    )

    frame_number = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        current_time = frame_number / fps

        current_text = ""

        # FIND CURRENT SUBTITLE
        for segment in result["segments"]:

            if segment["start"] <= current_time <= segment["end"]:

                current_text = segment["text"]

                break

        if current_text:

            wrapped_text = textwrap.wrap(
                current_text,
                width=30
            )

            y_position = height - 100

            for line in wrapped_text:

                text_size = cv2.getTextSize(
                    line,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    2
                )[0]

                x = (width - text_size[0]) // 2

                # BLACK BACKGROUND
                cv2.rectangle(
                    frame,
                    (x - 10, y_position - 30),
                    (x + text_size[0] + 10, y_position + 10),
                    (0, 0, 0),
                    -1
                )

                # WHITE TEXT
                cv2.putText(
                    frame,
                    line,
                    (x, y_position),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA
                )

                y_position += 40

        out.write(frame)

        frame_number += 1

    cap.release()
    out.release()

    # ADD ORIGINAL AUDIO BACK
    final_clip = VideoFileClip(temp_output)

    final_clip = final_clip.set_audio(video.audio)

    # EXPORT FINAL VIDEO
    final_clip.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )

