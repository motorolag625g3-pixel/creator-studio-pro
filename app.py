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
        "Trim Video",
        "Adjust Video Volume",
        "Insert Advertisements",
        "Auto Captions"
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

# =========================================
# ADJUST VIDEO VOLUME
# =========================================

if menu == "Adjust Video Volume":

    st.header("🎚️ Adjust Video Volume")

    volume_video = st.file_uploader(
        "Upload Video",
        type=["mp4"],
        key="volume_video"
    )

    if volume_video:

        with open("temp/volume_video.mp4", "wb") as f:
            f.write(volume_video.read())

        volume_level = st.slider(
            "Select Volume Level",
            min_value=0.0,
            max_value=3.0,
            value=1.0,
            step=0.1
        )

        st.write(f"Current Volume: {volume_level}x")

        if st.button("Apply Volume Change"):

            adjust_video_volume(
                "temp/volume_video.mp4",
                volume_level,
                "outputs/volume_output.mp4"
            )

            st.success("Volume Updated Successfully!")

            st.video("outputs/volume_output.mp4")

            with open("outputs/volume_output.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="volume_adjusted_video.mp4"
                )

# =========================================
# INSERT ADVERTISEMENTS
# =========================================

if menu == "Insert Advertisements":

    st.header("📢 Insert Advertisements")

    main_video = st.file_uploader(
        "Upload Main Video",
        type=["mp4"],
        key="main_ad_video"
    )

    ad_video = st.file_uploader(
        "Upload Advertisement Video",
        type=["mp4"],
        key="advertisement_video"
    )

    ad_count = st.number_input(
        "Number of Advertisements",
        min_value=1,
        max_value=10,
        value=1
    )

    if main_video and ad_video:

        with open("temp/main_ad_video.mp4", "wb") as f:
            f.write(main_video.read())

        with open("temp/ad_video.mp4", "wb") as f:
            f.write(ad_video.read())

        if st.button("Insert Advertisements"):

            insert_advertisements(
                "temp/main_ad_video.mp4",
                "temp/ad_video.mp4",
                ad_count,
                "outputs/final_ad_video.mp4"
            )

            st.success("Advertisements Added Successfully!")

            st.video("outputs/final_ad_video.mp4")

            with open("outputs/final_ad_video.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="advertisement_video.mp4"
                )

# =========================================
# AUTO CAPTIONS
# =========================================

if menu == "Auto Captions":

    st.header("📝 Automatic Video Captions")

    caption_video = st.file_uploader(
        "Upload English Video",
        type=["mp4"],
        key="caption_video"
    )

    if caption_video:

        with open("temp/caption_video.mp4", "wb") as f:
            f.write(caption_video.read())

        if st.button("Generate Captions"):

            add_auto_captions(
                "temp/caption_video.mp4",
                "outputs/caption_video.mp4"
            )

            st.success("Captions Added Successfully!")

            st.video("outputs/caption_video.mp4")

            with open("outputs/caption_video.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="caption_video.mp4"
                )
