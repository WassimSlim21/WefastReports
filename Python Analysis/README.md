# Formula 1 Analysis Scripts

This repository contains a collection of Python scripts for analyzing Formula 1 (F1) data. Each script focuses on a specific aspect of F1 data analysis, ranging from data cleaning and visualization to forecasting and clustering. Below is a brief description of each script along with its functionality.



## Scripts Description

### 1. f1_autocorrelation_analysis.py

- **Functionality**: Perform autocorrelation analysis on F1 points data.
- **Features**:
  - Visualize the original time series.
  - Calculate first differences and seasonal differencing.
  - Generate autocorrelation and partial autocorrelation plots.

### 2. f1_data_cleaning_and_visualization.py

- **Functionality**: Clean and visualize F1 points data.
- **Features**:
  - Rename columns for better readability.
  - Convert date columns to datetime format and set the date column as the index.
  - Plot the original time series.

### 3. f1_driver_data_k-mean_clustering.py

- **Functionality**: Apply K-means clustering to F1 driver data.
- **Features**:
  - Preprocess the dataset by encoding categorical variables and scaling features.
  - Apply K-means clustering with 2 clusters and visualize the clusters using PCA.

### 4. f1_fastest_lap_comparison.py

- **Functionality**: Compare the fastest laps of two F1 drivers in a qualifying session.
- **Features**:
  - Retrieve telemetry data for the fastest laps using FastF1.
  - Plot the telemetry data to compare the speeds of the two drivers.

### 5. f1_fastestlapspeed_classification_with_decision_tree.py

- **Functionality**: Classify F1 drivers based on their fastest lap speeds using a decision tree classifier.
- **Features**:
  - Preprocess the dataset by dropping unnecessary columns and converting data types.
  - Split the dataset into training and testing sets.
  - Train a decision tree classifier and visualize the decision tree.

### 6. f1_gear_shift_analysis.py

- **Functionality**: Analyze gear shifts during the fastest lap of an F1 race session.
- **Features**:
  - Install the required package 'fastf1'.
  - Load telemetry data for the fastest lap using FastF1.
  - Visualize gear shifts during the lap using matplotlib.

### 7. f1_nationality_pca_analysis.py

- **Functionality**: Perform PCA analysis on F1 driver nationality data.
- **Features**:
  - Load the dataset from an Excel file.
  - Fill missing values with 0 and perform PCA with 4 components.
  - Plot the reduced dataset in a scatter plot with annotations.

### 8. f1_point_per_date.py

- **Functionality**: Visualize F1 points data per date.
- **Features**:
  - Rename columns for better readability.
  - Convert date columns to datetime format and set the date column as the index.
  - Plot the original time series.

### 9. f1_points_forecasting.py

- **Functionality**: Forecast F1 points using SARIMA model.
- **Features**:
  - Rename columns for better readability.
  - Convert date columns to datetime format and set the date column as the index.
  - Perform first differences and seasonal differencing.
  - Fit SARIMA model and generate forecasts.

### 10. f1_qualifying_session_analysis.py

- **Functionality**: Analyze the fastest lap times in a qualifying session.
- **Features**:
  - Install the required package 'fastf1'.
  - Load telemetry data for the session using FastF1.
  - Calculate delta lap times compared to the pole lap and plot the results.

### 11. f1_racing_session_analysis.py

- **Functionality**: Analyze the fastest lap times in a racing session.
- **Features**:
  - Install the required package 'fastf1'.
  - Load telemetry data for the session using FastF1.
  - Calculate delta lap times compared to the pole lap and plot the results.

### 12. f1_seasonal_analysis.py

- **Functionality**: Perform seasonal analysis on F1 points data.
- **Features**:
  - Visualize the original time series and perform seasonal differencing.
  - Generate autocorrelation plots to identify seasonal patterns.

### 13. f1_seasonal_autocorrelation.py

- **Functionality**: Perform autocorrelation analysis on seasonal F1 points data.
- **Features**:
  - Visualize the original time series and perform seasonal differencing.
  - Generate autocorrelation and partial autocorrelation plots.

### 14. f1_seasonal_forecasting.py

- **Functionality**: Forecast F1 points using SARIMA model with seasonal differencing.
- **Features**:
  - Visualize the original time series and perform seasonal differencing.
  - Fit SARIMA model and generate forecasts for future dates.


## Libraries Used
The following Python libraries are used in this project:

#### scikit-learn
#### TensorFlow
#### pandas
#### numpy
#### statsmodels
#### matplotlib
#### seaborn
#### fastf1