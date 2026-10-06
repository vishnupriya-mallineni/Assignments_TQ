import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

print("Actual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(predictions)

print("\nAccuracy:")
print(accuracy)

print("\nFeature Importance:")
print(importance)

importance.plot(kind="bar")
plt.title("Decision Tree Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()
