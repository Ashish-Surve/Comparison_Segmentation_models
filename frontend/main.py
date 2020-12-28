import time

import requests
import streamlit as st
from PIL import Image

STYLES = {
    "unet": "U-net-efficientnet",
    "featurepyramidnetwork": "FPN-efficientnet",
    "linknet": "LinkedNet",
}


st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("Image Segmentation Tool")

image = st.file_uploader("Choose an image")

style = st.selectbox("Choose the model", [i for i in STYLES.keys()])

if st.button("Find Car!"):
    if image is not None and style is not None:
        files = {"file": image.getvalue()}
        # DEBUG
        #res = requests.post(f"http://127.0.0.1:8000/{style}", files=files)
        res = requests.post(f"http://backend:8080/{style}", files=files)
        img_path = res.json()
        # DEBUG
        # image_p = r"../backend/"+ img_path.get("name")
        # Docker
        image_p = img_path.get("name")
        image = Image.open(image_p)

        st.image(image)

        displayed_styles = [style]
        displayed = 1
        total = len(STYLES)

