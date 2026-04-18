import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

# Load dataset
diabetes = load_diabetes()

# Convert to DataFrame
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target

# Features and target
X = df.drop("target", axis=1)
y = df["target"]

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
y_pred = model.predict(X)

# R2 Score
print("R2 Score:", model.score(X, y))

# 📊 Graph: Actual vs Predicted
plt.scatter(y, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted (Multiple Linear Regression)")
plt.show()