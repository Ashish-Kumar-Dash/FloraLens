# 🌸 FloraLens

**FloraLens** is a smart and intuitive Streamlit app that identifies spring flowers using deep learning, shares personalized care tips, and maps your flower sightings — blending AI and nature into a delightful experience.

---

## Project Overview

### The Problem

Many nature enthusiasts, gardeners, and casual explorers struggle to identify wildflowers and understand how to care for them. Traditional plant identification apps often lack contextual insights or location mapping for ecological contribution.

### The Solution

FloraLens leverages a deep learning model fine-tuned on the Oxford 102 Flower Dataset to identify flowers in real-time. It provides care instructions, ecological facts, and community-driven bloom mapping — all in a seamless web app.

### The Impact

- **Democratizing Botany**: Makes plant science accessible to anyone with a smartphone or computer.
- **Community Collaboration**: Encourages citizen science by allowing users to contribute their flower sightings.
- **Ecological Awareness**: Promotes understanding of biodiversity and sustainable gardening practices.

---

## Features

- **AI-Powered Flower Identification**  
  Classifies 102 flower species using a retrained MobileNetV2 model fine-tuned on the Oxford Flowers 102 dataset.

- **Tailored Care Tips & Ecosystem Facts**  
  Learn how to grow, water, and care for each flower, along with fun ecological insights from `data/tips.json`.

- **Community Bloom Mapper**  
  Automatically geolocates users via IP and pins their flower sighting on an interactive Streamlit map.

- **Sightings Tracker**  
  All sightings are appended to `sightings.csv` for future analysis, trends, or community contributions.

---

## Privacy & Permissions

> **Note:** The app requests your approximate location via IP geolocation _only_ to place a map pin for your sighting. No precise GPS data or personal information is stored.

## Setup & Run

1. **Clone the repo**
   ```bash
   git clone FloraLens
   cd flowermapper
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Project Structure

floralens/
│
├── app.py — Main Streamlit app
├── requirements.txt — Python dependencies
├── flower_model.keras — Trained flower classification model
├── sightings.csv — Appended sightings data (optional)
├── data/
│   ├── labels.json — Class ID to flower name
│   └── tips.json — Tips and facts for each flower
├── Oxford102_Flower_Classifier.ipynb — Jupyter notebook for training dataset
└── README.md — Project documentation

Built with ❤️ using TensorFlow, Streamlit, and Oxford Flowers 102.
Crafted to encourage curiosity, conservation, and community.

---

Happy blooming!
