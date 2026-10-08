import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(random_state=42)

param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [2, 3, 5, None],
    "min_samples_split": [2, 5]
}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("Best Parameters:")
print(grid_search.best_params_)

print("\nBest Cross-Validation Accuracy:")
print(grid_search.best_score_)

results = pd.DataFrame(grid_search.cv_results_)

print("\nTop 5 Parameter Combinations:")
print(
    results[
        ["params", "mean_test_score", "std_test_score"]
    ].sort_values(
        by="mean_test_score",
        ascending=False
    ).head()
)

best_model = grid_search.best_estimator_

predictions = best_model.predict(X_test)

print("\nTest Accuracy:")
print(accuracy_score(y_test, predictions))

print("\nParameter Explanation:")

for parameter, value in grid_search.best_params_.items():
    print(parameter, ":", value)

    if parameter == "n_estimators":
        print("Controls the number of trees in the forest.")

    elif parameter == "max_depth":
        print("Controls tree complexity and may reduce overfitting.")

    elif parameter == "min_samples_split":
        print("Controls the minimum samples required to split a node.")
