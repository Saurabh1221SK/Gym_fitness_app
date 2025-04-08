import streamlit as st

def set_custom_style():
    st.markdown("""
        <style>
        body {
            background-color: #f2f4f7;
        }
        .section {
            background: linear-gradient(to right, #13315c, #2C3E50);
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        .title {
            text-align: center;
            color: #fdf0d5;
            font-size: 40px;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
