import streamlit as st 
import pandas as pd
import numpy as np
voc=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQu7A9rsNdCjubSwgVFXnOZH7CBRXV-iUNVnBKB6HSXuIHhFSdRdPexzHftf8Kx3ViL6e0CoQpK6vtp/pub?output=csv")
l=voc.shape[0]
i=np.random.choice(range(l))
indices=np.ramdom.choice(l,size=4,replace=False)
st.write(indices)
for i in range (4):
  st.button(voc["Hanzi"].values[indices[i]])
    





