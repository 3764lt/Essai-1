import streamlit as st 
import pandas as pd
voc=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQu7A9rsNdCjubSwgVFXnOZH7CBRXV-iUNVnBKB6HSXuIHhFSdRdPexzHftf8Kx3ViL6e0CoQpK6vtp/pub?output=csv")
st.dataframe(voc)

