# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the F1 points dataset
# Replace 'dataset' with the actual name of your dataset variable
# Assuming 'dataset' is a pandas DataFrame containing F1 points data
# If you want to load a dataset, you should add the corresponding code here

# Cleaning up the data
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
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(dataset['points'])
plt.show()