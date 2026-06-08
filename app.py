import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("house_price_model (3).pkl")

st.title("🏠 House Price Prediction")

id_val = st.number_input("Id", min_value=0, value=1)
area = st.number_input("Area", min_value=0, value=1000)
bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Bathrooms", min_value=0, value=2)
floors = st.number_input("Floors", min_value=0, value=1)
yearbuilt = st.number_input("Year Built", min_value=1900, value=2010)
location_text = st.selectbox(
    "Location",
    ["Urban", "Rural", "Suburban"]
)

condition_text = st.selectbox(
    "Condition",
    ["Poor", "Average", "Good"]
)

garage_text = st.selectbox(
    "Garage",
    ["No", "Yes"]
)

garage = 0 if garage_text == "No" else 1
# Convert text to encoded values
location_map = {
    "Urban": 0,
    "Rural": 1,
    "Suburban": 2
}

condition_map = {
    "Poor": 0,
    "Average": 1,
    "Good": 2
}

location = location_map[location_text]
condition = condition_map[condition_text]
if st.button("Predict Price"):
    features = np.array([[id_val, area, bedrooms, bathrooms,
                          floors, yearbuilt, location,
                          condition, garage]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹{prediction[0]:,.2f}")