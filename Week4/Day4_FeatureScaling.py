import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score

data = {
    "Hours_Studied": [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10],
    "Attendance": [50, 55, 60, 62, 68, 72, 75, 80, 85, 88, 92, 95],
    "Pass": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy_without_scaling = accuracy_score(y_test, predictions)

standard_scaler = StandardScaler()

X_train_standard = standard_scaler.fit_transform(X_train)
X_test_standard = standard_scaler.transform(X_test)

model.fit(X_train_standard, y_train)

standard_predictions = model.predict(X_test_standard)
standard_accuracy = accuracy_score(y_test, standard_predictions)

minmax_scaler = MinMaxScaler()

X_train_minmax = minmax_scaler.fit_transform(X_train)
X_test_minmax = minmax_scaler.transform(X_test)

model.fit(X_train_minmax, y_train)

minmax_predictions = model.predict(X_test_minmax)
minmax_accuracy = accuracy_score(y_test, minmax_predictions)

print("Accuracy Without Scaling:", accuracy_without_scaling)
print("Accuracy With StandardScaler:", standard_accuracy)
print("Accuracy With MinMaxScaler:", minmax_accuracy)
