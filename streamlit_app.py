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

f1 = st.number_input("Feature 1", value=0.0)
f2 = st.number_input("Feature 2", value=0.0)
f3 = st.number_input("Feature 3", value=0.0)

# --------------------
# 3️⃣ Prediction (HERE!)
# --------------------
if st.button("Check Fraud"):
    X = np.array([[f1, f2, f3]])      # ← PUT HERE
    result = model.predict(X)[0]      # ← PUT HERE

    if result == 1:
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Not Fraud")
