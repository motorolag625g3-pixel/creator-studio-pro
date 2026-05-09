import streamlit as st
import os

from branding_tools import *

# CREATE FOLDERS
os.makedirs("temp", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# PAGE SETTINGS
st.set_page_config(
    page_title="Creator Studio Pro",
    layout="wide"
)

# TITLE
st.title("🎬 Creator Studio Pro")

# SIDEBAR MENU
menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Full Screen Watermark",
        "Custom Text Branding",
        "Add Intro Video",
        "Replace Video Audio",
        "Trim Video"
    ]
)

# =========================================
# FULL SCREEN WATERMARK
# =========================================

if menu == "Full Screen Watermark":

    st.header("🖼️ Full Screen Watermark")

    video = st.file_uploader(
        "Upload Video",
        type=["mp4"],
        key="watermark_video"
    )

    logo = st.file_uploader(
        "Upload PNG Logo",
        type=["png"],
        key="watermark_logo"
    )

    if video and logo:

        with open("temp/input.mp4", "wb") as f:
            f.write(video.read())

        with open("temp/logo.png", "wb") as f:
            f.write(logo.read())

        if st.button("Apply Watermark"):

            add_logo_fullscreen(
                "temp/input.mp4",
                "temp/logo.png",
                "outputs/logo_output.mp4",
                opacity=0.2
            )

            st.success("Watermark Added Successfully!")

            st.video("outputs/logo_output.mp4")

            with open("outputs/logo_output.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="watermarked_video.mp4"
                )

# =========================================
# CUSTOM TEXT BRANDING
# =========================================

if menu == "Custom Text Branding":

    st.header("📝 Custom Text Branding")

    text_video = st.file_uploader(
        "Upload Video",
        type=["mp4"],
        key="text_video"
    )

    branding_text = st.text_input(
        "Enter Your Branding Text"
    )

    if text_video and branding_text:

        with open("temp/text_video.mp4", "wb") as f:
            f.write(text_video.read())

        if st.button("Apply Text Branding"):

            add_text_branding(
                "temp/text_video.mp4",
                branding_text,
                "outputs/text_branding.mp4"
            )

            st.success("Text Branding Added Successfully!")

            st.video("outputs/text_branding.mp4")

            with open("outputs/text_branding.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="text_branding_video.mp4"
                )

# =========================================
# ADD INTRO VIDEO
# =========================================

if menu == "Add Intro Video":

    st.header("🎬 Add Intro Video")

    intro_video = st.file_uploader(
        "Upload Intro Clip",
        type=["mp4"],
        key="intro_video"
    )

    main_video = st.file_uploader(
        "Upload Main Video",
        type=["mp4"],
        key="main_video"
    )

    if intro_video and main_video:

        with open("temp/intro.mp4", "wb") as f:
            f.write(intro_video.read())

        with open("temp/main_video.mp4", "wb") as f:
            f.write(main_video.read())

        if st.button("Generate Final Video"):

            add_intro_video(
                "temp/intro.mp4",
                "temp/main_video.mp4",
                "outputs/final_intro_video.mp4"
            )

            st.success("Intro Added Successfully!")

            st.video("outputs/final_intro_video.mp4")

            with open("outputs/final_intro_video.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="final_intro_video.mp4"
                )

# =========================================
# REPLACE VIDEO AUDIO
# =========================================

if menu == "Replace Video Audio":

    st.header("🎧 Replace Video Audio")

    replace_video = st.file_uploader(
        "Upload Video",
        type=["mp4"],
        key="replace_video"
    )

    replace_audio = st.file_uploader(
        "Upload New Audio",
        type=["mp3", "wav"],
        key="replace_audio"
    )

    if replace_video and replace_audio:

        with open("temp/replace_video.mp4", "wb") as f:
            f.write(replace_video.read())

        with open("temp/new_audio.mp3", "wb") as f:
            f.write(replace_audio.read())

        if st.button("Replace Audio"):

            replace_video_audio(
                "temp/replace_video.mp4",
                "temp/new_audio.mp3",
                "outputs/final_audio_replace.mp4"
            )

            st.success("Audio Replaced Successfully!")

            st.video("outputs/final_audio_replace.mp4")

            with open("outputs/final_audio_replace.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="audio_replaced_video.mp4"
                )

# =========================================
# TRIM VIDEO
# =========================================

if menu == "Trim Video":

    st.header("✂️ Trim Video")

    trim_video_file = st.file_uploader(
        "Upload Video",
        type=["mp4"],
        key="trim_video"
    )

    if trim_video_file:

        with open("temp/trim_video.mp4", "wb") as f:
            f.write(trim_video_file.read())

        start_time = st.number_input(
            "Start Time (seconds)",
            min_value=0,
            value=0
        )

        end_time = st.number_input(
            "End Time (seconds)",
            min_value=1,
            value=10
        )

        if st.button("Trim Video"):

            trim_video(
                "temp/trim_video.mp4",
                start_time,
                end_time,
                "outputs/trimmed_video.mp4"
            )

            st.success("Video Trimmed Successfully!")

            st.video("outputs/trimmed_video.mp4")

            with open("outputs/trimmed_video.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="trimmed_video.mp4"
                )
