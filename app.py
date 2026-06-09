import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("house_price_model (4).pkl", "rb"))

st.title("House Price Prediction App")

# ID input
id_value = st.number_input("Id", min_value=1, max_value=2000, value=1)

# Area
area = st.number_input("Area", min_value=500, max_value=10000, value=1800)

# Bedrooms
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)

# Bathrooms
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

# Floors
floors = st.number_input("Floors", min_value=1, max_value=5, value=1)

# Year Built
yearbuilt = st.number_input("Year Built", min_value=1900, max_value=2025, value=2015)

# Location Mapping
location_map = {
    "Downtown": 0,
    "Rural": 1,
    "Suburban": 2,
    "Urban": 3
}

location_text = st.selectbox(
    "Location",
    ["Downtown", "Rural", "Suburban", "Urban"]
)

location = location_map[location_text]

# Condition Mapping
condition_map = {
    "Poor": 0,
    "Fair": 1,
    "Good": 2,
    "Excellent": 3
}

condition_text = st.selectbox(
    "Condition",
    ["Poor", "Fair", "Good", "Excellent"]
)

condition = condition_map[condition_text]

# Garage Mapping
garage_map = {
    "No": 0,
    "Yes": 1
}

garage_text = st.selectbox(
    "Garage",
    ["No", "Yes"]
)

garage = garage_map[garage_text]

# Predict
if st.button("Predict Price"):

    features = np.array([[
        id_value,
        area,
        bedrooms,
        bathrooms,
        floors,
        yearbuilt,
        location,
        condition,
        garage
    ]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹{prediction[0]:,.2f}")