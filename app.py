
import streamlit as st

from branding_tools import *

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

# VIDEO UPLOAD
video = st.file_uploader(
    "Upload Video",
    type=["mp4"]
)

# CHECK VIDEO
if video:

    # SAVE VIDEO
    with open("temp/input.mp4", "wb") as f:
        f.write(video.read())

    st.success("Video Uploaded Successfully")

    # LOGO WATERMARK
    if menu == "Full Screen Watermark (Logo)":

        logo = st.file_uploader(
            "Upload Logo",
            type=["png"]
        )

        if logo:

            # SAVE LOGO
            with open("temp/logo.png", "wb") as f:
                f.write(logo.read())

            # BUTTON
            if st.button("Add Logo Watermark"):
                

                
                
                add_logo_fullscreen(
                    "temp/input.mp4",
                    "temp/logo.png",
                    "outputs/logo_output.mp4",
                 opacity=0.2
                    # TEXT BRANDING FEATURE
elif menu == "Text Branding":

    st.header("📝 Text Branding")

    # upload video
    text_video = st.file_uploader(
        "Upload Video for Text Branding",
        type=["mp4"]
    )

    # text input
    branding_text = st.text_input(
        "Enter Branding Text"
    )

    if text_video and branding_text:

        # save video
        with open("temp/text_video.mp4", "wb") as f:
            f.write(text_video.read())

        # process button
        if st.button("Apply Text Branding"):

            add_text_branding(
                "temp/text_video.mp4",
                branding_text,
                "outputs/text_branding.mp4"
            )

            st.success("Text Branding Added!")

            st.video("outputs/text_branding.mp4")
                    
                )

                st.success("Logo Added Successfully!")

                # SHOW VIDEO
                st.video("outputs/logo_output.mp4")
