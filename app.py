import streamlit as st
import pickle



st.title('Movie Recommender System')

options = st.selectbox(
    'How would you like to be contacted?',
    ['Email', 'Home phone', 'Mobile phone'])