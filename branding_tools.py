from moviepy.editor import *

# FULL SCREEN WATERMARK FUNCTION
def add_logo_fullscreen(video_path, logo_path, output, opacity=0.2):

    # Load main video
    video = VideoFileClip(video_path)

    # Create full-screen watermark
    logo = (
        ImageClip(logo_path)
        .set_duration(video.duration)

        # Resize logo to full video size
        .resize((video.w, video.h))

        # Center position
        .set_position(("center", "center"))

        # Watermark visibility (20%)
        .set_opacity(opacity)
    )
    # TEXT BRANDING FUNCTION
from moviepy.editor import *

# FULL SCREEN LOGO WATERMARK
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


# CUSTOM TEXT BRANDING
def add_text_branding(video_path, text, output):

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

        # CENTER OF VIDEO
        .set_position(("center", "center"))

        # 20% visibility
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
        # center text
        .set_position(("center", "center"))

        # transparency
        .set_opacity(0.3)
    )

    final = CompositeVideoClip([video, txt])

    final.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )

    # Combine video + watermark
    final = CompositeVideoClip([video, logo])

    # Export final video
    final.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )
