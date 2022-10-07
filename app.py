import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from random import *

from st_aggrid import AgGrid

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
df_track = pd.read_csv("data.txt",';')
st.df_track

