
import streamlit as st
import joblib
import numpy as np
import pandas as pd

#Load trained model

model = joblib.load("bankruptcy_model_final.pkl")

st.title("Financial Status Predictor")

st.sidebar.header("Financial Ratios")

#Input fields

f1 = st.sidebar.number_input("Net_profit_total_assets" )
f2 = st.sidebar.number_input("Total_liabilities_total_assets")
f3 = st.sidebar.number_input("EBIT_total_assets")
f4 = st.sidebar.number_input("Sales_total_assets")
f5 = st.sidebar.number_input("Gross_profit_current_liabilities")
f6 = st.sidebar.number_input("Net_profit_total_liabilities")
f7 = st.sidebar.number_input("Operating_profit_total_assets")
f8 = st.sidebar.number_input("Sales_inventory")

#Prediction button
#Prediction button

if st.button("Check Financial Status", use_container_width=True):

    data = pd.DataFrame(
        [[f1,f2,f3,f4,f5,f6,f7,f8]],
        columns=[
            "Net_profit_total_assets",
            "Total_liabilities_total_assets",
            "EBIT_total_assets",
            "Sales_total_assets",
            "Gross_profit_current_liabilities",
            "Net_profit_total_liabilities",
            "Operating_profit_total_assets2",
            "Sales_inventory"
        ]
    )

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠ Financially Weak Company")
    else:
        st.success("✅ Financially Strong Company")

