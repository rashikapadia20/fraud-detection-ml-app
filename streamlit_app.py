import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Load model CORRECTLY
# -----------------------------
with open("model.pkl", "rb") as f:
    data = pickle.load(f)

# If model.pkl stores a dict
if isinstance(data, dict):
    model = data["model"]
else:
    model = data

# -----------------------------
# UI
# -----------------------------
st.title("💳 Fraud Detection App")

f1 = st.number_input("Feature 1", value=0.0)
f2 = st.number_input("Feature 2", value=0.0)
f3 = st.number_input("Feature 3", value=0.0)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Check Fraud"):
    try:
        X = np.array([[f1, f2, f3]])
        prediction = model.predict(X)[0]

        if int(prediction) == 1:
            st.error("🚨 Fraud Detected")
        else:
            st.success("✅ Not Fraud")

    except Exception as e:
        st.error(f"Prediction error: {e}")
