import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load dataset
df = pd.read_csv("crypto_prices.csv", parse_dates=["Date"])
df.set_index("Date", inplace=True)

# Use closing price
data = df["Close"]

# Plot original data
plt.plot(data)
plt.title("Original Time Series")
plt.show()

# Build ARIMA model (p=1, d=1, q=1)
model = ARIMA(data, order=(1,1,1))
model_fit = model.fit()

# Summary
print(model_fit.summary())

# Forecast next 5 days
forecast = model_fit.forecast(steps=5)
print("\nForecasted Values:")
print(forecast)

# Plot forecast
plt.plot(data, label="Original")
plt.plot(forecast, label="Forecast", color="red")
plt.legend()
plt.title("ARIMA Forecast")
plt.show()