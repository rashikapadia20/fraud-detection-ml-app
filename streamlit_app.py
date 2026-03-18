if page == "Transaction Fraud":
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


elif page == "Startup Fraud":
    st.title("🚨 Startup Fraud Detection System")

    startup = st.text_input("Startup Name")
    sector = st.text_input("Sector")
    stage = st.text_input("Funding Stage")

    rev = st.number_input("Revenue (M)", value=1.0)
    val = st.number_input("Valuation (M)", value=100.0)
    growth = st.number_input("Growth %", value=20.0)

    if st.button("Check Fraud"):
        result = predict_data(rev, val, growth)

        if result == 1:
            st.error("🚨 High Risk Startup")
        else:
            st.success("✅ Low Risk Startup")
