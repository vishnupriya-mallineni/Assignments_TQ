import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

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

decision_tree = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

decision_tree.fit(X_train, y_train)
random_forest.fit(X_train, y_train)

dt_predictions = decision_tree.predict(X_test)
rf_predictions = random_forest.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_predictions)
dt_precision = precision_score(y_test, dt_predictions)
dt_recall = recall_score(y_test, dt_predictions)
dt_f1 = f1_score(y_test, dt_predictions)

rf_accuracy = accuracy_score(y_test, rf_predictions)
rf_precision = precision_score(y_test, rf_predictions)
rf_recall = recall_score(y_test, rf_predictions)
rf_f1 = f1_score(y_test, rf_predictions)

results = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [dt_accuracy, rf_accuracy],
    "Precision": [dt_precision, rf_precision],
    "Recall": [dt_recall, rf_recall],
    "F1 Score": [dt_f1, rf_f1]
})

print(results)

if rf_accuracy > dt_accuracy:
    print("\nRandom Forest performs better based on accuracy.")
elif dt_accuracy > rf_accuracy:
    print("\nDecision Tree performs better based on accuracy.")
else:
    print("\nBoth models have the same accuracy.")
