import pandas as pd
import streamlit


df = pd.read_csv("data.txt",';')

st.dataframe(df)
