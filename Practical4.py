import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("crypto_prices.csv", parse_dates=["Date"])
df.set_index("Date", inplace=True)

print(df.head())

plt.plot(df.index, df["Close"])
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Cryptocurrency Price Over Time")
plt.show()

# 7-day moving average
df["MA7"] = df["Close"].rolling(window=7).mean()

# Plot
plt.plot(df.index, df["Close"], label="Original Price")
plt.plot(df.index, df["MA7"], label="7-Day Moving Avg")

plt.legend()
plt.title("Crypto Price with Moving Average")
plt.show()

df_last = df.tail(30)

plt.plot(df_last.index, df_last["Close"])
plt.title("Last 30 Days Price Trend")
plt.show()