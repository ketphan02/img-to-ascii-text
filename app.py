import streamlit as st
from process import process
from PIL import Image

st.write("""
# ASCII DRAWING TRANSFORMATIONS
""")
image = st.file_uploader("Select an image to transform", type=".jpg")
col1, col2 = st.columns([0.2, 1])
val = st.slider("Select size of image", 50, 250, value=50)

if val and image:
    image = Image.open(image)
    st.code(
        process(image, width=val),
        language='text'
    )
    btn = False
elif not image:
    st.info('Upload an image to display')
