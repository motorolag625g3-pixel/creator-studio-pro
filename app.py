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
        "Full Screen Watermark (Logo)",
        "Text Branding"
    ]
)

# ==============================
# FULL SCREEN WATERMARK
# ==============================
    # ==============================
# CUSTOM TEXT BRANDING
# ==============================

if menu == "Custom Text Branding":

    st.header("📝 Custom Text Branding")

    # upload video
    branding_video = st.file_uploader(
        "Upload Video",
        type=["mp4"]
    )

    # custom user text
    branding_text = st.text_input(
        "Enter Your Branding Text"
    )

    if branding_video and branding_text:

        # SAVE VIDEO
        with open("temp/text_video.mp4", "wb") as f:
            f.write(branding_video.read())

        # BUTTON
        if st.button("Apply Custom Branding"):

            add_text_branding(
                "temp/text_video.mp4",
                branding_text,
                "outputs/custom_text_branding.mp4"
            )

            st.success("Custom Text Branding Added!")

            # SHOW OUTPUT
            st.video("outputs/custom_text_branding.mp4")

            # DOWNLOAD BUTTON
            with open("outputs/custom_text_branding.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="custom_branding.mp4"
                )

        # SAVE VIDEO
        with open("temp/input.mp4", "wb") as f:
            f.write(video.read())

        # SAVE LOGO
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

# ==============================
# TEXT BRANDING
# ==============================

if menu == "Text Branding":

    st.header("📝 Text Branding")

    text_video = st.file_uploader(
        "Upload Video for Text Branding",
        type=["mp4"]
    )

    branding_text = st.text_input(
        "Enter Branding Text"
    )

    if text_video and branding_text:

        # SAVE VIDEO
        with open("temp/text_video.mp4", "wb") as f:
            f.write(text_video.read())

        if st.button("Apply Text Branding"):

            add_text_branding(
                "temp/text_video.mp4",
                branding_text,
                "outputs/text_branding.mp4"
            )

            st.success("Text Branding Added!")

            st.video("outputs/text_branding.mp4")
