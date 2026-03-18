import streamlit as st
import numpy as np
import joblib

# --------------------
# Load model
# --------------------
model = joblib.load("model.pkl")

# --------------------
# Prediction function
# --------------------
def predict_data(a, b, c):
    x = np.array([[a, b, c]])
    prediction = model.predict(x)[0]
    return prediction

# --------------------
# 1️⃣ Fraud Detection UI
# --------------------
st.title("💳 Fraud Detection App")

amount = st.number_input("Transaction Amount", value=0.0)
frequency = st.number_input("Transaction Frequency", value=0.0)
risk_score = st.number_input("Account Risk Score", value=0.0)

if st.button("Predict"):
    result = predict_data(amount, frequency, risk_score)
    
    if result == 1:
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Safe Transaction")

# --------------------
# 2️⃣ Startup Section (Simplified)
# --------------------
st.title("🚨 Startup Fraud Detection System")

startup = st.text_input("Startup Name")
sector = st.text_input("Sector")
stage = st.text_input("Funding Stage")

rev = st.number_input("Revenue (M)", value=1.0)
val = st.number_input("Valuation (M)", value=100.0)
growth = st.number_input("Growth %", value=20.0)
linkedin = st.slider("LinkedIn %", 0, 100, 50)
web = st.slider("Web Reputation", 0, 100, 50)

if st.button("Check Fraud"):
    # Using SAME model (for now simple logic)
    result = predict_data(rev, val, growth)

    st.subheader("Result")

    if result == 1:
        st.error("🚨 High Risk Startup")
    else:
        st.success("✅ Low Risk Startup")
