from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

# Dropping rows with missing values
dataset.dropna(inplace=True)

# Assuming 'dataset' is a pandas DataFrame containing the required data

# Preprocessing the dataset
X = dataset.drop(['rank', 'number', 'time', 'constructorId', 'statusId'], axis=1)  # Drop unnecessary columns
y = dataset[['rank']]  # Target variable

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Convert 'fastestLapSpeed' column to float type
dataset['fastestLapSpeed'] = dataset['fastestLapSpeed'].astype(float)

# Convert features to integer type
X.info()
X = X.astype(int)

# Decision Tree Classifier model initialization and training
Tree = DecisionTreeClassifier(criterion='gini', max_depth=3, min_samples_leaf=1, random_state=0)
Tree.fit(X_train, y_train)

# Visualize the decision tree
from sklearn.tree import plot_tree
plt.figure()
plot_tree(Tree, filled=True)
plt.show()