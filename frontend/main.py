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

st.title("Image Segmentation Tool web app")

image = st.file_uploader("Choose an image")

style = st.selectbox("Choose the model", [i for i in STYLES.keys()])

if st.button("Image Segmentation"):
    if image is not None and style is not None:
        files = {"file": image.getvalue()}
        res = requests.post(f"http://127.0.0.1:8000/{style}", files=files)
        img_path = res.json()
        image = Image.open(img_path.get("name"))
        st.image(image)

        displayed_styles = [style]
        displayed = 1
        total = len(STYLES)

        st.write("Generating other models...")

        while displayed < total:
            for style in STYLES:
                if style not in displayed_styles:
                    try:
                        path = f"{img_path.get('name').split('.')[0]}_{STYLES[style]}.jpg"
                        image = Image.open(path)
                        st.image(image, width=500)
                        time.sleep(1)
                        displayed += 1
                        displayed_styles.append(style)
                    except:
                        pass
