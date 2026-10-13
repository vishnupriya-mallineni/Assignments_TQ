from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state = 0
)
k_neighbors = 1
knn = KNeighborsClassifier(n_neighbors = k_neighbors)
knn.fit(X_train, y_train)

True_Positive = 0
True_Negative = 0
False_Positive = 0
False_Negative = 0

y_pred = knn.predict(X_test)
x_pred = np.array(y_pred)
x_test = np.array(y_test)
y_test = np.array(y_test)
for i in range(len(y_test)):
  True_Positive = True_Positive + 1 if x_pred[i] == x_test[i] and x_pred[i] == 1 else True_Positive
  True_Negative = True_Negative + 1 if x_pred[i] == x_test[i] and x_pred[i] == 0 else True_Negative
  False_Positive = False_Positive + 1 if x_pred[i] != x_test[i] and x_pred[i] == 1 else False_Positive
  False_Negative = False_Negative + 1 if x_pred[i] != x_test[i] and x_pred[i] == 0 else False_Negative

Accuracy = True_Positive + True_Negative / (True_Positive + True_Negative + False_Positive + False_Negative)
Precision = True_Positive / (True_Positive + False_Positive)
Recall = True_Positive / (True_Positive + False_Negative)

print("Accuracy: ", Accuracy)
print("Precision: ", Precision)
print("Recall: ", Recall)
print("True Positive: ", True_Positive)
print("True Negative: ", True_Negative)
print("False Positive: ", False_Positive)
print("False Negative: ", False_Negative)


