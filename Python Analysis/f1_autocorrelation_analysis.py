import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm

# Load or define your dataset here

# Cleaning up the data
# Assuming 'dataset' is a pandas DataFrame containing F1 points data

# Rename columns for better readability
dataset.columns = ["date", "points"]

# Convert date column to datetime format
dataset['date'] = pd.to_datetime(dataset['date'], errors='coerce', dayfirst=True)

# Set date column as the index
dataset.set_index('date', inplace=True)

# Plot the original time series
dataset.plot()

# Calculate the first differences of the points scored
dataset['Points First Difference'] = dataset['points'] - dataset['points'].shift(1)

# Seasonal differencing: Calculate the difference between points scored in the current season and the same season of the previous year
dataset['Seasonal First Difference'] = dataset['points'] - dataset['points'].shift(12)

# Plot the seasonal first difference
dataset['Seasonal First Difference'].plot()

# Visualize autocorrelation plot to understand any patterns in the data
autocorrelation_plot(dataset['points'])

# Visualize autocorrelation and partial autocorrelation plots
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dataset['Seasonal First Difference'].iloc[13:], lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dataset['Seasonal First Difference'].iloc[13:], lags=40, ax=ax2)

plt.show()