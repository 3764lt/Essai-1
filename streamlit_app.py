import streamlit as st 
import pandas as pd
import numpy as np
voc=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQu7A9rsNdCjubSwgVFXnOZH7CBRXV-iUNVnBKB6HSXuIHhFSdRdPexzHftf8Kx3ViL6e0CoQpK6vtp/pub?output=csv")
l=voc.shape[0]
if "indices" in st.session_state :
  indices=st.session_state["indices"]
else :
  indices=np.random.choice(l,size=4,replace=False)
j=np.random.choice(indices)
word_fr=voc["Définition"].values[j]
st.write("Traduis:"+" "+word_fr")
def is_correct(i,j):
  if i==j:
    st.write("Bravo")
    del st.session_state["indices"]
  else:
    st.write("Raté")
    st.session_state["indices"]=indices
col1, col2 = st.columns(2) 
with col1:
    for i in range(2):
        st.button(voc["Hanzi"].values[indices[i]], on_click= is_correct, args=(indices[i],j))
with col2:
    for i in range(2,4):
        st.button(voc["Hanzi"].values[indices[i]], on_click= is_correct, args=(indices[i],j))

st.button("Seconday button")  
#st.button default type is secondary
st.button("Primary button", type="primary")
st.session_state["my_var"]=1
if "my_var" in st.session_state







