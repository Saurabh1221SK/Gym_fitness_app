import pandas as pd
from sklearn.model_selection import train_test_split

# Loading the full dataset
df = pd.read_excel("gym recommendation.xlsx")

# Splitting into 80% training and 20% test data
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Saving the splits to new Excel files
train_df.to_excel("gym_recommendation_train.xlsx", index=False)
test_df.to_excel("gym_recommendation_test.xlsx", index=False)

print("Dataset has been divided and saved as 'gym_recommendation_train.xlsx' and 'gym_recommendation_test.xlsx'.")
