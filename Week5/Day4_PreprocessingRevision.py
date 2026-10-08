import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

data = {
    "Age": [22, 25, 28, None, 35, 40, 30, 27, 45, 32, 38, 29],
    "Salary": [25000, 30000, None, 40000, 50000, 60000,
               35000, 32000, 70000, None, 55000, 38000],
    "Department": ["IT", "HR", "Sales", "IT", None, "HR",
                   "Sales", "IT", "Sales", "HR", "IT", "Sales"],
    "Purchased": [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

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

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_transformer, numeric_features),
    ("categorical", categorical_transformer, categorical_features)
])

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_processed, y_train)

predictions = model.predict(X_test_processed)

print("\nProcessed Training Data:")
print(X_train_processed)

print("\nProcessed Testing Data:")
print(X_test_processed)

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(predictions)

print("\nAccuracy:", accuracy_score(y_test, predictions))
