
import streamlit as st
import joblib
import numpy as np
import pandas as pd

#Load trained model

model = joblib.load("bankruptcy_model_final.pkl")

st.title("Financial Status Predictor")

st.sidebar.header("Financial Ratios")

#Input fields

f1 = st.sidebar.number_input("Net_profit_total_assets", -0.05, 0.35, 0.10)
f2 = st.sidebar.number_input("Total_liabilities_total_assets", 0.05, 0.75, 0.40)
f3 = st.sidebar.number_input("Working_capital_total_assets", -0.20, 0.50, 0.15)
f4 = st.sidebar.number_input("Current_assets_current_liabilities", 0.50, 3.00, 1.80)
f5 = st.sidebar.number_input("EBIT_total_assets", -0.10, 0.35, 0.15)
f6 = st.sidebar.number_input("Sales_total_assets", 0.50, 2.00, 1.10)
f7 = st.sidebar.number_input("Equity_total_assets", 0.20, 0.65, 0.45)
f8 = st.sidebar.number_input("Gross_profit_current_liabilities", -0.10, 1.00, 0.35)
f9 = st.sidebar.number_input("Net_profit_sales", -0.15, 0.30, 0.08)
f10 = st.sidebar.number_input("Operating_profit_total_assets", -0.10, 0.35, 0.12)
f11 = st.sidebar.number_input("Net_profit_total_liabilities", -0.20, 0.25, 0.05)
f12 = st.sidebar.number_input("Operating_profit_total_assets2", -0.10, 0.35, 0.15)
f13 = st.sidebar.number_input("Gross_profit_sales", 0.00, 0.35, 0.15)
f14 = st.sidebar.number_input("Operating_expenses_total_liabilities", 0.00, 5.00, 0.50)
f15 = st.sidebar.number_input("Sales_inventory", 0.50, 10.00, 3.50)

#Prediction button

if st.button("Check Financial Status", use_container_width=True):
    

    data = pd.DataFrame(
        
        
       [[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]],
        
       columns=[
        "Net_profit_total_assets",
        "Total_liabilities_total_assets",
        "Working_capital_total_assets",
        "Current_assets_current_liabilities",
        "EBIT_total_assets",
        "Sales_total_assets",
        "Equity_total_assets",
        "Gross_profit_current_liabilities",
        "Net_profit_sales",
        "Operating_profit_total_assets",
        "Net_profit_total_liabilities",
        "Operating_profit_total_assets2",
        "Gross_profit_sales",
        "Operating_expenses_total_liabilities",
        "Sales_inventory"
    ]
)

prediction = model.predict(data)

if prediction[0] == 1:
    st.error("⚠ Financially Weak Company")
else:
    st.success("✅ Financially Strong Company")
