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

    # Combine video + watermark
    final = CompositeVideoClip([video, logo])

    # Export final video
    final.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )
