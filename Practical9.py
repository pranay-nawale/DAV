import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("crypto_prices.csv")

# Plot
plt.plot(df["Date"], df["Close"])
plt.title("Crypto Price Trend (Matplotlib)")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.xticks(rotation=45)

plt.show()