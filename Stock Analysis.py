import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
csv_file = '(AAPL.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index for time-based plotting
df.set_index('Date', inplace=True)

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the stock data
ax.plot(df.index, df['Open'], label='Open')
ax.plot(df.index, df['High'], label='High')
ax.plot(df.index, df['Low'], label='Low')
ax.plot(df.index, df['Close'], label='Close')
ax.plot(df.index, df['Adj Close'], label='Adj Close')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Stock Price Trends Over Time')
ax.legend()

# Display the plot
plt.show()
