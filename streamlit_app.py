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
if st.button("Check Fraud"):
   X = np.array([[amount, frequency, risk_score]])
     # ← PUT HERE
    result = model.predict(X)[0]      # ← PUT HERE

    if result == 1:
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Not Fraud")
