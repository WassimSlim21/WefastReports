# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
dataset['Seasonal First Difference'] = dataset['points'] - dataset['points'].shift(24)

# Plot the seasonal first difference
dataset['Seasonal First Difference'].plot()

# Visualize autocorrelation plot to understand any patterns in the data
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(dataset['points'])

# Fit SARIMA model to the dataset
# SARIMA model parameters are chosen as (1, 1, 1) for non-seasonal part and (1, 1, 1, 12) for seasonal part
model = sm.tsa.statespace.SARIMAX(dataset['points'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# Generate forecast using the SARIMA model
dataset['forecast'] = results.predict(start=80, end=100, dynamic=True)

# Plot actual points and forecasted points
dataset[['points', 'forecast']].plot()

plt.show()