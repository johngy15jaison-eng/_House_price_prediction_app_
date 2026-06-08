import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction")

id_val = st.number_input("Id", min_value=0, value=1)
area = st.number_input("Area", min_value=0, value=1000)
bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Bathrooms", min_value=0, value=2)
floors = st.number_input("Floors", min_value=0, value=1)
yearbuilt = st.number_input("Year Built", min_value=1900, value=2010)
location = st.selectbox(
    "Location",
    ["Downtown", "Rural", "Suburban", "Urban"]
)

location_map = {
    "Downtown": 0,
    "Rural": 1,
    "Suburban": 2,
    "Urban": 3
}

location_encoded = location_map[location]

# Condition Dropdown
condition = st.selectbox(
    "Condition",
    ["Excellent", "Fair", "Good", "Poor"]
)

condition_map = {
    "Excellent": 0,
    "Fair": 1,
    "Good": 2,
    "Poor": 3
}

condition_encoded = condition_map[condition]

garage = st.number_input("Garage (0 = No, 1 = Yes)", min_value=0, max_value=1, value=0)if st.button("Predict Price"):
    features = np.array([[id_val, area, bedrooms, bathrooms,
                          floors, yearbuilt, location,
                          condition, garage]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹{prediction[0]:,.2f}")