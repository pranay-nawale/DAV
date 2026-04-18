import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample dataset (you can replace with CSV later)
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Scores": [40, 50, 60, 70, 80]
}

df = pd.DataFrame(data)

# Independent variable (X) and Dependent variable (y)
X = df[["Hours"]]   # must be 2D
y = df["Scores"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Output
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])

# Plot graph
plt.scatter(X, y, color="blue")      # actual data
plt.plot(X, y_pred, color="red")     # regression line
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.title("Simple Linear Regression")
plt.show()