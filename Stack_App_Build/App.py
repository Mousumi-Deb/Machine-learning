
import streamlit as st
from Page_predict import predict_page
from Page_explore import explore_page

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    predict_page()
else:
    explore_page()
