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
X=df_st1['Nombre séance','dose/seance','Longueur Active La (cm)']
st.write(X)

 # clf = LogisticRegression(random_state=0).fit(X, y)


#>>> X, y = load_iris(return_X_y=True)
#>>> clf = LogisticRegression(random_state=0).fit(X, y)
#v>>> clf.predict(X[:2, :])
#array([0, 0])
#>>> clf.predict_proba(X[:2, :])
#array([[9.8...e-01, 1.8...e-02, 1.4...e-08],
#       [9.7...e-01, 2.8...e-02, ...e-08]])
#>>> clf.score(X, y)
#0.97...
