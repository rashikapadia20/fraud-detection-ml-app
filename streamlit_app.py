import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

# --------------------
# 1️⃣ Train the model
# --------------------
X_train = np.array([
    [0.1, 0.2, 0.1],
    [2.0, 2.1, 2.2],
    [0.3, 0.1, 0.2],
    [3.0, 3.2, 3.1]
])

y_train = np.array([0, 1, 0, 1])

model = LogisticRegression()
model.fit(X_train, y_train)

# --------------------
# 2️⃣ App UI
# --------------------
st.title("💳 Fraud Detection App")

amount = st.number_input("Transaction Amount", value=0.0)
frequency = st.number_input("Transaction Frequency", value=0.0)
risk_score = st.number_input("Account Risk Score", value=0.0)

# --------------------
# 3️⃣ Prediction (HERE!)
# --------------------
from app import predict_data  # IMPORTANT

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
    X = np.array([[amount, frequency, risk_score]])
    result = model.predict(X)[0]
    result = predict(startup, sector, stage, rev, val, growth, linkedin, web)

    st.subheader("Result")

    st.write("Risk Score:", result['risk_score'])
    st.write("Risk Level:", result['risk_level'])

    if result == 1:
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Not Fraud")
    st.write("Justification:")
    for j in result['justification']:
        st.write("•", j)
