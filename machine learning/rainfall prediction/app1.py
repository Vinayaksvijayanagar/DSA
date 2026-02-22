import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("rainfall_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Rainfall Prediction", page_icon="🌧️")

st.title("🌧️ Rainfall Prediction System")
st.write("Enter the weather parameters below to predict rainfall.")

# Create Form
with st.form("rainfall_form"):
    temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=1.0)
    pressure = st.number_input("Atmospheric Pressure (hPa)", min_value=800.0, max_value=1100.0, step=0.1)
    wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=200.0, step=0.1)
    cloud_cover = st.slider("Cloud Cover (%)", 0, 100, 50)

    submit = st.form_submit_button("Predict Rainfall")

# Prediction
if submit:
    features = np.array([[temperature, humidity, pressure, wind_speed, cloud_cover]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("🌧️ Rainfall Expected")
    else:
        st.info("☀️ No Rainfall Expected")