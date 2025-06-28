import streamlit as st
import pandas as pd

st.title('Streamlit App')

name = st.text_area("Enter your  name: ")
age = st.slider("Select your age:  ", 0,100,25)
st.write(f"Your age is: {age}")

option = ['Python', 'Java', 'C++', 'C']

choice =  st.selectbox("Choose your favorite language", option)
st.write(f'You have selected {choice}')

upload_file = st.file_uploader("choose a CSV file", type='csv')

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)

if name:
    st.write(f"Hello {name}")