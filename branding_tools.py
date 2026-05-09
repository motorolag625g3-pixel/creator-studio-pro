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

def add_text_branding(video_path, text, output):

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
