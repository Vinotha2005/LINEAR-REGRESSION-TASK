# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_squared_error
import pickle
import numpy as np

# Load dataset
df = pd.read_csv("Salary_dataset.csv")

# Display first few rows
print("Dataset preview:")
print(df.head())

# Automatically detect feature and target columns
# (assuming columns: YearsExperience, Salary)
X = df[["YearsExperience"]]  # feature
y = df["Salary"]             # target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Ridge Regression
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)

# Evaluate
y_pred = ridge_model.predict(X_test)
print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Save model
with open("salary_model.pkl", "wb") as file:
    pickle.dump(ridge_model, file)

print("✅ Model saved as salary_model.pkl")
