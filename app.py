import streamlit as st
import pickle
import numpy as np

# Load Model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict the price.")

# Inputs
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

# Location
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

# Condition
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

# Garage
garage = st.selectbox(
    "Garage",
    ["No", "Yes"]
)

garage_map = {
    "No": 0,
    "Yes": 1
}

# Predict
if st.button("Predict Price"):

    features = np.array([[
        house_id,
        area,
        bedrooms,
        bathrooms,
        floors,
        year_built,
        location_map[location],
        condition_map[condition],
        garage_map[garage]
    ]])

    prediction = model.predict(features)

    st.success(
        f"Predicted House Price: ₹ {prediction[0]:,.2f}"
    )