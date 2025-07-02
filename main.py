import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("california_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Streamlit UI
st.set_page_config(page_title="California House Price Predictor", layout="centered")
st.title("🏡 California Housing Price Prediction")

st.markdown("Enter the features to predict the house price in **California**.")

# User Inputs
MedInc = st.number_input("Median Income (10k USD)", value=5.0)
HouseAge = st.number_input("House Age (in years)", value=20)
AveRooms = st.number_input("Average Rooms", value=5.0)
AveBedrms = st.number_input("Average Bedrooms", value=1.0)
Population = st.number_input("Population", value=1000)
AveOccup = st.number_input("Average Occupancy", value=3.0)
Latitude = st.number_input("Latitude", value=34.0)
Longitude = st.number_input("Longitude", value=-118.0)

# Predict Button
if st.button("Predict House Price"):
    # Prepare input
    input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    st.success(f"🏠 Estimated House Price: **${prediction * 100000:.2f}**")

