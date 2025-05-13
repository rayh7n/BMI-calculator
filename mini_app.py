import streamlit as st
import pandas as pd

st.title("simple BMI calculator")

height=st.number_input("enter your height (in cm):")
weight=st.number_input("enter your wight (in kg):")

if st.button("calculate BMI"):
    bmi=weight/((height/100)**2)
    st.write(f"your BMI is:{bmi:.2f}")