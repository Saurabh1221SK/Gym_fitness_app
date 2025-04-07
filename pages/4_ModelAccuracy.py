import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from utils.style_utils import set_custom_style

st.set_page_config(page_title="Model Accuracy", layout="wide")
set_custom_style()

st.markdown('<div class="title">Model Accuracy</div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Evaluating Model Accuracy on Test Dataset")

@st.cache_data
def load_train_data(filepath="gym_recommendation_train.xlsx"):
    df = pd.read_excel(filepath)
    df['BMI'] = df['Weight'] / (df['Height'] ** 2)
    df['Level'] = pd.cut(
        df['BMI'], 
        bins=[0, 18.5, 24.9, 29.9, 100],
        labels=["Underweight", "Normal weight", "Overweight", "Obesity"]
    )
    return df

@st.cache_data
def load_test_data(filepath="gym_recommendation_test.xlsx"):
    df = pd.read_excel(filepath)
    df['BMI'] = df['Weight'] / (df['Height'] ** 2)
    df['Level'] = pd.cut(
        df['BMI'], 
        bins=[0, 18.5, 24.9, 29.9, 100],
        labels=["Underweight", "Normal weight", "Overweight", "Obesity"]
    )
    return df

# Load training data for model building
train_df = load_train_data()

# Define the features and targets
features = ['Sex', 'Age', 'Height', 'Weight', 'Hypertension', 'Diabetes', 'BMI', 'Level', 'Fitness Goal']
targets = ['Fitness Type', 'Exercises', 'Equipment', 'Diet', 'Recommendation']

# One-hot encode training features
X_train = pd.get_dummies(train_df[features])

accuracy_results = {}

# Train separate models on the training dataset, then evaluate on the test dataset.
test_df = load_test_data()
X_test = pd.get_dummies(test_df[features])
# Make sure X_test has the same columns as X_train
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

for target in targets:
    le = LabelEncoder()
    y_train = le.fit_transform(train_df[target])
    y_test = le.fit_transform(test_df[target])
    
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy_results[target] = acc

st.write("The model is trained on the training dataset and evaluated on the test dataset (80/20 split is now replaced by separate files).")
st.markdown("</div>", unsafe_allow_html=True)

for target, acc in accuracy_results.items():
    st.write(f"**{target} Accuracy:** {acc:.2f}")
