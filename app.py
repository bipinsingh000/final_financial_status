import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("bankruptcy_model_final.pkl","rb"))

st.title("Financial Risk Prediction")

value = st.number_input("Enter value")

if st.button("Predict"):
    prediction = model.predict([[value]])
    st.write("Prediction:", prediction)