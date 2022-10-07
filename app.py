import pandas as pd
import streamlit


df_trak = pd.read_csv("data.txt",';')

st.dataframe(df)
