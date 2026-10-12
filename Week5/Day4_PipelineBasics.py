import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "Age": [22, 25, 28, None, 35, 40, 30, 27, 45, 32, 38, 29],
    "Salary": [25000, 30000, None, 40000, 50000, 60000,
               35000, 32000, 70000, None, 55000, 38000],
    "Department": ["IT", "HR", "Sales", "IT", None, "HR",
                   "Sales", "IT", "Sales", "HR", "IT", "Sales"],
    "Purchased": [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

numeric_features = ["Age", "Salary"]
categorical_features = ["Department"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])

model_pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

model_pipeline.fit(X_train, y_train)

predictions = model_pipeline.predict(X_test)

print("Actual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(predictions)

print("\nAccuracy:", accuracy_score(y_test, predictions))

new_data = pd.DataFrame({
    "Age": [26, 42],
    "Salary": [34000, 65000],
    "Department": ["IT", "Sales"]
})

new_predictions = model_pipeline.predict(new_data)

print("\nNew Predictions:")
print(new_predictions)
