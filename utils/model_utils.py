import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import streamlit as st

@st.cache_resource
def train_models(train_filepath="gym_recommendation_train.xlsx"):
    # Load training data from Excel file
    df = pd.read_excel(train_filepath)
    
    # Compute BMI and BMI Level
    df['BMI'] = df['Weight'] / (df['Height'] ** 2)
    df['Level'] = pd.cut(
        df['BMI'],
        bins=[0, 18.5, 24.9, 29.9, 100],
        labels=["Underweight", "Normal weight", "Overweight", "Obesity"]
    )
    
    # Use only the required features for training
    features = ['Sex', 'Age', 'Height', 'Weight', 'Hypertension', 'Diabetes', 'BMI', 'Level', 'Fitness Goal']
    targets = ['Fitness Type', 'Exercises', 'Equipment', 'Diet', 'Recommendation']
    
    # One-hot encode features
    X = pd.get_dummies(df[features])
    
    models = {}
    label_encoders = {}
    
    for target in targets:
        le = LabelEncoder()
        y_encoded = le.fit_transform(df[target])
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X, y_encoded)
        models[target] = clf
        label_encoders[target] = le
        
    return models, label_encoders, X.columns

def preprocess_input(user_data, feature_columns):
    # Convert height from feet and inches to meters
    height_m = ((user_data['height_ft'] * 12) + user_data['height_in']) * 0.0254
    bmi = round(user_data['weight'] / (height_m ** 2), 2)
    
    # Determine BMI Level
    if bmi < 18.5:
        level = "Underweight"
    elif bmi < 25:
        level = "Normal weight"
    elif bmi < 30:
        level = "Overweight"
    else:
        level = "Obesity"
        
    input_df = pd.DataFrame([{
        "Sex": user_data["sex"],
        "Age": user_data["age"],
        "Height": height_m,
        "Weight": user_data["weight"],
        "Hypertension": user_data["hypertension"],
        "Diabetes": user_data["diabetes"],
        "Fitness Goal": user_data["fitness_goal"],
        "BMI": bmi,
        "Level": level
    }])
    
    # One-hot encode and align columns with training features
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)
    
    return input_encoded, bmi, level
