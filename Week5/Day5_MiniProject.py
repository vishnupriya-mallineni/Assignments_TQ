import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 6, 9,
                      3, 5, 7, 10, 1, 8, 4, 6, 9, 2, 5, 7],
    "Attendance": [45, 50, 60, 65, 70, 75, 80, 90, 55, 68, 78, 95,
                   58, 72, 85, 98, 48, 88, 63, 82, 92, 52, 74, 86],
    "Previous_Marks": [30, 35, 42, 48, 55, 62, 70, 82, 38, 50, 65, 88,
                       40, 58, 75, 95, 32, 80, 46, 68, 90, 36, 60, 78],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1,
             0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

df.to_csv("student_performance.csv", index=False)

print("Dataset:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

X = df[["Hours_Studied", "Attendance", "Previous_Marks"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

results = []

for name, model in models.items():
    if name == "Logistic Regression":
        model.fit(X_train_scaled, y_train)
        predictions = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, predictions),
        "Precision": precision_score(y_test, predictions, zero_division=0),
        "Recall": recall_score(y_test, predictions, zero_division=0),
        "F1 Score": f1_score(y_test, predictions, zero_division=0)
    })

comparison = pd.DataFrame(results)

comparison = comparison.sort_values(
    by=["F1 Score", "Accuracy"],
    ascending=False
)

print("\nModel Comparison:")
print(comparison.to_string(index=False))

best_model = comparison.iloc[0]["Model"]

print("\nBest Model:", best_model)

comparison.to_csv("model_comparison.csv", index=False)
