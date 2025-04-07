import streamlit as st
from utils.model_utils import train_models, preprocess_input
from utils.style_utils import set_custom_style

st.set_page_config(page_title="Diet Recommendations", layout="wide")
set_custom_style()

st.markdown('<div class="title">Diet Recommendations</div>', unsafe_allow_html=True)

if "user_data" not in st.session_state:
    st.warning("Please fill in your data in the 'User Input' page first.")
    st.stop()

models, label_encoders, feature_columns = train_models()
input_encoded, _, _ = preprocess_input(st.session_state["user_data"], feature_columns)

diet = label_encoders["Diet"].inverse_transform(models["Diet"].predict(input_encoded))[0]
recommendation = label_encoders["Recommendation"].inverse_transform(models["Recommendation"].predict(input_encoded))[0]

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Your Diet Recommendations")
st.write(f"**Diet Plan:** {diet}")
st.write(f"**General Recommendation:** {recommendation}")
st.markdown('</div>', unsafe_allow_html=True)
