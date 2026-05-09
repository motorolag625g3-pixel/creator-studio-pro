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
        "Custom Text Branding"
    ]
)

# =========================================
# FULL SCREEN WATERMARK
# =========================================

if menu == "Full Screen Watermark":

    st.header("🖼️ Full Screen Watermark")

    # VIDEO UPLOAD
    video = st.file_uploader(
        "Upload Video",
        type=["mp4"]
    )

    # LOGO UPLOAD
    logo = st.file_uploader(
        "Upload PNG Logo",
        type=["png"]
    )

    if video and logo:

        # SAVE VIDEO
        with open("temp/input.mp4", "wb") as f:
            f.write(video.read())

        # SAVE LOGO
        with open("temp/logo.png", "wb") as f:
            f.write(logo.read())

        # BUTTON
        if st.button("Apply Watermark"):

            add_logo_fullscreen(
                "temp/input.mp4",
                "temp/logo.png",
                "outputs/logo_output.mp4",
                opacity=0.2
            )

            st.success("Watermark Added Successfully!")

            # SHOW VIDEO
            st.video("outputs/logo_output.mp4")

            # DOWNLOAD BUTTON
            with open("outputs/logo_output.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="watermarked_video.mp4"
                )

# =========================================
# CUSTOM TEXT BRANDING
# =========================================

if menu == "tharuuu":

    st.header("📝 Custom Text Branding")

    # VIDEO UPLOAD
    text_video = st.file_uploader(
        "Upload Video",
        type=["mp4"]
    )

    # USER TEXT INPUT
    branding_text = st.text_input(
        "tharuuu"
    )

    if text_video and branding_text:

        # SAVE VIDEO
        with open("temp/text_video.mp4", "wb") as f:
            f.write(text_video.read())

        # BUTTON
        if st.button("Apply Text Branding"):

            add_text_branding(
                "temp/text_video.mp4",
                branding_text,
                "outputs/text_branding.mp4"
            )

            st.success("Text Branding Added Successfully!")

            # SHOW VIDEO
            st.video("outputs/text_branding.mp4")

            # DOWNLOAD BUTTON
            with open("outputs/text_branding.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="text_branding_video.mp4"
                )
