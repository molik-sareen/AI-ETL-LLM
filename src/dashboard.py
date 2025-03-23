import streamlit as st
import pandas as pd

st.title("AI-Driven ETL Dashboard")

df = pd.read_csv("data/sample_data.csv")
st.write(df.head())

