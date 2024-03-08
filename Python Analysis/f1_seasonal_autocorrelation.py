import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# raise Exception(dataset.head())
## Cleaning up the data
dataset.columns=["date","points"]
dataset['date']=pd.to_datetime(dataset['date'], errors='coerce', dayfirst = True)
dataset.set_index('date',inplace=True)
dataset.plot()

dataset['Points First Difference'] = dataset['points'] - dataset['points'].shift(1)
dataset['points'].shift(1)

dataset['Seasonal First Difference']=dataset['points']-dataset['points'].shift(12)

## Again test dickey fuller test
dataset['Seasonal First Difference'].plot()

from pandas.plotting import autocorrelation_plot
autocorrelation_plot(dataset['points'])

from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import statsmodels.api as sm
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dataset['Seasonal First Difference'].iloc[13:],lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dataset['Seasonal First Difference'].iloc[13:],lags=40,ax=ax2)
plt.show()





