import streamlit as st
import pickle
import pandas as pd

# Load trained pipeline
model = pickle.load(open("models/final_xgboost_model.pkl", "rb"))

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="wide")

# Header Section
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🏠 House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter the house details below to predict the price</p>", unsafe_allow_html=True)
st.markdown("---")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏡 Basic Information")
    bedrooms = st.number_input("No of bedrooms", min_value=0)
    bathrooms = st.number_input("No of bathrooms", min_value=0)
    floors = st.number_input("No of floors", min_value=0)
    condition = st.number_input("House condition", min_value=0)
    grade = st.number_input("House grade", min_value=0)
    waterfront = st.selectbox("Waterfront present", [0, 1])
    views = st.number_input("No of views", min_value=0)

with col2:
    st.subheader("📏 Area & Location Details")
    living_area = st.number_input("Living area (sqft)", min_value=0)
    total_floor_area = st.number_input("Total floor area", min_value=0)
    total_lot_area = st.number_input("Total lot area", min_value=0)
    living_area_renov = st.number_input("Living area renovation")
    built_year = st.number_input("Built Year", min_value=1900, max_value=2026)
    renov_year = st.number_input("Renovation Year", min_value=0)
    lat = st.number_input("Lattitude")
    long = st.number_input("Longitude")

st.markdown("---")

# Prediction Button Centered
if st.button("💰 Predict House Price"):

    input_data = pd.DataFrame({
        'No of bedrooms': [bedrooms],
        'No of bathrooms': [bathrooms],
        'living area': [living_area],
        'No of floors': [floors],
        'waterfront present': [waterfront],
        'No of views': [views],
        'house condition': [condition],
        'house grade': [grade],
        'Built Year': [built_year],
        'Renovation Year': [renov_year],
        'Lattitude': [lat],
        'Longitude': [long],
        'living_area_renov': [living_area_renov],
        'Total floor area': [total_floor_area],
        'Total lot area': [total_lot_area]
    })

    prediction = model.predict(input_data)

    st.markdown(
        f"""
        <div style='background-color:#D5F5E3;padding:20px;border-radius:10px;text-align:center;'>
            <h2 style='color:#1E8449;'>Predicted Price: {prediction[0]:,.2f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
