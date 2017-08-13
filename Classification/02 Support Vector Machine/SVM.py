# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:58:52 2017

@author: Eng.Alla Khaled
"""

# Support Vextor Macine (SVM)

# import dependencies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import dataset
dataset = pd.read_csv("Social_network_Ads.csv")
x = dataset.iloc[:, [2,3]].values 
y = dataset.iloc[:,4].values

# splitting data into training and test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, train_size=0.75,  random_state= 0)

# Feature scaling using [standaralization = (x-mean(x)/ SD(x)) or Normalization = (x-min(x))/ max(x)-min(x)]
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

# Fitting the classifier to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0) # To use linear kernel, put kernel = 'linear' AND to use gaussian kernel, put kernel = 'rbf'
classifier.fit(x_train, y_train)

# Predicting the test set results
y_pred = classifier.predict(x_test)

# Compute the Confusion matrix (Classifier Evaluation)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
""" TN = 66, FP = 2, FN = 8, TP = 24 For a Linear Kernel"""
""" TN = 64, FP = 4, FN = 3, TP = 29 For a Gaussian kernel"""

# Calculate the Logistic regression Accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, y_pred)*100   # 90% , will obtain 93% for a gaussian kernel

# Visualising the Training set results
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
X1, X2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j, edgecolors = 'black')
plt.title('SVM (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
X1, X2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j, edgecolors = 'black')
plt.title('SVM (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
