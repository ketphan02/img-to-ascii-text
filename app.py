import streamlit as st
from process import process, video
from PIL import Image
import time
import tempfile

def image():
    image = st.file_uploader("Select an image to transform", type=".jpg")
    val = st.slider("Select size of image", 50, 250, value=50)

    if val and image:
        image = Image.open(image)
        st.code(
            process(image, width=val),
            language='text'
        )
    elif not image:
        st.info('Upload an image to display')

def vid():
    vid = st.file_uploader("Select a video to transform", type=["mp4", "gif", "mov"])
    val = st.slider("Select size of video", 30, 100, value=40)
    speed = st.slider("Select the FPS of your video", 1, 30, value=12)

    if val and vid and speed:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(vid.read())
        text_frames = video(tfile.name, val)

        writer = st.empty()
        while True:
            for frame in text_frames:
                writer.code(
                    frame,
                    language='text'
                )
                time.sleep(1/speed)
    elif not image:
        st.info('Upload a video to display')

if __name__ == '__main__':
    st.write("""
    # ASCII DRAWING TRANSFORMATIONS
    """)

    options = st.sidebar.selectbox("Select an option", ["Image", "Video"])

    if options == 'Image':
        image()
    elif options == 'Video':
        vid()