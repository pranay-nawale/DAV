install.packages("ggplot2")   # run once
library(ggplot2)

data <- read.csv("crypto_prices.csv")

# Convert Date column to Date format
data$Date <- as.Date(data$Date)

# Plot
ggplot(data, aes(x=Date, y=Close)) +
  geom_line(color="blue") +
  ggtitle("Crypto Price Trend")