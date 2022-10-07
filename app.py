import pandas as pd
import streamlit as st


df = pd.read_csv("data.txt",';')

st.dataframe(df)
