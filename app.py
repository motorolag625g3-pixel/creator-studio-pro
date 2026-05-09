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
