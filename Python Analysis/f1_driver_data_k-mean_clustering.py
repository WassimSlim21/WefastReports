import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Suppressing chained assignment warning
pd.options.mode.chained_assignment = None

# Assuming 'dataset' is a pandas DataFrame containing the required data

# Preprocessing the dataset
dataset['Winrate'] = dataset['Winrate'].replace(',', '.')  # Replacing commas with dots in Winrate column
dataset['Winrate'].unique()  # Checking unique values in Winrate column

# Dropping unnecessary columns
x = dataset.drop(['surname', 'forename', 'driverId'], axis=1)

# Replacing NaN values with 0
x = x.replace(np.nan, 0)

# Converting Winrate column to float
x['Winrate'] = x['Winrate'].astype(float)

# Applying KMeans clustering with 2 clusters
kmeans = KMeans(n_clusters=2) 
kmeans.fit(x)

# Applying PCA for dimensionality reduction
pca = PCA(2)
d = pca.fit_transform(x)

# Predicting labels for the data points
label = kmeans.fit_predict(x)

# Plotting the clusters
u_labels = np.unique(label)
for i in u_labels:
    plt.scatter(d[label == i, 0], d[label == i, 1], label=i)

# Plotting the centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='purple', label='centroid')

# Adding labels and legend
plt.xlabel('Nombre de races')
plt.ylabel('Wins')
plt.legend()
plt.show()