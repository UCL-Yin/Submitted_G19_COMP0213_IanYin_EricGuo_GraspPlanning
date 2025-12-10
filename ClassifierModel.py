import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression  
from sklearn.metrics import accuracy_score, classification_report
import joblib
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
data_path = os.path.join(parent_dir,"data", "2FingerGripper_cube","2FingerGripper_cube_Total.csv")

df = pd.read_csv(data_path)   # my dataset csv

# 2. Features and labels
X = df[['x','y','z','pitch','yaw']]     # Input: 5 features
y = df["success"]           # output: success label

# Alternative model: Random Forest
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )
# 
# model = RandomForestClassifier(
#     n_estimators=200,
#     max_depth=10,
#     random_state=42
# )
# model.fit(X_train, y_train)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)
# training model
y_pred = model.predict(X_test)

# Alternative model: Random Forest
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )
# 
# model = RandomForestClassifier(
#     n_estimators=200,
#     max_depth=10,
#     random_state=42
# )
# model.fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


joblib.dump(model, "Grasp2_BLOCK_classifier_2.pkl")
print("The model has been saved as: Grasp2_BLOCK_classifier_2.pkl")