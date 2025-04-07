import streamlit as st
from utils.style_utils import set_custom_style

st.set_page_config(page_title="Gym & Fitness Recommender", layout="wide")
set_custom_style()

st.markdown('<div class="title">Gym & Fitness Recommender</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <h3>Welcome!</h3>
    <p>This app gives you personalized fitness and diet recommendations based on your health data.</p>
    <p>Use the sidebar to navigate between pages: enter your data, view fitness/diet outputs, and check model accuracy.</p>
</div>
""", unsafe_allow_html=True)
