
from moviepy.editor import *

# LOGO WATERMARK
def add_logo(video_path, logo_path, output):

    # Load video
    video = VideoFileClip(video_path)

    # Load logo image
    logo = (
        ImageClip(logo_path)
        .set_duration(video.duration)
        .resize(height=80)
        .set_pos(("right", "bottom"))
        .set_opacity(0.5)
    )

    # Combine video + logo
    final = CompositeVideoClip([video, logo])

    # Save output
    final.write_videofile(output)


# TEXT WATERMARK
def add_text(video_path, text, output):

    # Load video
    video = VideoFileClip(video_path)

    # Create text
    txt = (
        TextClip(
            text,
            fontsize=40,
            color='white'
        )
        .set_duration(video.duration)
        .set_position("center")
    )

    # Combine video + text
    final = CompositeVideoClip([video, txt])

    # Save output
    final.write_videofile(output)
