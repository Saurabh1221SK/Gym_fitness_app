import streamlit as st
import pandas as pd
from utils.model_utils import train_models, preprocess_input
from utils.style_utils import set_custom_style

st.set_page_config(page_title="Fitness Recommendations", layout="wide")
set_custom_style()

st.markdown('<div class="title">Fitness Recommendations</div>', unsafe_allow_html=True)

if "user_data" not in st.session_state:
    st.warning("Please fill in your data in the 'User Input' page first.")
    st.stop()

# Loading the model 
models, label_encoders, feature_columns = train_models()

# Preprocessing the user input
input_encoded, bmi, bmi_level = preprocess_input(st.session_state["user_data"], feature_columns)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Calculated Metrics")
st.write(f"**BMI:** {bmi}")
st.write(f"**BMI Level:** {bmi_level}")
st.markdown('</div>', unsafe_allow_html=True)

# Predicting fitness-related outputs
fitness_type = label_encoders["Fitness Type"].inverse_transform(models["Fitness Type"].predict(input_encoded))[0]
exercises = label_encoders["Exercises"].inverse_transform(models["Exercises"].predict(input_encoded))[0]
equipment = label_encoders["Equipment"].inverse_transform(models["Equipment"].predict(input_encoded))[0]

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Your Fitness Recommendations")
st.write(f"**Fitness Type:** {fitness_type}")
st.write(f"**Recommended Exercises:** {exercises}")
st.write(f"**Suggested Equipment:** {equipment}")
st.markdown('</div>', unsafe_allow_html=True)
