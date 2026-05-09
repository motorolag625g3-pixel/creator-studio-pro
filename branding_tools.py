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
def add_text_branding(video_path, text, output):

    video = VideoFileClip(video_path)

    txt = (
        TextClip(
            text,
            fontsize=60,
            color='white',
            font='Arial-Bold'
        )
        .set_duration(video.duration)

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
