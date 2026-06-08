import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

# App Title
st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to predict the house price.")

# Input Fields
house_id = st.number_input("House ID", min_value=1, value=1)

area = st.number_input("Area (sq.ft)", min_value=100, value=1000)

bedrooms = st.number_input("Bedrooms", min_value=1, value=2)

bathrooms = st.number_input("Bathrooms", min_value=1, value=1)

floors = st.number_input("Floors", min_value=1, value=1)

year_built = st.number_input(
    "Year Built",
    min_value=1900,
    max_value=2026,
    value=2010
)

# Location Dropdown
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

# Garage Dropdown
garage = st.selectbox(
    "Garage",
    ["No", "Yes"]
)

garage_map = {
    "No": 0,
    "Yes": 1
}

garage_encoded = garage_map[garage]

# Prediction Button
if st.button("Predict Price"):

    features = np.array([[
        house_id,
        area,
        bedrooms,
        bathrooms,
        floors,
        year_built,
        location_encoded,
        condition_encoded,
        garage_encoded
    ]])

    prediction = model.predict(features)

    st.success(
        f"Predicted House Price: ₹ {prediction[0]:,.2f}"
    )
