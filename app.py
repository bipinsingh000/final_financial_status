import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("bankruptcy_model_final.pkl","rb"))

st.title("Financial Status Predictor")

st.subheader("Enter Financial Ratios")

f1 = st.number_input("Net Profit / Total Assets")
f2 = st.number_input("Total Liabilities / Total Assets")
f3 = st.number_input("Working Capital / Total Assets")
f4 = st.number_input("Current Assets / Current Liabilities")
f5 = st.number_input("EBIT / Total Assets")
f6 = st.number_input("Sales / Total Assets")
f7 = st.number_input("Equity / Total Assets")
f8 = st.number_input("Gross Profit / Current Liabilities")
f9 = st.number_input("Net Profit / Sales")
f10 = st.number_input("Operating Profit / Total Assets")
f11 = st.number_input("Net Profit / Total Liabilities")
f12 = st.number_input("Operating Profit / Total Assets 2")
f13 = st.number_input("Gross Profit / Sales")
f14 = st.number_input("Operating Expenses / Total Liabilities")
f15 = st.number_input("Sales / Inventory")

if st.button("Check Financial Status"):
    
    data = np.array([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]])
    
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Financially Weak Company")
    else:
        st.success("Financially Strong Company")
