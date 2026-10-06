import pandas as pd
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

depths = [1, 2, 3, 4, 5]

for depth in depths:
    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_accuracy = accuracy_score(y_train, train_predictions)
    test_accuracy = accuracy_score(y_test, test_predictions)

    print("Max Depth:", depth)
    print("Training Accuracy:", train_accuracy)
    print("Testing Accuracy:", test_accuracy)
    print()
