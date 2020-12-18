import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello 
""")

x=st.slider("Select a number")
st.write("You select:",x)