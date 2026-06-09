import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("house_price_model (4).pkl", "rb"))

# Title
st.title("House Price Prediction App")

# Inputs
area = st.number_input("Area", min_value=500, max_value=10000, value=1800)

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)

bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

floors = st.number_input("Floors", min_value=1, max_value=5, value=1)

yearbuilt = st.number_input("Year Built", min_value=1900, max_value=2025, value=2015)

# Location mapping
location_map = {
    "Downtown": 0,
    "Rural": 1,
    "Suburban": 2,
    "Urban": 3
}

# Location dropdown
location_text = st.selectbox(
    "Location",
    ["Downtown", "Rural", "Suburban", "Urban"]
)

# Convert location text to encoded value
location = location_map[location_text]

# Condition mapping
condition_map = {
    "Poor": 0,
    "Fair": 1,
    "Good": 2,
    "Excellent": 3
}

# Condition dropdown
condition_text = st.selectbox(
    "Condition",
    ["Poor", "Fair", "Good", "Excellent"]
)

# Convert condition text to encoded value
condition = condition_map[condition_text]

# Garage mapping
garage_map = {
    "No": 0,
    "Yes": 1
}

# Garage dropdown
garage_text = st.selectbox(
    "Garage",
    ["No", "Yes"]
)

# Convert garage text to encoded value
garage = garage_map[garage_text]

# Predict button
if st.button("Predict Price"):

    features = np.array([[
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