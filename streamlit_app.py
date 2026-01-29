import streamlit as st
import numpy as np

# Fake rule-based "model" (temporary)
def predict_fraud(x):
    # simple logic: large values → fraud
    if x.sum() > 3:
        return 1
    return 0

st.title("💳 Fraud Detection App")

f1 = st.number_input("Feature 1", value=0.0)
f2 = st.number_input("Feature 2", value=0.0)
f3 = st.number_input("Feature 3", value=0.0)

if st.button("Check Fraud"):
    X = np.array([f1, f2, f3])
    result = predict_fraud(X)

    if result == 1:
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Not Fraud")
