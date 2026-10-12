import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    "Age": [22, 25, 28, None, 35, 40, 30, 27, 45, 32, 38, 29],
    "Salary": [25000, 30000, None, 40000, 50000, 60000,
               35000, 32000, 70000, None, 55000, 38000],
    "Department": ["IT", "HR", "Sales", "IT", None, "HR",
                   "Sales", "IT", "Sales", "HR", "IT", "Sales"],
    "Purchased": [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0]
}

df = pd.DataFrame(data)

df.to_csv("customer_data.csv", index=False)

df = pd.read_csv("customer_data.csv")

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

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

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(predictions)

print("\nAccuracy:")
print(accuracy_score(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

new_customers = pd.DataFrame({
    "Age": [26, 42],
    "Salary": [34000, 65000],
    "Department": ["IT", "Sales"]
})

new_predictions = model.predict(new_customers)

print("\nNew Customer Predictions:")

for i in range(len(new_customers)):
    result = "Purchased" if new_predictions[i] == 1 else "Not Purchased"
    print(new_customers.iloc[i].to_dict(), "->", result)
