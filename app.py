
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
        "Logo Watermark",
        "Text Watermark"
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
    if menu == "Logo Watermark":

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

                add_logo(
                    "temp/input.mp4",
                    "temp/logo.png",
                    "outputs/logo_output.mp4"
                )

                st.success("Logo Added Successfully!")

                # SHOW VIDEO
                st.video("outputs/logo_output.mp4")
