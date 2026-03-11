import streamlit as st
import joblib
import numpy as np

model = joblib.load('bankruptcy_model_final.pkl')

st.title(" Financial Status Predictor")

st.sidebar.header("Financial Ratios")

# TERE DATA KE PERFECT RANGES
f1  = st.sidebar.number_input("Net Profit/TA",           -0.05,  0.35,  0.10)
f2  = st.sidebar.number_input("Total Liabilities/TA",     0.05,  0.75,  0.40)
f3  = st.sidebar.number_input("Working Capital/TA",      -0.20,  0.50,  0.15)
f4  = st.sidebar.number_input("Current Assets/CL",        0.50,  3.00,  1.80)
f5  = st.sidebar.number_input("EBIT/TA",                 -0.10,  0.35,  0.15)
f6  = st.sidebar.number_input("Sales/TA",                 0.50,  2.00,  1.10)
f7  = st.sidebar.number_input("Equity/TA",                0.20,  0.65,  0.45)
f8  = st.sidebar.number_input("Gross Profit/CL",         -0.10,  1.00,  0.35)
f9  = st.sidebar.number_input("Net Profit/Sales",        -0.15,  0.30,  0.08)
f10 = st.sidebar.number_input("Operating Profit/TA",     -0.10,  0.35,  0.12)
f11 = st.sidebar.number_input("Net Profit/Total Liab",   -0.20,  0.25,  0.05)
f12 = st.sidebar.number_input("Op Profit/TA 2",          -0.10,  0.35,  0.15)
f13 = st.sidebar.number_input("Gross Profit/Sales",       0.00,  0.35,  0.15)
f14 = st.sidebar.number_input("Op Expenses/Total Liab",   0.00,  5.00,  0.50)
f15 = st.sidebar.number_input("Sales/Inventory",          0.50, 10.00,  3.50)

if st.button(" Check Status", use_container_width=True):
    data = np.array([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]])
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.error(" Financially Weak")
    else:
        st.success("Financially Strong")
