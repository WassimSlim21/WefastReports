# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
plt.show()