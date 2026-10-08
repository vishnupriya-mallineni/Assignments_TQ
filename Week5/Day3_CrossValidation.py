import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

print("Accuracy for Each Fold:")
print(scores)

print("\nMean Accuracy:", scores.mean())
print("Standard Deviation:", scores.std())

print("\nMean Accuracy Percentage:", round(scores.mean() * 100, 2), "%")
