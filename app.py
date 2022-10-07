import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from random import *

from st_aggrid import AgGrid

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
df_track = pd.read_csv("data.txt",';')
AgGrid(df_track)


st.title("gestion materiel de curietherapie")
name = st.text_input("Enter your name", '')
st.write(f"Hello {name}!")


#exemple slider
#x = st.slider("Select an integer x", 0, 10, 1)
#y = st.slider("Select an integer y", 0, 10, 1)

#df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
#st.write(df)

x = st.slider("Select an integer x", 0, 4, 1)
n = randrange(0,4,1)
file = open('file.txt', "r")


file2=open('ReferenceMat_001.txt',"r")

#file_ListeMat=open('ListeMat_01.txt',"r")
#st.write(list(file_ListeMat)[0])


df_file3 = pd.read_csv("ReferenceMat_001.txt",';')

file_ListeMat = pd.read_csv("ListeMat_01.txt",';')
st.dataframe(file_ListeMat)
st.dataframe(file_ListeMat.iloc[:,[0,2]])

col1, col2, col3 = st.columns(3)

with col1:
    st.header("test 01")
    st.dataframe(df_file3)

with col2:
   st.dataframe(df_file3.iloc[:,[0,2]])

with col3:
   st.dataframe(df_file3.iloc[:,[5]])


st.dataframe(df_file3)
st.dataframe(df_file3.iloc[:,[0,2]])






choix_01 = st.selectbox("Choix: ", ['Dancing', 'Reading', 'Sports', 'Reading', 'Sports', 'Reading', 'Sports', 'Reading', 'Sports'])
st.write("Your hobby is: ", choix_01)   


st.write("test ecriture")
st.write(list(file)[0])
st.write(list(file2)[0])
st.write("test ecriture")


for line in file:
    #print(line)
    st.write(line)
file.close()


st.title('calcul')


    
    
    
# success
st.success("Success")
 
# success
st.info("Information")
 
# success
st.warning("Warning")
 
# success
st.error("Error")    

    
# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports', 'Reading', 'Sports', 'Reading', 'Sports', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", hobby)    
    
    
# "st.session_state object:", st.session_state

if "df_result" not in st.session_state:
    st.session_state['df_result'] = pd.DataFrame(columns=['h1','h2'])


# st.write(st.session_state)

def onAddRow():
    data = {
            'n°':"something",
            'Denomination baclesse':"something",
            'Reference':'',
            'Denomination fournisseur':'',
            'Fournisseur':'',
            'Quantité':'',
            'Date de commande':'',
            'Date de réception':'',
            
        }
    st.session_state['df_result'] = st.session_state['df_result'].append(data, ignore_index=True)

st.button("Add row", on_click = onAddRow)

#@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')
st.download_button(
    "Press to Download",
    convert_df(st.session_state.df_result),
    "file.csv",
    "text/csv",
    key='download-csv'
)
st.dataframe(st.session_state['df_result'])



