import streamlit as st
from your_python_file_name import predict   # IMPORTANT

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
    result = predict(startup, sector, stage, rev, val, growth, linkedin, web)

    st.subheader("Result")

    st.write("Risk Score:", result['risk_score'])
    st.write("Risk Level:", result['risk_level'])

    st.write("Justification:")
    for j in result['justification']:
        st.write("•", j)

