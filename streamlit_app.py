import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Fraud Detection", layout="centered")

st.title("🚨 Startup Fraud Detection System")

# Load model
model = joblib.load("model.pkl")

st.write("Enter details to check fraud risk")

f1 = st.number_input("Feature 1", value=0.0)
f2 = st.number_input("Feature 2", value=0.0)
f3 = st.number_input("Feature 3", value=0.0)

if st.button("Check Fraud"):
    X = np.array([[f1, f2, f3]])
# Safe prediction handling
try:
    if hasattr(model, "predict"):
        result = model.predict(X)[0]

    elif hasattr(model, "predict_proba"):
        prob = model.predict_proba(X)
        result = 1 if prob[0][1] > 0.5 else 0

    elif isinstance(model, dict) and "model" in model:
        result = model["model"].predict(X)[0]

    else:
        st.error("Unsupported model format")
        st.stop()

    if result == 1:
        st.error("⚠️ Fraud Detected")
    else:
        st.success("✅ Not Fraud")

except Exception as e:
    st.error(f"Prediction error: {e}")

