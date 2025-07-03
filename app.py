import streamlit as st
st.set_page_config(page_title="FloraLens", page_icon="🌸", layout="centered")
from PIL import Image
import tensorflow as tf
import numpy as np
import pandas as pd
import json
import geocoder
import os

@st.cache_resource

def load_model():
    class CustomInputLayer(tf.keras.layers.InputLayer):
        @classmethod
        def from_config(cls, config):
            if 'batch_shape' in config:
                config['batch_input_shape'] = config.pop('batch_shape')
            return super().from_config(config)

    try:
        model = tf.keras.models.load_model(
            "flower_model.keras",
            custom_objects={'InputLayer': CustomInputLayer},
            compile=False
        )
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise

model = load_model()

def load_labels():
    with open("data/labels.json") as f:
        return json.load(f)

labels = load_labels()

def load_tips():
    with open('data/tips.json') as f:
        return json.load(f)

tips_db = load_tips()

def classify_image(img: Image.Image) -> str:
    img_resized = img.resize((224, 224))
    x = np.array(img_resized) / 255.0
    x = np.expand_dims(x, 0)
    preds = model.predict(x)
    predicted_idx = np.argmax(preds, axis=1)[0]
    predicted_label = labels[str(predicted_idx)].lower()  
    return predicted_label

def get_location():
    g = geocoder.ip('me')
    return g.latlng if g.ok else None


st.markdown(
    """
    <h1 style='text-align: center; color: #6a1b9a;'>FloraLens</h1>
    <h4 style='text-align: center; color: #444;'>Spring flower classifier with care tips & a community bloom map</h4>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

uploaded = st.file_uploader("Upload a photo of a spring flower", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Your Uploaded Flower", use_container_width=True)

    with st.spinner("Classifying..."):
        flower = classify_image(img)

    if flower:
        st.header(f"I think this is: **{flower.title()}**")

        if flower in tips_db:
            st.success("Care Tips:")
            for tip in tips_db[flower]['tips']:
                st.markdown(f"- {tip}")
            st.info(f"**Ecosystem Fact**: {tips_db[flower]['fact']}")
        else:
            st.warning("No care tips available for this flower.")

        loc = get_location()
        if loc:
            lat, lon = loc
            st.markdown("### Your Flower Sighting Location:")
            st.map(pd.DataFrame([[lat, lon]], columns=['lat', 'lon']), zoom=10)
            df = pd.DataFrame([[flower, lat, lon]], columns=['flower', 'lat', 'lon'])
            mode = 'a' if os.path.exists('sightings.csv') else 'w'
            header = not os.path.exists('sightings.csv')
            df.to_csv('sightings.csv', index=False, mode=mode, header=header)
        else:
            st.error("Could not determine your location. Please enable location services.")

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>Thank you for contributing to FloraLens!</p>", unsafe_allow_html=True)
