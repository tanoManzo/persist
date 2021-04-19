import streamlit as st
import pandas as pd

st.write("""
# Gaetano Manzo  
# Test App
""")

x=st.slider("Select a number")
st.write("You select:",x)