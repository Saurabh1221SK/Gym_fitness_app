# 🏋️‍♂️ Gym & Fitness Recommender App

Welcome to the Gym & Fitness Recommender — your personal guide to smarter workouts and healthier living! This is a **Streamlit-based web app** that provides personalized fitness recommendations, exercise plans, and diet advice based on your health data and fitness goals. Whether you're aiming to lose weight, gain muscle, or just stay fit, we've got your back.

---

## 💡 What Does It Do?

Based on your inputs (like age, gender, height, weight, and medical history), the app:
- Calculates your **BMI** and classifies your **BMI level**
- Recommends a suitable **Fitness Type**
- Suggests personalized **Exercises**
- Suggests the right **Equipment**
- Generates a diet plan including **vegetables, protein intake, and juices**
- Provides detailed **Health & Wellness Recommendations**

---

## 📊 Model Accuracy

We’ve trained a machine learning model using a labeled dataset of fitness and dietary plans. Here’s how it performs on a **test dataset**:

| Output Category     | Accuracy |
|---------------------|----------|
| Fitness Type        | 100%     |
| Exercises           | 100%     |
| Equipment           | 95%      |
| Diet                | 95%      |
| Recommendation Text | 95%      |

The model is split into **training** and **testing** datasets to ensure reliable performance.

---

## 🛠️ How to Run the App

1. Clone this repo:
   ```bash
   git clone https://github.com/Saurabh1221SK/Gym_fitness_app.git
   cd gym-fitness-recommender
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run Home.py
   ```

---

## 📂 Project Structure

```
├── Home.py                   # Main landing page
├── pages/
│   ├── UserInput.py          # Page to enter user health data
│   ├── FitnessOutput.py      # Fitness recommendations
│   ├── DietOutput.py         # Diet recommendations
│   ├── WorkoutPlans.py       # Custom workout plans
│   └── ModelAccuracy.py      # Model evaluation results
├── train_dataset.xlsx        # Training data
├── test_dataset.xlsx         # Testing data
├── utils                     # Utility functions for prediction
    ├── style_utils.py
    ├── model_utils.py
├── split_datset.py           # splitting the Dataset
└── README.md                 
```

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** for frontend UI
- **Pandas / scikit-learn** for data handling & modeling
- **Excel datasets** for training and testing

---

## 🧪 Sample Input

```json
{
  "age": 27,
  "sex": "Male",
  "height": 6.0,
  "weight": 109,
  "hypertension": "No",
  "diabetes": "Yes",
  "fitness_goal": "Weight Loss"
}
```

🔎 This input leads to:
- BMI: 32.55 (Obese)
- Cardio Fitness
- Exercises: Walking, Yoga, Swimming
- Diet and equipment tailored for weight loss & diabetic management

---

## ✅ Future Improvements

- User login and progress tracking
- Save historical data for users
- Add charts and progress visualization
- Include video links for recommended exercises

---

## 👨‍⚕️ Disclaimer

This app provides general fitness and dietary recommendations. Always consult with your doctor or a registered dietitian before starting any fitness or diet program — especially if you have underlying health conditions.

---
## 🧪 Test the App Live

You can try our Streamlit app here:  
🔗 https://gymfitness.streamlit.app/

---
## 🙌 Thank You!

Thanks for checking out the project! If you found it helpful, feel free to ⭐ star the repo or suggest improvements.

Stay fit and code strong 💪
```
