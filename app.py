import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data.txt",';')

st.dataframe(df)
st.write(df['type'].value_counts())

st.write(df.groupby('type').size())
st.write(df.groupby('type').count())
df_st1 = df[df['type']=='st1']

st.write(df_st1)
X=df_st1.loc[:,['Nombre séance','dose/seance','Longueur Active La (cm)']]
st.write(X)
y=df_st1.loc[:,['KERMA (cgy cm²)']]
st.write(y)

clf = LogisticRegression(random_state=0).fit(X, y)
predictions  = clf.predict(X[:2, :])
st.write(predictions)


