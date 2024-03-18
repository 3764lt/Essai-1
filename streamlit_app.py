import streamlit as st 
import pandas as pd
import numpy as np
voc=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQu7A9rsNdCjubSwgVFXnOZH7CBRXV-iUNVnBKB6HSXuIHhFSdRdPexzHftf8Kx3ViL6e0CoQpK6vtp/pub?output=csv")
l=voc.shape[0]
i=np.random.choice(range(l))
indices=np.ramdom.choices(range(l),h=4,replace=False)
word_fr=voc["Définition"].values[i]
word_pin=voc["Pinyin"].values[i]
word_chi=voc["Hanzi"].values[i]
st.write(word_fr+" "+word_pin+" "+word_chi)
st.button("refresh")
if st.button ("i"):
  st.write("Bravo")
else :
  st.write("mauvaise réponse")




