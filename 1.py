import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Specify the target stock ticker (Amazon in this case)
ticker = "AMZN"

# Download historical data for the specified stock ticker over a 7-day period
data = yf.download(ticker, period='1y', interval="1d")

# Create a DataFrame and remove the 'Volume' column for simplicity
df = data.drop("Volume", axis=1)

# Plot the stock price data
df['Adj Close'].plot(figsize=(10, 6))
plt.title(f"{ticker} Stock Price Over the Last 7 Days")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid()
plt.show()
