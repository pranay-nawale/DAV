import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("crypto_prices.csv")

# Plot
fig = px.line(df, x="Date", y="Close", title="Crypto Price Trend (Plotly)")
fig.show()