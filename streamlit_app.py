import streamlit as st
import numpy as np

# Fake rule-based "model" (temporary)
from sklearn.linear_model import LogisticRegression

# -----------------------------
# Train real ML model in-app
# -----------------------------
X_train = np.array([
    [0.1, 0.2, 0.1],
    [2.0, 2.1, 2.2],
    [0.3, 0.1, 0.2],
    [3.0, 3.2, 3.1],
    [0.2, 0.4, 0.3],
    [4.0, 4.1, 4.2]
])

y_train = np.array([0, 1, 0, 1, 0, 1])

model = LogisticRegression()
model.fit(X_train, y_train)

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
