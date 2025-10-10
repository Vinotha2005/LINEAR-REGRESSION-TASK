# app.py
import streamlit as st
import pickle
import numpy as np

# Load model
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="💼 Salary Predictor", page_icon="💰", layout="centered")

st.title("💼 Salary Prediction App")
st.write("Enter years of experience to estimate salary (based on Ridge Regression).")

# Input
years_exp = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, value=2.0, step=0.5)

if st.button("Predict Salary 💰"):
    data = np.array([[years_exp]])
    prediction = model.predict(data)[0]
    st.success(f"Estimated Salary: ₹{prediction:,.2f}")

st.markdown("---")
st.caption("Model: Ridge Regression | Built with Streamlit")
