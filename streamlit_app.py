import streamlit as st 
import pandas as pd
import numpy as np
voc=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQu7A9rsNdCjubSwgVFXnOZH7CBRXV-iUNVnBKB6HSXuIHhFSdRdPexzHftf8Kx3ViL6e0CoQpK6vtp/pub?output=csv")
st.dataframe(voc)
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr=voc["Définition"].value[i]
word_chi=voc["hanzi"].values[i]
st.write(word_fr+""+word_chi)

