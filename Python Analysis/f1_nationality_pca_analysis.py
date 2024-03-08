import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the dataset from an Excel file
df = pd.read_excel('http://localhost:3000/data.xlsx', engine='openpyxl', index_col=0)

# Fill missing values with 0
df = df.fillna(0)

# Display the first 5 rows of the dataset
df.head(n=5)

# Perform PCA (Principal Component Analysis) with 4 components
pca = PCA(n_components=4)
pca.fit(df)

# Explained variance ratio of each principal component
explained_variance = pca.explained_variance_ratio_

# Reduce the dimensionality of the dataset using PCA
X_reduced = pca.transform(df)

# Plot the reduced dataset in a scatter plot
plt.figure(figsize=(18, 6))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1])

# Annotate the scatter plot with labels
for label, x, y in zip(df.index, X_reduced[:, 0], X_reduced[:, 1]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-10, 10),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
plt.title("PCA: Profil d'évolution des wins pour chaque nationalité")
plt.show()