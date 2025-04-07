import streamlit as st
from utils.style_utils import set_custom_style

st.set_page_config(page_title="User Input", layout="wide")
set_custom_style()

st.markdown('<div class="title">User Input</div>', unsafe_allow_html=True)

with st.form("user_form"):
    st.markdown('<div class="section">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 15, 80, 32)
        sex = st.selectbox("Sex", ["Male", "Female"])
        height_ft = st.number_input("Height (ft)", min_value=1, max_value=8, value=5)
        height_in = st.number_input("Height (inches)", min_value=0, max_value=11, value=10)
    with col2:
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=57)
        hypertension = st.selectbox("Hypertension", ["No", "Yes"])
        diabetes = st.selectbox("Diabetes", ["No", "Yes"])
        fitness_goal = st.selectbox("Fitness Goal", ['Weight Loss', 'Weight Gain'])
    submit = st.form_submit_button("Submit")
    st.markdown('</div>', unsafe_allow_html=True)

if submit:
    st.session_state["user_data"] = {
        "age": age,
        "sex": sex,
        "height_ft": height_ft,
        "height_in": height_in,
        "weight": weight,
        "hypertension": hypertension,
        "diabetes": diabetes,
        "fitness_goal": fitness_goal
    }
    st.success("Data saved! You can now view your recommendations on the next pages.")
