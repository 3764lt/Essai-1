import streamlit as st 
import pandas as pd
import numpy as np
voc=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQu7A9rsNdCjubSwgVFXnOZH7CBRXV-iUNVnBKB6HSXuIHhFSdRdPexzHftf8Kx3ViL6e0CoQpK6vtp/pub?output=csv")
l=voc.shape[0]
indices=np.random.choice(l,size=4,replace=False)
j=np.random.choice(indices)
word_fr=voc["Définition"].values[j]
st.write("Traduis:"+word_fr)
st.write(indices)
def is_correct(i,j):
  if i==j:
    st.write("Bravo")
  else:
    st.write("Raté")
for i in range (4):
  st.button(voc["Hanzi"].values[indices[i]],on_click=is_correct, args=(indices[i],j))





